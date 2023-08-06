class AirConditioner:
    _is_on: bool = False
    _temperature: int = 25
    
    def turn_off(self):
        self._is_on = False
        print(f"AC is turned off")
    
    def turn_on(self):
        self._is_on = True
        print(f"AC is turned on")
    

    def set_temperatue(self, temperature: int):
        self._temperature = temperature
        print(f"Temperatue of AC set to {temperature}")


