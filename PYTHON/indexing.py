#indexing = accessing elements of a sequence using [](indexing operator)
            #[start : end : step]

credit_number = "1234-4747-7548-4783"
print(credit_number.index("7"))#prints out the index of the specified digit within the sequence
                              #the specified digit/character should be stringified
print(credit_number[4])#prints out the digit in the index 4
print(credit_number[5:9])#prints out the digits in the indexes 5,6,7,8 of the sequence
print(credit_number[5:])#prints out the digits from index 5 to the end of the sequence
print(credit_number[-1])#print out the last digit

#EXERCISE
#PRINT THE LAST DIGITS OF A CREDIT CARD
last_digits = credit_number[15:]
l_digits = credit_number[-4:]
print(f"Owner of Credit Card NO XXXX-XXXX-XXXX-{last_digits}")
print(f"Owner of Credit Card NO XXXX-XXXX-XXXX-{l_digits}")

#EMAIL SLICER EXERCISE
email = input("Enter your email: ")
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username.capitalize()} and your domain is {domain}")


