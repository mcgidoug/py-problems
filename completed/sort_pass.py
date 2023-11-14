# todo
# write a func that sorts through an array of passwords and returns the ones containing a certain char

arr = ["word", "dog", "hat", "hello", "wash", "text", "flock"]

def pull_words(letter):
    new_arr = []
    for word in arr:
        if letter in word:
            new_arr.append(word)
    print(new_arr)


pull_words("o")