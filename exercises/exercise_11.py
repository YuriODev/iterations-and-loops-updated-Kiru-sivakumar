n = int(input('enter the upper bound:'))

sos = 0
for i in range(1,n+1):
    sos += i/(i+1)
print(f'{sos:.2f}')
