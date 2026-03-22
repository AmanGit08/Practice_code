#write the code to store the name of the student with there known language
# take the 8 input from the user

s = {}

name = input("Enter the name")
value = input("enter the value")
s.update({name:value}) # this is how the value is add to the empty dictionay
print(type(s))
print(s)