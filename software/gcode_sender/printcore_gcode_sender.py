# install printcore and install pyserial

from printrun.printcore import printcore
from printrun import gcoder
import time
import serial.tools.list_ports

def send_gcode(iter, gcode_file): 

  port = '/dev/ttyACM0' # Default port

  # Auto Connect to Prusa
  for device in serial.tools.list_ports.comports(): 
    if 'Prusa' in device.description: 
      port = device.device

  p = printcore(port , 115200) #  Instance of Printcore
  gcode = [i.strip() for i in open(gcode_file)] # Process Gcode read from file
  gcode = gcoder.LightGCode(gcode) # Process Gcode

  # Startprint silently exits if not connected yet, this is important to initiate print
  while not p.online:
    time.sleep(0.1)

  p.startprint(gcode) # Start the print

  # Print Progress if printing, otherwise disconnect
  last_val = 0
  print('Printing...')
  while p.printing:
    # Display progress
    current = round(100 * float(p.queueindex) / len(p.mainqueue))

    if last_val is not current:
      # print('Progress: {}'.format(current))

      last_val = current
    
  else:
    print('Print {} Complete'.format(iter))
    p.disconnect()
      
# List all com connected devices
# for device in serial.tools.list_ports.comports(): 
#   print(device.description)

#If you need to interact with the printer:
# p.send_now("M105") # this will send M105 immediately, ahead of the rest of the print
# p.pause() # use these to pause/resume the current print
# p.resume()
# p.disconnect() # this is how you disconnect from the printer once you are done. This will also stop running prints.