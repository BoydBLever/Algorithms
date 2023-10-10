#Implement A Lock is a Microsoft interview question listed on Glassdoor. The lock I choose to implement is a mutex lock. Though it is a logical construct, it bears similarities conceptually to a door lock with a thread acting as the key, and where the critical region is most like a room.
import threading

# Initialize a shared counter
counter = 0

# Create a mutex using the Lock class from the threading module
mutex = threading.Lock()

def increment_counter():
    global counter
    
    # Acquire the mutex. If it's already locked, the thread will block until it's unlocked.
    mutex.acquire()
    
    # Critical section: Only one thread can execute this at a time because of the mutex
    temp = counter
    counter = temp + 1
    
    # Release the mutex so other threads can acquire it
    mutex.release()

# Start multiple threads that will try to increment the counter
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(counter)
