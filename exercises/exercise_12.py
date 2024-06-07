n = int(input('please enter a three digit number'))
s = 0
for i in range(100, 1000):
    
    if i % n == 0:
        
        s += i 

while len(str(n)) != 3:
    print('not a 3 digit integr try again.')
    n = int(input('Enter a 3 digit number:'))
print(s)
