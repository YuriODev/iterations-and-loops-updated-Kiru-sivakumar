#given n > 20,  print all the numbers between 20 and n inclusive:
n = int(input('Please enter the upper bound number:'))
for i in range(20 , n+1):
    print(i, end =' ')
while n < 20 :
    print('n is less than 20 try again')
    n = int(input('Please enter the upper bound number:'))
    
