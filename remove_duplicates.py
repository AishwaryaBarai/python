orig_list = [3,6,4,5,4,5,6,7,8,7,8,9,8]
new_list = []
for num in orig_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)
