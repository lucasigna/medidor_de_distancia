import utime
from machine import Pin

class LCD1602:

    def pulseE(self):
        self.e.value(1)
        utime.sleep_us(40)
        self.e.value(0)
        utime.sleep_us(40)
    def send2LCD4(self,BinNum):
        self.d4.value((BinNum & 0b00000001) >>0)
        self.d5.value((BinNum & 0b00000010) >>1)
        self.d6.value((BinNum & 0b00000100) >>2)
        self.d7.value((BinNum & 0b00001000) >>3)
        self.pulseE()
    def send2LCD8(self,BinNum):
        self.d4.value((BinNum & 0b00010000) >>4)
        self.d5.value((BinNum & 0b00100000) >>5)
        self.d6.value((BinNum & 0b01000000) >>6)
        self.d7.value((BinNum & 0b10000000) >>7)
        self.pulseE()
        self.d4.value((BinNum & 0b00000001) >> 0)
        self.d5.value((BinNum & 0b00000010) >> 1)
        self.d6.value((BinNum & 0b00000100) >> 2)
        self.d7.value((BinNum & 0b00001000) >> 3)
        self.pulseE()
    def init(self):
        self.rs.value(0)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0010)
        self.send2LCD8(0b00101000)
        self.send2LCD8(0b00001100) # lcd on, blink off, cursor off.
        self.send2LCD8(0b00000110) # increment cursor, no display shift
        self.send2LCD8(0b00000001) # clear screen
        utime.sleep_ms(2) # clear screen needs a long delay
        
    def write(self,string,row):
        code = 0
        if row == 1:
            code = 0x80
        if row == 2:
            code = 0xC0
        self.send2LCD8(code)
        self.rs.value(1)
        for x in string:
            self.send2LCD8(ord(x))
            utime.sleep_ms(1)
        self.rs.value(0)
            
    def clear(self):
        self.init()
            
    def __init__(self,rs,e,d4,d5,d6,d7):
        self.rs = Pin(rs, Pin.OUT)
        self.e = Pin(e, Pin.OUT)
        self.d4 = Pin(d4, Pin.OUT)
        self.d5 = Pin(d5, Pin.OUT)
        self.d6 = Pin(d6, Pin.OUT)
        self.d7 = Pin(d7, Pin.OUT)
