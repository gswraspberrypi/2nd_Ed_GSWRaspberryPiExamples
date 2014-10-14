# GSW Raspberry Pi ch 3 example 2
# Declare global variables
n = 0 

# Setup function
def setup(): 
    global n
    n = 100

# Loop function
def loop(): 
    global n
    n = n + 1
    if ((n % 2) == 0):
        print(n)

# Main
setup()
while True:
    loop()