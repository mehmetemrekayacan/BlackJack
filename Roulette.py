import random

number=range(0,37)
colour=["red","black"]

yourNumber=random.choice(number)
yourcolour=random.choice(colour)

x=input("1.Just number range\n2.Just colour\n3.Both of them\n:")

if x=="3":
    a=input("1.(0-12)\n2.(13-24)\n3.(25-36)\n:")
    b=input("1.Red\n2.Black\n:")
    if a=="1" and yourNumber==range(0,13) and ((b=="1" and yourcolour=="red") or (b=="2" and yourcolour=="black")):
        print("You win 4x!")
    elif a=="2" and yourNumber==range(13,25) and ((b=="1" and yourcolour=="red") or (b=="2" and yourcolour=="black")):
        print("You win 4x!")
    elif a=="3" and yourNumber==range(25,37) and ((b=="1" and yourcolour=="red") or (b=="2" and yourcolour=="black")):
        print("You win 4x!")
    else:
        print("You lost!")
elif x=="2":
    c=input("1.Red\n2.Black\n:")
    if (c=="1" and yourcolour=="red") or (c=="2" and yourcolour=="black"):
        print("You win 2x!")
    else:
        print("You lost!")
elif x=="1":
    d=input("1.(0-12)\n2.(13-24)\n3.(25-36)\n:")
    if d=="1" and yourNumber==range(0,13):
        print("You win 2x!")
    elif d=="2" and yourNumber==range(13,25):
        print("You win 2x!")
    elif d=="3" and yourNumber==range(25,37):
        print("You win 2x!")
    else:
        print("You lost!")

print(f"Roulette is {yourNumber} and {yourcolour}")
