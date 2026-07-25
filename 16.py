from transformers import BertTokenizer,GPT2Tokenizer
bert=BertTokenizer.from_pretrained("bert-base-uncased")
gpt2=GPT2Tokenizer.from_pretrained("gpt2")
text="Artificial Intelligence is changing the world"
print(bert.tokenize(text))
print(gpt2.tokenize(text))