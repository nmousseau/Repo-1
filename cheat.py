print("hello world")

pageBreak = "############## \n" 

add = 2 + 2
print("this is the add variable")
print(add)
print(pageBreak)

# + - * / // ** %

minus = 4 - 2
print("this is the minus variable")
print(minus)
print(pageBreak)

times = 2 * 4
print("this is the times variable")
print(times)
print(pageBreak)

divide = 8 / 2
print("this is the divide variable")
print(divide)
print(pageBreak)

divideLeftOver = 5 / 2
print("this is the divideLeftOver variable")
print(divideLeftOver)
print(pageBreak)

divideShowInteger = 5 // 2
print("this is the divideShowInteger variable")
print(divideShowInteger)
print(pageBreak)

exponent = 2 ** 3
print("this is the exponent variable")
print(exponent)
print(pageBreak)

remainder = 5 % 2
print("this is the remainder variable")
print(remainder)
print(pageBreak)

print("this is defining a variable be sure it is defined before called for")
def printLyrics():
    lyrics = ("I'm a lumberjack, and I'm really lazy.")
    lyrics = lyrics + ("i sleep all day and I work all day.")
    if False:
        return lyrics
    elif True:
        return pageBreak

print(printLyrics())

i = 0
while i < 5:
    print('hello')
    i += 1

for number in range(12, 20):
    print(number)

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n##############')
    j = 0
    i += 1

print(pageBreak)

numb = 1
if numb == 1:
    print("one")
elif numb == 2:
    print("two")
else:
    print("bigger number")
print(pageBreak)

fruits = ['apple', 'orange', 'banana', 'grape']
print(pageBreak)

string = "catch my catatonic cat."
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)
if (subString in string):
    print("yes")
else:
    print("no")
crazyString = "I will be easy to cAtch my cAtAtonic cat."
stringIndex = crazyString.find(subString)
print(stringIndex)
stringIndex = crazyString.lower().find(subString)
print(stringIndex)
print(crazyString.lower())
print(crazyString)
if crazyString > string:
    print("crazy")
else:
    print("lower is greater than uppercase")

if "Z" < "a":
    print("uppercase letters come first")
stringIndex = string.find(subString, 19)
print(stringIndex)
someValues = "Laconia Gilfrod Belmont"
listOfValues = someValues.split()
print(listOfValues[1])
keyValuePairs = "Bill: Laconia, Jane: Gilford, Tom: Belmont"
listOfPairs = keyValuePairs.split(",")
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is " + fname + "\n town is: " + town)
    count += 1


#loop example


mystring = "acbcdce"
count_c = 0
for letter in mystring:
    if letter == 'c':
        count_c += 1
        #print("hello" + str(count_c))

print(count_c)
