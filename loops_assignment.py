# Qn. 1

print("Enter list size: ")
list_size = input()

ans = [x for x in range(int(list_size))]

print(ans)


# Qn. 2

a_list = ['abc', 'xyz', 'aba', '1221']
count = 0

for word in a_list:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print(count, 'words.')

# Qn. 3
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]

new_arr = []
[new_arr.append(f) for f in fruits if f not in new_arr]

print(new_arr)

# Qn. 4

spec_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
spec_list.pop(0)
spec_list.pop(4)
spec_list.pop(5)
print(spec_list)

# Qn. 5

ans_arr=[]
for x in range(30):
    v = x**2
    ans_arr.append(v)
del ans_arr[0:5]

print(ans_arr)
