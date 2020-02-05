print("Entre your string")
print("PRESS X FOR EXIT")
string = input("Entre any string to count character")
if string=='X':
    exit();
else:
    char=input("entre your character to be searched")
    val=string.count(char)
    print("Frequency=",val)



