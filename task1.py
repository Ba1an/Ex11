class AirConditioning:
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
        self._status = True
        self._temperature = 18

    def switch_off(self):
        self._status = False
        self._temperature = None

    def reset(self):
        self._status = False
        self._temperature = None

    def raise_temperature(self):
        if self._status:
            self._temperature += 1
            if self._temperature > 43:
                self._temperature = 43
        return self._temperature
    def get_temperature(self):
        return self._temperature

    def __str__(self):
        if self._status:
            return f'Кондиционер включен. Температурный режим: {self._temperature} градусов.' 
        return f'Кондиционер выключен.'

    def lower_temperature(self):
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
