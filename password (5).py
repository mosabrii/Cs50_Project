import string

while True:
    x = input("password: ")
    i = len(x)

    if i < 8:
           print("Password too small!")
           continue
    else:
           break
j = 0
if 8 <= i <= 16:
     j += 10
elif 17 <= i <= 24:
     j += 45

if any(ch.isdigit() for ch in x):
     j += 5
if any(ch.isupper() for ch in x):
     j += 15
if any(ch.islower() for ch in x):
     j += 15
if any(ch in string.punctuation for ch in x):
     j += 20

if j >= 70:
     print("Protection: Red")
elif 40 <= j <= 65:
     print("Protection: Yellow")
else:
     print("Protection: Blue")
