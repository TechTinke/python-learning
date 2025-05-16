#for loops = executes a block of code a fixed number of times.
            #You can iterate over a range, string, sequence
#continue keyword is used for skipping a certain part of an iteration
#break keyword is used for breaking out of the loop entirely

credit_card_no = "1234-5664-7583-2833"

for x in credit_card_no:#1 is the start #11 is the end but exclusive(is not included) #3 is the periodicals
    print(x)

#continue keyword is used to skip a certain part of an iteration
for count in range(1, 21):
    if count == 13:
        continue
    else:
       print(count)

#break keyword is used to break out of the loop entirely
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)
