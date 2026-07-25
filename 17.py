from transformers import BertTokenizer,BertModel
import torch
tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")
model=BertModel.from_pretrained("bert-base-uncased")
inputs=tokenizer("Data Science is fun",return_tensors="pt")
outputs=model(**inputs)
print(outputs.last_hidden_state)