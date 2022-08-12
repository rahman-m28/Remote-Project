class Television:
    MIN_CHANNEL = 0 # Minimum TV channel
    MAX_CHANNEL = 3 # Maximum TV channel
    MIN_VOLUME = 0 # Minimum TV volume
    MAX_VOLUME = 2 # Maximum TV volume
    def __init__(self):
        """
    - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
    - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
    - Create a private variable to store the TV __tv_status. The TV should start when it is off.
    """
        self.__default_channel=self.MIN_CHANNEL
        self.__default_volume=self.MIN_VOLUME
        self.__tv_status=False
        
    def power(self):
        """
    - This method should be used to turn the TV on/off.
    - If called on a TV object that is off, the TV object should be turned on.
    - If called on a TV object that is on, the TV object should be turned off.
    """
        if(self.__tv_status == False) :
            self.__tv_status = True
        else:
            self.__tv_status = False
        
        return self.__tv_status

    def channel_up(self):
        """
    - This method should be used to adjust the TV channel by incrementing its value.
    - It should only work for a TV that is on.
    - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
    """
        if (self.__tv_status):
            if (self.__default_channel + 1 < self.MAX_CHANNEL):
                self.__default_channel += 1
            else:
                self.__default_channel = self.MIN_CHANNEL

         return self.__default_channel

    def channel_down(self):
        """
    - This method should be used to adjust the TV channel by decrementing its value.
    - It should only work for a TV that is on.
    - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
    """
        if (self.__tv_status):
            if(self.__default_channel-1>=self.MIN_CHANNEL):
                self.__default_channel-=1

        return self.__default_channel

    def volume_up(self):
        """
    - This method should be used to adjust the TV volume by incrementing its value.
    - It should only work for a TV that is on.
    - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
    """
        if(self.__tv_status):
            if(self.__default_volume+1<=self.MAX_VOLUME):
                self.__default_volume+=1

        return self.__default_volume


    def volume_down(self):
        """
    - This method should be used to adjust the TV volume by decrementing its value.
    - It should only work for a TV that is on.
    - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
    """
        if (self.__tv_status):
            if (self.__default_channel - 1 >= self.MIN_CHANNEL):
                self.__default_channel -= 1
            else:
                self.__default_channel = self.MAX_CHANNEL - 1

        return self.__default_channel
    def get_volume(self):
        """
    - Returns the current value of the volume.    
    """
        return self.__default_volume

    def get_channel(self):
        """
    - Returns the current channel.    
    """
        return self.__default_channels

    def get_tv_status(self):
        """
    - Returns the current tv status.    
    """
        return self.__tv_status

    def __str__(self):
        """
    - This method should be used to return the TV __tv_status using the format shown in the comments of main.py
    """
        return f"TV __tv_status: Is on = {self.__tv_status}, Channel ={self.__default_channel}, Volume ={self.__default_volume}"
