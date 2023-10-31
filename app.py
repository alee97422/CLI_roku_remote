import readline
from roku import Roku

# Define the list of commands, including "back"
commands = ["peacock","home", "up", "down", "left", "right", "select", "back", "play", "forward", "reverse", "netflix", "exit", "back"]

# Custom completer function
def complete(text, state):
    options = [cmd for cmd in commands if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Set the completer function
readline.set_completer(complete)

# Enable tab-completion
readline.parse_and_bind("tab: complete")

while True:
    print("1. Bedroom: 192.168.1.***")
    print("2. Kids room: 192.168.1.***")
    print("3. Living Room: 192.168.1.***")
    print("from command screen use command {back2IP} to go back to IP screen")
    roku_ip = input("Enter the Roku Device IP address ( 'exit' to quit):")

    if roku_ip == "exit":
        break

    try:
        roku = Roku(roku_ip)
        netflix = roku.apps[0]
        peacock = roku.apps[11]

        while True:
            action = input("Enter a command: ")

            if action == "exit":
                exit() 
            elif action == "back2IP":#edit this if you wanna use a diff command to go back to IP screen 
                break  
            elif action in commands:
                if action == "netflix":
                    netflix.launch()
                if  action == "peacock":
                    peacock.launch()
                else:
                    getattr(roku, action)()
            else:
                print("Invalid command. Please enter a valid command.")
    except Exception as e:
        print(f"Failed to connect to Roku with IP address {roku_ip}. Make sure the IP address is correct and the Roku device is reachable.")
