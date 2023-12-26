import socket
from datetime import datetime

## Enter Host to scan
host = input("Enter a remote host to scan: ")
ip = socket.gethostbyname(host) # Translate a host name to IPv4 address format

#This is just a nice touch that prints out information on which host we are about to scan
print("-" * 80)
print("              Please wait, scanning the host --------> ", ip)
print("-" * 80)

## Check what time the scan started
t1 = datetime.now()

## Using the range function to specify ports (here it will scans all ports between 1 and 1024)
## We also put in some error handling for catching errors
try:
    for port in range(1,81):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it use for Creates a stream socket
        result = sock.connect_ex((ip, port))
        if result == 0:
            ## if a socket is listening it will print out the port number 
            print("\n Port %d Is Open!!!!!!!!!!!!!" %(port))
            sock.close()
        #else:
            #print("\n Port %d Is Close :( " %(port))
            
except:
    pass

## Checking the time again
t2 = datetime.now()
## Calculates the difference of time, to see how long it took to run the script
total = t2 - t1
## Printing the information to screen
print('Scanning Completed in: ', total)
