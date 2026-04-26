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

# t1 = threading.Thread(target=task_one, name="Logger-1")   # ✅ Custom name
# t1.start()
# t2 = threading.Thread(target=task_two, name="Logger-2")   # ✅ Custom name
# t2.start()
# t3 = threading.Thread(target=task_three, name="Logger 3")  # ✅
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# Thread Naming matters in production systems for debugging because you'd seee thousands of these lines
# [Logger-1] Processing payment for user 001
# [Logger-2] Fetching data from API
# [Logger-3] Writing to database


# 4. Concurrent File Downloader
# Write a function download_file(filename, size_mb) that simulates a download
# by sleeping for size_mb * 0.5 seconds and prints when the download starts and finishes.
# Create a list of 5 files with different sizes and download all of them concurrently using threads.
# Print the total time taken and compare it to sequential downloading.

# queue.Queue() in Python is a thread-safe FIFO (First-In, First-Out) data structure from the queue module.
# It’s mainly used when multiple threads need to safely share data without corrupting it.

# time.time() - record current time so that you can calculate how long something took

# import threading
# import time 
# def download_file(filename, size_mb):
#     print(f"Starting download: {filename}")
#     time.sleep(size_mb * 0.5)
#     print(f"Finished download: {filename}")

# the values are stored as a tuple
# files = [
#     ("report.pdf", 6),
#     ("exam.txt", 4),
#     ("video.mp4", 20),
#     ("image.jpg", 3),
#     ("data.csv", 8)
# ]

# start_time = time.time()
# threads = []
# for filename, size_mb in files:
#     t = threading.Thread(target=download_file, args=(filename, size_mb))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# end_time = time.time()
# print(f"Total time: {end_time - start_time:.2f} seconds")

# 5. Thread Safety with Locks
# A ticket booking system has a race condition.
# Write a TicketCounter class with a class variable tickets = 10.
# Write a function book_ticket(name) that checks if tickets are available and decrements the count.
# Run 15 threads simultaneously all trying to book a ticket —
# first without a lock to show the race condition, then with a threading.Lock() to fix it.
# Explain what a race condition is and why it's dangerous.

# RACE CONDITION - count foes below zero
# In a Race Condition, the next thread reads stale data and still processes the thread 
# Without a lock threads read stale data before other threads finish updating it —
# a lock forces them to wait their turn so they always read the latest value!

# import threading
# import time

# class TicketCounter():
#     tickets = 10
#     lock = threading.Lock() #Lock forces each thread to wait its turn so that they always read the latest value

# def book_ticket(name):
#     with TicketCounter.lock:
#         if TicketCounter.tickets == 0:
#             print(f"Sorry {name} - Tickets sold out!")
#         else:
#             print(f"Booking ticket for {name}...")
#             time.sleep(0.1) # Small sleep exposes race condition
#             TicketCounter.tickets -= 1
#             print(f"Ticket booked for {name}successfully booked")

# names = ["Oscar", "Abel", "Praise", "Jerome", "Anne", "Yula", "Kivua", "Michael", "Abel", "Maingi", "Mary", "Cate", "Winnie", "Nzula", "Grace"]
# ticket_threads = []
# for name in names:
#     ticket = threading.Thread(target=book_ticket, args=(name, ))
#     ticket_threads.append(ticket)
#     ticket.start()

# for ticket in ticket_threads:
#     ticket.join()
# print(f"Final ticket count: {TicketCounter.tickets}")

# 7. Thread Pool
# A web scraper needs to fetch data from 10 URLs efficiently.
# Use concurrent.futures.ThreadPoolExecutor to create a pool of 3 worker threads.
# Write a function fetch_url(url) that simulates fetching data with time.sleep().
# Submit all 10 URLs to the pool and collect results.
# Compare this to creating 10 individual threads and explain why thread pools are better for managing large numbers of tasks.



# Thread Pools - used for managing a large number of tasks as threads are automatically managed:
# - Creating threads
# - Starting threads
# - Tracking threads
# - Joining threads 
# In Thread Pools, threads are reused but are not recreated per task that happening in the background of course


# import time
# from concurrent.futures import ThreadPoolExecutor
# urls =[
#     "https://google.com",
#     "https://chatgpt.com",
#     "https://moringaschool.com",
#     "https://gemini.com",
#     "https://google.com",
#     "https://google.com",
#     "https://google.com",
#     "https://google.com",
#     "https://x.com",
#     "https://instagram.com"
# ]

# def fetch_url(url):
#     print(f"Fetching data from {url}...")
#     time.sleep(2)
#     print(f"Successfully fetched data from {url}")
#     # executor = ThreadPoolExecutor(max_workers=3) # Creates a pool of 3 worker threads

# with ThreadPoolExecutor(max_workers=3) as executor:
#     url_futures = [executor.submit(fetch_url, url) for url in urls]

#     for url_future in url_futures:
#         url_future.result()
        # print(url_future.result())
        

# from concurrent.futures import ThreadPoolExecutor
# import time

# def task(n):
#     time.sleep(1)
#     return f"Done {n}"

# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(task, i) for i in range(5)]

#     for f in futures:
#         print(f.result())

# Why Thread Pools are better than individual threads
# INDIVIDUAL THREADS
# - Create 10 threads for 10 URLs.
# - All 10 run at once - consumes more memory due to heavy memory usage
# - Hard to collect thread results
# - Manual thread management

# POOL OF THREADS
# - Only 3 threads handle all 10 URLs
# - Only 3 threads  run at a time — controlled memory due to small memory usage
# - resultsfuture.result() makes it easy and fast to collect thread results
# - Thread Pool manages everything automatically




    


