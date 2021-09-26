#practicing file

import lk

text = open("1235.txt", "a")
text.write("e = 100")
text.close()

text = open("123.txt", "r")
for t in text.readlines():
    print(t)
text.close()

print(lk.random_number(5))