import time

print("Press enter to start the stopwatch")
input()
print("Stopwatch started")

start_time = time.time()

print("Press enter to stop the stopwatch")
input()

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
