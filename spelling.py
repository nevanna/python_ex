def remove_repeats(mistakes):
    i = len(mistakes)-1
    while i >= 0:
        if mistakes.count(mistakes[i]) > 1:
            mistakes.pop(i)
        i-=1
    for w in mistakes:
        print(w)


def check_spelling(words, text):
    mistakes = []
    for raw in text:
        for word in raw:
            if not(word.lower() in words):
                mistakes.append(word)
    remove_repeats(mistakes)

def spelling():
    nb_w  = int(input())
    words = []
    for i in range(0, nb_w):
        words.append(str(input()))
    nb_raws = int(input())
    text = []
    for i in range (0, nb_raws):
        text.append(str(input()).split(" "))
    check_spelling(words, text)
    


    pass
if __name__ == "__main__":
    spelling()
    pass