s = input("Enter - ")

if len(s)<1:s = 'azcbobobegghakl'
smax = ''
cl=0
cr=1
while cr<len(s):
    stm=''
    while cr<len(s) and s[cr] >= s[cr-1]: 
        cr+=1
    stm += s[cl:cr]
    print(stm)
    if len(smax)<len(stm): smax = stm
    cl = cr
    cr = cr+1

print('Longest substring in alphabetical order is:', smax)
