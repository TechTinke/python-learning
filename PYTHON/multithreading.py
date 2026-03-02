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


# WORK TO BE DONE 
# 1. Parallel File Downloader
# Create a function download_file(url: str) that uses requests.get() to download a file and save it.
# Use 3 threads to download 3 different image URLs at the same time.
# Use join() to wait for all downloads to finish, then print "All files downloaded".
    

# 2. API Call Fan-Out
# Create fetch_user(user_id: int) that calls a fake API (e.g. https://jsonplaceholder.typicode.com/users/{user_id}).
# Use threads to fetch data for user IDs 1–10 concurrently.
# Collect results and print usernames after all threads finish.


# 3. Image Processing Pipeline (partial code)
# Finish this script to process images concurrently:

# Pythonimport threading
# import time
# from PIL import Image  # pip install pillow

# def resize_image(filename: str, size=(300, 300)):
#     img = Image.open(filename)
#     img = img.resize(size)
#     img.save(f"resized_{filename}")
#     print(f"Resized {filename}")

# # Finish: create list of 5 image filenames (assume they exist)
# # Create a thread for each resize task
# # Start all threads
# # Wait for all to finish using join()
# # Print "All images processed"
# Show how multithreading speeds up processing vs sequential.


# 4. Web Scraper with Thread Pool
# Use concurrent.futures.ThreadPoolExecutor to scrape 20 URLs concurrently.
# Each thread calls requests.get(url) and extracts title using BeautifulSoup.
# Print title + URL for each page.
# Use max_workers=8 and handle exceptions.


# 5. Bank Account Simulation with Race Condition
# Create BankAccount class with balance.
# Create deposit and withdraw methods.
# Use 10 threads to deposit/withdraw random amounts concurrently.
# Show race condition (wrong final balance).
# Then fix it using threading.Lock().


# 6. Producer-Consumer with Queue
# Use queue.Queue and two types of threads:
# 3 producer threads: put random numbers (1–100) into queue every 1–3 seconds
# 2 consumer threads: get numbers from queue, print "Consumed: X"
# Use queue.get() and queue.task_done()
# Run for 20 seconds, then gracefully stop.


# 7. GUI Responsive Counter (Tkinter + threads)
# Create a simple Tkinter window with a counter label and "Start" button.
# When clicked, start a thread that counts from 0 to 100 (sleep 0.1s each).
# Update label every step from the thread (use root.after() or threading.Event).
# Show that GUI remains responsive (you can still click buttons).


# 8. Parallel File Search
# Search for a keyword in 50 text files concurrently.
# Each thread reads one file, checks if keyword exists, and collects matching filenames.
# Use threading.Thread + list to collect results.
# Print all files containing the keyword after all threads finish.


# 9. Thread-Safe Counter with Lock
# Create a shared counter.
# Start 20 threads that each increment the counter 1000 times.
# Without lock → wrong final value (race condition).
# With threading.Lock() → correct value (20000).
# Print before/after to show difference.


# 10. Mini Web Server Load Tester (longer project)
# Create a script that simulates 50 concurrent users hitting a website.
# Each thread:
# Makes 10 GET requests to a URL (e.g. your own site or httpbin.org)
# Measures time per request
# Prints average response time
# Use ThreadPoolExecutor with max_workers=20.
# Show how multithreading helps simulate real load.
