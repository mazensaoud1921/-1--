binary=[]
def dectobin(decimal):
    if(decimal > 0):
        dectobin((int)(decimal//2))
        print(decimal%2,end='')
decimal=int(input("أدخل الرقم العشري--->:"))
dectobin(decimal)
binary.append([1,2,3])
print(binary)
binary.append(8)
print(binary)
binary.reverse()
print(binary)
