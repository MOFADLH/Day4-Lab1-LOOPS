for i in range (45, 210,1):
    if i == 100:
        continue
    if i == 205:
        break 
    print (i)

while True :
    name = input('what is the product of 7 * 24 ?')
    if name != '168':
        print('YYour Answer is wrong try again..')
        continue
    if name == '168':
        print('You answered this Question correctly')
        break