import sys, time


fallback = [   
            "         .?77777777777777$.              ",
            "          777..777777777777$+            ",
            "         .77    7777777777$$$            ",
            "         .777 .7777777777$$$$            ",           
            "         .7777777777777$$$$$$            ",
            "         ..........:77$$$$$$$            ",           
            "  .77777777777777777$$$$$$$$$.=======.   ",  
            " 777777777777777777$$$$$$$$$$.========   ",  
            "7777777777777777$$$$$$$$$$$$$.=========  ", 
            "77777777777777$$$$$$$$$$$$$$$.=========  ",
            "777777777777$$$$$$$$$$$$$$$$ :========+. ",
            "77777777777$$$$$$$$$$$$$$+..=========++~ ",
            "777777777$$..~=====================+++++ ",
            "77777777$~.~~~~=~=================+++++. ",
            "777777$$$.~~~===================+++++++. ",
            "77777$$$$.~~==================++++++++:  ", 
            " 7$$$$$$$.==================++++++++++.  ", 
            " .,$$$$$$.================++++++++++~.   ",  
            "         .=========~.........            ",           
            "         .=============++++++            ",           
            "         .===========+++..+++            ",           
            "         .==========+++.  .++            ",          
            "          ,=======++++++,,++,            ",           
            "         . .=====+++++++++=.             ",            
            "               ..~+=...                  ",     
            "                 '''                     "
        ]

def calculate_checksum(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        checksum = hash(content)
        return checksum
    except FileNotFoundError:
        return None

def render(ptri, delay):
    try:
        with open(ptri, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
       content = fallback 
    
    print("\n" * 100)   
    for line in content:
        print(line.rstrip())  # Strip trailing newline characters
        time.sleep(delay)

def main():
    filename = None
    delay = None
    Verbose = False
    if input("Would you like verbose messages? [Y/n]") == 'y' or 'Y':
        Verbose = True  
    if len(sys.argv) > 1:
        # Use command-line arguments only when started for the first time
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-f' and i+1 < len(sys.argv):
                filename = sys.argv[i+1]
            elif sys.argv[i] == '-t' and i+1 < len(sys.argv):
                delay = float(sys.argv[i+1])

    while True:
        if filename is None:
            if Verbose == True:
                print("No filename flag found, requesting spesification")
            filename = input("What is the name of your .ptri file (This must be in the same folder that I am in) For example, 'Testlist.ptri'\n(If I can't find the file, I will fallback to the python logo.): ")
        if delay == None:
            if Verbose == True:
                print("No delay flag found, requesting spesification")
            delay = (input("Enter the delay time (in seconds) between each line rendering: "))
            if delay == '':
                 delay = 0.05
            else:
                try:
                    delay = float(delay)
                except:
                    if Verbose == True:
                        print("There was an error converting the input into a float, defaulting to 0.05")
                    delay = 0.05
    
        # Calculate checksum for the .ptri file
        ptri_checksum = calculate_checksum(filename)
        if ptri_checksum is None and Verbose == True:
            print(f"Error: File '{filename}' not found or empty. Fallback to default content.")
            
        
        # Check if the total rendering time exceeds 10 seconds
        try:
            with open(filename, 'r') as file:
                content = file.readlines()
            total_lines = len(content)
        except FileNotFoundError:
            total_lines = 28  # Default number of lines for the fallback content
        total_time = total_lines * delay
        
        if total_time > 10:
            if Verbose == True:
                print(f"Error: The total rendering time ({total_time:.2f} seconds) exceeds 10 seconds. Defaulting to 0.05 per line.")
            delay = 0.05
            continue  # Restart the loop if total time exceeds 10 seconds
        
        render(filename, delay)
        timer = 3
        for _ in range(3):
            print(f"Press Ctrl+C to exit, Wait for {timer} seconds to restart", end='\r')  # Move the cursor to the beginning of the line
            time.sleep(1)
            timer -= 1

        print("\n" * 100)  # Clear the screen after the countdown finishes
        render(filename, 0)  # Render without delay after the countdown finishes
        filename = None  # Reset filename after first loop
        delay = None

if __name__ == '__main__':
    main()
