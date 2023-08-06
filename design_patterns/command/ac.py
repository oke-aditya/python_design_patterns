class AirConditioner:
    _is_on: bool = False
    _temperature: int = 25
    
    def turn_off(self) -> None:
        self._is_on = False
        print(f"AC is turned off")
    
    def turn_on(self) -> None:
        self._is_on = True
        print(f"AC is turned on")
    

    def set_temperatue(self, temperature: int) -> None:
        self._temperature = temperature
        print(f"Temperatue of AC set to {temperature}")


