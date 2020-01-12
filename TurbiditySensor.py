#turbidity sensor data
import time.sleep

while True
  
  totalVolatgeReading = 0
  for count in range(800):
    currentVolatgeReading = float(anlogRead(rpiGpioSensorPinNum / 1023)*5)
    totalVoltageReading = totalVoltageReading + currentVoltageReading
    
   averageVoltageReading = totalVoltageReading/800
   
   roundedUpAverageVoltageReading = round(averageVoltageReading)
   
   if roundedUpAverageVoltageReading < 2.5:
     nephelometricTurbidityUnit = -(1120.4* square(roundAverageVoltageReading) + (5742.3* roundUpAverageVoltageReading - 4353.8)
     
   lcd.clear()
   lcd.setCursor(0,0)
   lcd.print(roundedUpAverageVoltageReadig, "V")
   
   lcd.setCursor(0,1)
   lcd.print(nephelometricTurbidityUnit, "NTU")
   
   sleep(10)
