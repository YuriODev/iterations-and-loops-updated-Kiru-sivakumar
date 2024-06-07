pw = int(input('enter a pw:'))
pw2 = int(input('reneter pw:'))
fin = False
while fin == False:
    if pw2 != pw:
        print('Error!')
        pw2 = int(input('reneter pw:'))
        
    if pw2 == pw:
        print('done')
        fin  = True
