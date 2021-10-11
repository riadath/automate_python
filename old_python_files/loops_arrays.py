char_arr = ['in', 'the', 'heat', 'of', 'the']
arr2 = ['The', 'is', 'not', True, False]
arr_new = [True, False, False, True, 'NEGRO']
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)


def odd_even_check(num):
    if num % 2 == 0:
        return False
    else:
        return True


for i in arr:
    print(f"The number is {i}")
for j in char_arr:
    print(j)
for k in arr2:
    print(f'The element is {k}')
for i in range(9, 15):
    arr.append(i)
print(arr)

for i in range(0, 5):
    print(f"LOOP NO: {i}")
    print('arr', arr[i])
    print('char arr', char_arr[i])
    print('arr2', arr2[i])
    print('arr_new', arr[i])
    i += 1
