class WeatherForecast:
    def __init__(self, status, temp):
        if status in ["sunny", "rainny", "cloudy", "snowy"]:
            self.__status = status
        else:
            raise ValueError(f'{status} must be "sunny", "rainny", "cloudy" or "snowy"')
        if temp<=40 and temp >= -40:
            self.__temp = temp
        else:
            raise ValueError('Temperature must be between -40 and 40')

    def __str__(self):
        return f"WeatherForecast {self.__status} {self.__temp}"
    
    @property
    def status(self):
        return self.__status
    
    @property
    def temp(self):
        return self.__temp
    
    @status.setter
    def status(self, status):
        if status in ["sunny", "rainny", "cloudy", "snowy"]:
            self.__status = status
        else:
            raise ValueError(f'{status} must be "sunny", "rainny", "cloudy" or "snowy"')
    
    @temp.setter
    def temp(self, temp):
        if temp<=40 and temp >= -40:
            self.__temp = temp
        else:
            raise ValueError('Temperature must be between -40 and 40')
        