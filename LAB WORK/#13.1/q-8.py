#Q-8 Write a program that simulates a stopwatch. Allow the user to start, stop, and reset the stopwatch using the time module.

import time

start_time = None
elapsed_time = 0

while True:

    print("\n1. Start")
    print("2. Stop")
    print("3. Reset")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if start_time is None:
            start_time = time.monotonic()
            print("Stopwatch Started")
        else:
            print("Stopwatch is already running")

    elif choice == "2":

        if start_time is not None:
            elapsed_time += time.monotonic() - start_time
            start_time = None

            print("Stopwatch Stopped")
            print("Elapsed Time:", elapsed_time, "seconds")
        else:
            print("Stopwatch is not running")

    elif choice == "3":

        start_time = None
        elapsed_time = 0

        print("Stopwatch Reset")

    elif choice == "4":

        print("Program Ended")
        break

    else:
        print("Invalid Choice")