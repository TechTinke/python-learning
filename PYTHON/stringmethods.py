name = input("Enter your full name: ")
phone_number = input("Please input your phone number: ")

result = len(name)#if you ever need the length of a string you use len
result = name.find(" ")#the first character always has the index 0#find is used to find the first occurence of a particular character
result = name.rfind(" ")#rfind is used to find the last occurence of a particular character
name = name.capitalize()#capitalizes the first letter of the string
name = name.upper()#makes all the characters in uppercase
name = name.lower()#makes all the characters in lowercase
result = name.isdigit()#returns true or false: true if the string only contains digits and false if no/some digits in the string
result = name.isalpha()#returns true or false: true if the string contains alphabetical characters only

result = phone_number.count("-")#counts the number of specified characters
phone_number = phone_number.replace("-", "")#replaces specified characters with something else


#VALIDATE USER INPUT
#1. Must not be more than 12 characters
#2. Must not contain any spaces
#3. Must not contain any digits


username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cannot contain more than 12 characters")
#elif not username.find(" ") == -1:
    #print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
else:
    print(f"Welcome, {username}")

