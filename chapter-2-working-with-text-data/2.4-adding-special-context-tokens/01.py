import re
with open("../the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_tokens)
print(vocab_size) # 1130 -> 1132


# create a vocabulary
vocab = { token: integer for integer,token in enumerate(all_tokens)}

for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)