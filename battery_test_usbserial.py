import serial
#usbport = '/dev/ttyAMA0'
usbport = '/dev/tty.usbmodem12341'
ser = serial.Serial(usbport, 9600, timeout=1)

import time
count = time.time()
t = time.localtime()
temp = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + " - " + str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec)


while True:
    s='\x00\xF0' + '\xAA\x00\x01' + '\x0F' + '\xF0' + "\xAB\x00\x02" + '\x0F'
#    s='S'
#    ser.write(s)
#    s='\xAA\x00\x01' 
#    ser.write(s)
#    s='S'
    ser.write(s)
#    ser.write(" S 0xAA 0x00 0x01 S\n S 0xAB 0x00 2 S\n")
    response=ser.read()
    time.sleep=1
    result=ser.read(ser.inWaiting())
    print result
    time.sleep=100
           
ser.close()
