from TemperatureModule import TemperatureModule
def __init__(self, path):
    self.temperatureModule = TemperatureModule()
    print(self.temperatureModule.getTemperature1())
    print(self.temperatureModule.getTemperature2())
    print(self.temperatureModule.getTemperature3())
    
