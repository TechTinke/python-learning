# multithreading = Used to perform multiple tasks concurrently(multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading.Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# The 3 tasks are achieved one at a time and not concurrently
# walk_dog()
# take_out_trash()
# get_mail()

# Executing the chores concurrently
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# Join method is used to wait to wait for the threads to finish before continuing with the rest of the program
chore1.join()
chore2.join()
chore3.join()
print("All chores have been completed!")

