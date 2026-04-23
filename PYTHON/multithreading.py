# multithreading = Used to perform multiple tasks concurrently(multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading.Thread(target=my_function)

import threading
import time
def walk_dog(first,last):
    time.sleep(4)
    print(f"You finish walking {first} {last}")
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
def get_mail():
    time.sleep(2)
    print("You take out the trash")

# The 3 tasks are achieved one at a time and not concurrently
# walk_dog("Scooby", "Doo")
# take_out_trash()
# get_mail()

# # Executing the chores concurrently
# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # Join method is used to wait to wait for the threads to finish before continuing with the rest of the program
# chore1.join()
# chore2.join()
# chore3.join()
# print("All chores have been completed!")


# WORK TO BE DONE 
# 1. Restaurant Kitchen
# A restaurant kitchen processes multiple orders at the same time.
# Write three functions — make_pizza(order_id), make_burger(order_id), and make_salad(order_id) —
# each with a time.sleep() to simulate cooking time.
# Run all three concurrently using threads and use join()
# to wait for all of them to finish before printing "All orders ready!".
# Compare what happens when you run them without threads.
# import time
# import threading

# def make_pizza(order_id):
#     print("Making pizza...")
#     time.sleep(4)
#     print("Pizza is ready!")
# def make_burger(order_id):
#     print("Making burger...")
#     time.sleep(6)
#     print("Burger is ready!")
# def make_salad(order_id):
#     print("Making salad...")
#     time.sleep(5)
#     print("Salad is ready")
# pizza = threading.Thread(target=make_pizza, args=(2,)) #args needs a tuple not a single value
# pizza.start()
# burger = threading.Thread(target=make_burger, args=(1,))
# burger.start()
# salad = threading.Thread(target=make_salad, args=(3,))
# salad.start()

# pizza.join()
# print(" ")
# burger.join()
# print(" ")
# salad.join()
# print("All orders are ready")

# 2. Spot the Bug
# The following multithreading code is meant to run two tasks concurrently
# but they run one after the other instead.
# Identify and fix it:

# import threading
# import time

# def download_file(filename):
#     time.sleep(3)
#     print(f"{filename} downloaded!")

# def send_email(recipient):
#     time.sleep(2)
#     print(f"Email sent to {recipient}!")

# t1 = threading.Thread(target=download_file, args=("report.pdf",))
# t1.start()
# t2 = threading.Thread(target=send_email, args=("oscar@gmail.com",))
# t2.start()

# t1.join()
# t2.join()

# 3. Thread Naming
# A logging system needs to identify which thread is doing what.
# Write three functions that each print the name of the thread currently running them
# using threading.current_thread().name.
# Create three threads with custom names using the name parameter in threading.Thread()
# and run them concurrently. This introduces threading.current_thread().


# import threading
# import time

# def task_one():
#     print(f"Thread running: {threading.current_thread().name}")
#     time.sleep(2)
#     print(f"Thread finished: {threading.current_thread().name}")
# def task_two():
#     print(f"Thread running: {threading.current_thread().name}")
#     time.sleep(3)
#     print(f"Thread finished: {threading.current_thread().name}")
# def task_three():
#     print(f"Thread running: {threading.current_thread().name}")
#     time.sleep(4)
#     print(f"Thread finished: {threading.current_thread().name}")

# t1 = threading.Thread(target=task_one)   # ✅ Custom name
# t1.start()
# t2 = threading.Thread(target=task_two)   # ✅ Custom name
# t2.start()
# t3 = threading.Thread(target=task_three)  # ✅
# t3.start()

# t1.join()
# t2.join()
# t3.join()

