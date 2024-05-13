class AirConditioning:
    """
    It is a class representing an air conditioning system.

    Attributes
    -----------
    - status: str, Current status of the air conditioning system ('True' if on, 'False' if off).
    - temperature: str, Current temperature set for the air conditioning system.

    Methods
    --------
    - switch_on(): Turns on the air conditioning system and sets the temperature to 18 degrees Celsius.
    - switch_off(): Turns off the air conditioning system and resets the temperature.
    - reset(): Resets the status and temperature of the air conditioning system.
    - raise_temperature(): Increases the temperature by 1 degree Celsius if the system is on, up to a maximum of 43 degrees Celsius.
    - lower_temperature(): Decreases the temperature by 1 degree Celsius if the system is on, down to a minimum of 0 degrees Celsius.
    - get_temperature(): Returns the current temperature set for the air conditioning system.
    - __str__(): Returns a string representation of the air conditioning system, indicating whether it is on or off and the current temperature setting.
    """
    _status = False
    _temperature = None

    @property
    def status(self):
        return f"{self._status}"

    @status.setter
    def status(self, value):
        self._status = self._status

    @property
    def temperature(self):
        return f'{self._temperature}'

    @temperature.setter
    def temperature(self, value):
        self._temperature = self._temperature

    def switch_on(self):
        """
        Turns on the air conditioning system and sets the temperature to 18 degrees Celsius.
        """
        self._status = True
        self._temperature = 18

    def switch_off(self):
        """
        Turns off the air conditioning system and resets the temperature.
        """
        self._status = False
        self._temperature = None

    def reset(self):
        """
        Resets the status and temperature of the air conditioning system.
        """
        self._status = False
        self._temperature = None

    def raise_temperature(self):
        """
        Increases the temperature by 1 degree Celsius if the system is on, up to a maximum of 43 degrees Celsius.
        """
        if self._status:
            self._temperature += 1
            if self._temperature > 43:
                self._temperature = 43
        return self._temperature
    def get_temperature(self):
        return self._temperature

    def __str__(self):
        """
        Returns a string representation of the air conditioning system, indicating whether it is on or off and the current temperature setting.
        """
        if self._status:
            return f'Кондиционер включен. Температурный режим: {self._temperature} градусов.' 
        return f'Кондиционер выключен.'

    def lower_temperature(self):
        """
        Decreases the temperature by 1 degree Celsius if the system is on, down to a minimum of 0 degrees Celsius.
        """
        if self._status:
            self._temperature -= 1
            if self._temperature < 0:
                self._temperature = 0
        return self._temperature


conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)
