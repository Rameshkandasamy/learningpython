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

#print isPalindrome("malayalam sis malayalam")
#print isPalindrome("xoxoxox")


