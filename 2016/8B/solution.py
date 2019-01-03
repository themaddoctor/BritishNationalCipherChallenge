alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key      = 'DYNAMIXZBCEFGHJKLOPQRSTUVW'
c = open('ciphertextB.txt','r').read().replace(' ','').replace('\n','')
things = c.split('2')[:-1]
p = ''
for i in range(len(things)//5):
    for j in range(len(things[i*5])):
        number = 0
        for k in range(4,-1,-1):
            number *= 2
            number += int(things[i*5+k][j])
        p += alphabet[key.index(alphabet[number])]
    p += ' '
print (p.lower())
