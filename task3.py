text = ('посмотри , как красив этот мир , посмотри')
words= text.split()

word_count = {}
for i in words:
    word_count[i]= word_count.get (i, 0)+1

for i, count in word_count.items():
    print(f"{i}: {count}")