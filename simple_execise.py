command = ""
started = False #
while True: #if command is not = to quit
    command = input(">").lower() #input from user
    if command == "start":
        if started: #if car is already started
            print("car is already started..")
        else:
            started = True
            print("starting car now")
    elif command == "stop":
        if not started:
            print("car is already stopped...")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start -> to start the car 
stop -> to stop the car  
quit -> to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("invalid keyword ")
