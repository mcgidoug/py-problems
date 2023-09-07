s = "Its to easy"

def add_len(s):
    word_lengths = []
    words = s.split()
    for word in words:
        word_lengths.append(f"{word} {len(word)}")
    return word_lengths

print(add_len(s))
