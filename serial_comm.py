import serial
import time
 
<<<<<<< HEAD
ArduinoSerial = serial.Serial('/dev/tty',9600) #Create Serial port object called arduinoSerialData

time.sleep(2) #wait for 2 secounds for the communication to get established
print(ArduinoSerial)

# while 1:

#     var = raw_input() #get input from user
#     print("you entered", var) #print the intput for confirmation
    
#     if (var == '1'): #if the value is 1
#         ArduinoSerial.write('1') #send 1
#         print ("LED turned ON")
#         time.sleep(1)
    
#     if (var == '0'): #if the value is 0
#         ArduinoSerial.write('0') #send 0
#         print ("LED turned OFF")
#         time.sleep(1)
=======
ArduinoSerial = serial.Serial('com12',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established
print (ArduinoSerial)
while 1:
    var = int(input()) #get input from user
    print ("you entered", var) #print the intput for confirmation
    
    if (var == 1): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == 0): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)
>>>>>>> 557f07e20e5d90b2881bf5f0b91c0d2f81e72066

# from time import sleep
# import serial
# ser = serial.Serial('COM11', 9600) # Establish the connection on a specific port
# while True:
#     ser.write('1') # Convert the decimal number to ASCII then send it to the Arduino
#     sleep(1)
#     ser.write('0') # Convert the decimal number to ASCII then send it to the Arduino
#     sleep(1)
