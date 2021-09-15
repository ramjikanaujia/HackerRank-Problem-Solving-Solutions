
def area_highlighted(h_words, word):
    letters = [ord(i.lower()) - ord('a') for i in word]
    area = max([h_words[i] for i in letters]) * len(letters)
    return area

h = list(map(int, input().strip().split(' ')))
word = input().strip()
print (area_highlighted(h, word))