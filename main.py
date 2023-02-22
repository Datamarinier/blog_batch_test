import sys
import time

def long_running_function(n):
    for i in range(n):
        time.sleep(1)
        print(f"Processed {i+1} out of {n} items...")

if __name__ == "__main__":
    try:
        long_running_function(60)
    except Exception as err:
        print("Error occurred:", err)
        sys.exit(1)
