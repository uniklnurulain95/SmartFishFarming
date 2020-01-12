#ADC Coding 
#!/usr/bin/phython
#-*- coding :utf-8 -*-
import smbus
import time

address =0x48
A0 = 0X40
A1 = 0X41
A2 = 0X42
A3 = 0X43
bus = smbus.SMBus(1)
while True:
  bus.write_byte(address,A0)
  value = bus.read_byte(address)
  print("AOUT:%1.3f "%(value*3.3/255))
  time.sleep(0.1)
  
#save file as "pcf8591.py" and execute it with: sudo python pcf8591.py  
