from transformers import BertTokenizer
tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")
tokens=tokenizer.tokenize("Machine learning is interesting")
print(tokens)