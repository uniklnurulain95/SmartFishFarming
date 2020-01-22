    def reading(sensor):
        import time
        import RPi.GPIO as GPIO
    
        GPIO.setwarnings(False)
    
        GPIO.setmode(GPIO.BCM)
    
    if sensor == 0:
              
        GPIO.setup(5,GPIO.OUT)
        GPIO.setup(6,GPIO.IN)
        GPIO.output(5, GPIO.LOW)
                
        time.sleep(0.3)
                
        GPIO.output(5, True)
               
        time.sleep(0.00001)
        
        return tankPercentFull
        
        GPIO.cleanup()

    else:
        print "Incorrect usonic() function varible."


    if __name__ == "__main__": 
	      import time	
	      file = open("/home/pi/wellsensor/hourlyTankRecord", "a")
	      file.write("%s | %6.2f" % (str(time.ctime()), reading(0)))
	      file.write("\n")
	      file.close()
