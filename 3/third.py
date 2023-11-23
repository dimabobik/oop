statement = False
another_statement = True
if statement is True:
    print('This Is If choice')
elif another_statement is True:
    print('This is Elif choice')
else:
    print('This is else choice')
#SECOND TASK --------------------------------------------------------
f = 17

if f < 10:
    print('f > 10 YES ')
else:
    print('No!')

#3 TASK --------------------------------------------------------------
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
else:
    print('NoName')


#4 TASK --------------------------------------------------------------

listFor = [0, 1, 2, 3, 4]
for x in listFor:
    print(x)

# Prints out 3,4,5
for x in range(2, 3):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)