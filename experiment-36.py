!pip install diffusers transformers accelerate torch

from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
).to("cuda")

prompts = [
    "A simple robotic arm in an engineering laboratory",
    "A futuristic robotic arm in an advanced engineering laboratory",
    "A highly detailed humanoid robot working in a futuristic engineering laboratory"
]

images = []

for prompt in prompts:
    image = pipe(prompt).images[0]
    images.append(image)

plt.figure(figsize=(15, 5))

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i])
    plt.title(f"Prompt {i + 1}")
    plt.axis("off")

plt.show()
