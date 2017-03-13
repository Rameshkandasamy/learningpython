'''#1 get age and tell when they will be 100 years old
name =  raw_input("Enter your Name")

current_age = int(input("Enter your current age"))

hundredyear = 100 - current_age
##print ("{0} You will turn 100 years in {1} years!!").format(name,hundredyear)
print (name + ", You will turn 100 years in " + str(hundredyear) + " years!!")

#2 div/2
number = int(input("Enter your number: "));

if (number%2) == 0:
    print("You entered an even number, {0}").format(number)
else :
    print ("You entered an odd number, {0}" ).format(number)


#p = L[::-1


#listb = lista[::-1]
#listb = []
#for i in reversed(lista):
#    listb.append(i);
#    print i;
##for i in listb


#3
number = int(input("Enter your number"))
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
listb = []

for l in lista:
    if l <= number:
        listb.append(l)

#for b in listb:
print listb

#4
number = int(input("Enter a number"));
divisor = []
for i in range(2,number):
    if number%i == 0:
        divisor.append(i)
print divisor;

#5
a = [1,3,5,7,11,13,17,19]
b = [1,1,3,5,6,7]
c = []

for i in a:
    if i in b:
        c.append(i)
print c

#6
a = str(raw_input("Enter your string for palindrome check: "))
b = ''

for i in range(0,(len(a))):
    b += a[len(a) -i -1]
if a == b:
    print ("You have a palindrome string!")
else:
    print ("No beans!")
def isPalindrome(input):
    #inputStr = (str) input
    reversedInput = input[::-1]
    return input == reversedInput

print isPalindrome("malayalam")
print isPalindrome("xoxoxo")

'''



#7 print only evens in a list.
a = [1,2,3,5,6,7,8,9,4543,32,2,245,845]
b = []
for i in a:
    if(i%2 == 0 ):
        b.append(i)
print b

c = [number for number in a if number%2 == 0]

print c

