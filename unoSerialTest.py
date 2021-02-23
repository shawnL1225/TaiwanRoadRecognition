#!/usr/bin/python3
import time
import serial
import threading

# serial_port = serial.Serial(
#     port="/dev/ttyTHS0",
#     baudrate=9600,
#     timeout=0.5
# )

# Wait a second to let the port initialize
time.sleep(1)

arduino_message = ""

def send():
    
        
        
    for i in text:
        serial_port.write(i.encode('utf-8'))
            time.sleep(0.1)

try:
    send()
    # while True:

        if serial_port.inWaiting() > 0:
            uno = serial_port.read()
            arduino_message +=  uno.decode('utf-8')
            if uno == "\n".encode():
                print(arduino_message)
                arduino_message = ""
        

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

# finally:
#     serial_port.close()
#     pass
