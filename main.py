#practicing file

import lk

text = open("1235.txt", "a")
text.write("e = 100")
text.close()

text = open("123.txt", "r")
for t in text.readlines():
    print(t)
text.close()

a = int(input("Please type a number:"))
sum = 0
for i in range (a):
    sum += i+1
print(sum)
print(lk.random_number(5))
print(Hello)