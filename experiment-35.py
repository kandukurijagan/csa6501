!pip install diffusers transformers accelerate torch

from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda")

prompt = """
A futuristic suspension bridge designed by engineers,
modern architecture, strong steel structure,
river below, realistic, highly detailed
"""

image = pipe(prompt).images[0]

image.save("engineering_bridge.png")

display(image)
