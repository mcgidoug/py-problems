word = "hello"

def replace_word(word, newWord):
    replaced_word = word.replace(word, newWord)
    return replaced_word

result = replace_word(word, "why")
print(result)