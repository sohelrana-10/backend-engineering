import os

li=os.listdir()
print(li)
for l in range(4):
    print(li[l])
    os.remove(li[l])

