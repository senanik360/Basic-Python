num = {10,20,30,40,50,60,60}
 #can not print duplicate value
print(num)

numN = set([10,20,30])

print(numN)

numN.add(40)
print(numN)

numN.remove(40)
print(numN)

print(20 in numN)  #return ture if exists
print(20 not in numN)  #return false

print(num | numN)  #union between num and numN
print(num & numN)  #intersection between num and numN
print(num - numN)  #difference between num and numN
