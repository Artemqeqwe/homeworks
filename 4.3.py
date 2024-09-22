import random

new_list = []
for i in range(random.randint(3, 10)):
     new_list.append(random.randint(0, 10))
print(new_list)
for l in new_list:
     l = [new_list[0], new_list[2], new_list[-2]]
print(l)
