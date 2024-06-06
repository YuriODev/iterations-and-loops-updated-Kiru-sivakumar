a= int(input ('enter the first num:'))
b = int(input('enter the second num:'))
c = int(input('enter the third num:'))
for i in range (a,b+1):
    if i%c == 0:
        print(i, end = ' ')
