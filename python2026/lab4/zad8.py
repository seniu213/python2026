### Task 8
## Utwórz listę 100 losowych liczby
## utwórz podzbiór liczb parzystych większych od 10
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego

from itertools import dropwhile
from random import randint
list1 = [randint(1, 100) for _ in range(100)]
print(list(dropwhile(lambda x: x%2==0 and x>10 ,list1)))