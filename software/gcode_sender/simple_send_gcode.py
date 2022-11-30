# Send gcode using UART pins using serial
# https://onehossshay.wordpress.com/2011/08/26/grbl-a-simple-python-interface/

import serial
import time

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]

# Open serial port
s = serial.Serial("/dev/ttyUSB0",115200)
print('Opening Serial Port')
 
# Open g-code file
f = open('gcode.gcode','r')
print('Opening gcode file')
 
# Wake up 
s.write("\r\n\r\n") # Hit enter a few times to wake the Printrbot
time.sleep(2)   # Wait for initialize
s.reset_input_buffer()  # Flush startup text in serial input
print('Sending gcode')
 
# Stream g-code
for line in f:
	l = removeComment(line)
	l = l.strip() # Strip all EOL characters for streaming
	if l.isspace()==False and len(l)>0:
		print('Sending: ' + l)
		s.write(l + '\n') # Send g-code block
		grbl_out = s.readline() # Wait for response with carriage return
		print(' : ' + grbl_out.strip())
 
# Wait here until printing is finished to close serial port and file.
input("Press <Enter> to exit.")
 
# Close file and serial port
f.close()
s.close()