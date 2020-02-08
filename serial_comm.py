import serial
import time
 
ArduinoSerial = serial.Serial('com18',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established
while 1:

    var = raw_input() #get input from user
    print "you entered", var #print the intput for confirmation
    
    if (var == '1'): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)
