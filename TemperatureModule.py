import subprocess

Temperature1Path = "w1_bus_master3"
Temperature2Path = "w1_bus_master1"
Temperature3Path = "w1_bus_master5"

class TemperatureModule:
    
    def execute(self, sensor):
        try:
            get_id = ["ls", "/sys/bus/w1/devices/{}/".format(sensor)]
            sensor_id = subprocess.check_output(get_id).decode("utf-8").split("\n")[0]
            get_reading = ["cat", "/sys/bus/w1/devices/{}/{}/w1_slave".format(sensor, sensor_id)]
            reading = subprocess.check_output(get_reading).decode("utf-8").split("t=")[1]
            reading = reading.replace("\n", "").replace("\r", "")
            return (float(reading)/1000)
        except:
            return "NaN"
        
    def getTemperature1(self):
        return self.execute(Temperature1Path)

    
    def getTemperature2(self):
        return self.execute(Temperature2Path)

    def getTemperature3(self):
        return self.execute(Temperature3Path)
            