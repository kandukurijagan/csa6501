from transformers import BertTokenizer,BertModel
import torch
tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")
model=BertModel.from_pretrained("bert-base-uncased")
s1=tokenizer("The cat is on the mat",return_tensors="pt")
s2=tokenizer("A cat sits on the mat",return_tensors="pt")
e1=model(**s1).last_hidden_state.mean(dim=1)
e2=model(**s2).last_hidden_state.mean(dim=1)
print(e1)
print(e2)