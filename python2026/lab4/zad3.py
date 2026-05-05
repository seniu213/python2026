##### Task 3
### Utwórz pętlę generującą 50 liczb całkowitych z krokiem 5, większych niż 99
### Wykorzystaj count()

from itertools import count

counter = 0

for i in count(99, 5):
    if counter == 50:
        break
    print(i)
    counter += 1