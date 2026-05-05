# # ################################ Task 0
# '''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a 
## single line. Don't forget about function documentation

def find_numbers(x, y):
    """Zwraca pasujace liczby."""
    return [n for n in range(x, y + 1) if n % 7 == 0 and n % 5 != 0]


x = 1000
y = 2101
result = find_numbers(x, y)
print(','.join(map(str, result)))
