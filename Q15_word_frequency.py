
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq



    s = "python is fun and python is powerful"
    print(word_frequency(s))
