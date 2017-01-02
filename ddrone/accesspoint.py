class AccessPoint:
    
    def __init__(self, s, m=None, c=None):
        
        self.ssid = s
        self.mac = m
        self.channel = c
        
    def __str__(self):
        
        return '<SSID: ' + str(self.ssid) + ', MAC: ' + str(self.mac) + ', CHANNEL: ' + str(self.channel) + '>'
        