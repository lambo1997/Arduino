import serial
from expresslink import ExpressLink
import busio
from digitalio import DigitalInOut, Direction, Pull
import board


uart = busio.UART(tx=None, rx=None, baudrate=115200, timeout=30)
el = ExpressLink(uart, DigitalInOut(board.G5), DigitalInOut(board.G2), DigitalInOut(board.G6) )
el.begin()
print("ExpressLink Started")

if el.connect():
    serialPort = serial.Serial(port = "COM3", baudrate=115200,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    serialString = ""

    while(1):
        if(serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            print(serialString.decode('utf-8'))
            # Tell the device connected over the serial port that we recevied the data!
            # The b at the beginning is used to indicate bytes!
            serialPort.write(b"Thank you for sending data \r\n")

