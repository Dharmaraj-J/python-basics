started = False
while True :
    command = input("> ").lower()
    if command == "help":
          print('''
start -  to start the car
stop - to stop the car
quit = to quit
          ''')
    elif command == "start":
        if started:
            print("the car is already started")
        else:
            started=True
            print('car started ...')
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("car is stoped.")
    elif command == "quit":
        break
    else:
        print("sorry,I don't understand that !")



