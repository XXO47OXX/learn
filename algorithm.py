print('looping in list')
data = [x for x in range(20)]
print(data)

print('\n = = = odd_even = = = =')
odd_even = [f'{x} - even' if x %
            2 == 0 else f'{x} - odd' for x in range(1, 21)]

for x in odd_even:
    print(x)


print('\n = = = fizbuzz = = = =')
fizbuzz = [f'{x} - fizbuzz' if x % 15 == 0 else f'{x} - buzz' if x %
           3 == 0 else f'{x} - fizz' if x % 5 == 0 else x for x in range(1, 21)]
print(fizbuzz)
for x in fizbuzz:
    print(x)


print('\n = = = fibonaci = = = =')


def fibonaci(n: int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)


lala = [fibonaci(x) for x in range(21)]
i = 0
for x in lala:
    print(f'{x} index {i}')
    i += 1

print('\n = = = palindrome = = = =')
data_palin = 'maaaaa'
is_palindrome = ['its palindrome' if data_palin.lower().replace(
    ' ', '') == data_palin[::-1].lower().replace(' ', '') else 'its not palindrome']
print(is_palindrome)


print('\n = = = sorting using looping = = = =')

arr = [0, 1, 2, 3, 5, 2, 1, 45, 12, 4, 1, 2, 4, 1]
print(arr)
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
