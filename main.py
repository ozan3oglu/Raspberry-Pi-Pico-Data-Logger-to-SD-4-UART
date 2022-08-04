from machine import UART,SPI, Pin
import sdcard, uos
import time
import utime
import machine
import os

rtc=machine.RTC()


COLORS = {\
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
}

uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1),rxbuf=8192)
uart1 = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9),rxbuf=8192)
uart2 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5),rxbuf=8192)
uart3 = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17),rxbuf=8192)

ledpow=Pin(6,Pin.OUT)

spi = SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
print(COLORS["green"]+"[LOG SD] SD CARD AVAILABLE : "+str(sd)+"\n",'\033[m')

rxData = bytes()
rxData1= bytes()
rxData2 = bytes()
rxData3 = bytes()

uos.mount(sd, '/sd')
list= os.listdir('/sd')
print(COLORS["green"]+"[LOG SD] LIST OF FOLDERS : "+str(list)+"\n",'\033[m')
number_files = len(list)-1
print(COLORS["green"] +"[LOG SD] SD FOLDER NUMBER : " + str(number_files) +"\n",'\033[m')


folderstop=0
foldnum=1

while (folderstop == 0) :
    foldname="Folder_" + str(foldnum)
    if not str(foldname) in str(uos.listdir('/sd')):
        path = "/sd/"+str(foldname)
        path=f'{path}'
        os.mkdir(path)
        filename= path + "/UART0.txt"
        filename=f'{filename}'
        filename1= path + "/UART1.txt"
        filename1=f'{filename1}'
        filename2= path + "/UART2.txt"
        filename2=f'{filename2}'
        filename3= path + "/UART3.txt"
        filename3=f'{filename3}'
        print(COLORS["yellow"]+"[LOG SD] : Folder created as : "+str(foldname)+"\n",'\033[m')
        folderstop=1
    foldnum +=1
  
    


while True:
    timestamp=rtc.datetime()
    timestring="%02d.%02d.%02d"%(timestamp[4],timestamp[5],timestamp[6])
    
    if uart0.any() > 0:
        print(COLORS["yellow"] + str(uart0.any()),'\033[m' +"\n")
        rxData += uart0.read()
        print(COLORS["yellow"]+"[LOG SD] UART_O read data : ",'\033[m' +"\n")
        #print(COLORS["yellow"] + str(rxData),'\033[m' +"\n")
        print(rxData.decode('utf-8','ignore'))
        #time.sleep_ms(100)
        with open(filename, "a") as file:
                file.write(rxData.decode('utf-8','ignore'))
                file.write("\r\n")
                #time.sleep_ms(100)
                file.flush()
                file.close()
        ledpow.toggle()
        if len(rxData)>1000:
            rxData=bytes()
        
        if uart0.any() < 0 :
            break
            
    if uart1.any() > 0:
        print(COLORS["green"] + str(uart1.any()),'\033[m' +"\n")
        rxData1 += uart1.read()
        print(COLORS["green"]+"[LOG SD] UART_1 read data : ",'\033[m' +"\n")
        #print(rxData1.decode('utf-8','ignore'))
        print(COLORS["green"]+rxData1.decode('utf-8','ignore'),'\033[m' +"\n")
        #time.sleep_ms(100)
        with open(filename1, "a") as file1:
                file1.write(rxData1.decode('utf-8','ignore'))
                file1.write("\r\n")
                #time.sleep_ms(100)
                file1.flush()
                file1.close()
        ledpow.toggle()
        if len(rxData1)>1000:
            rxData1=bytes()
        if uart1.any() < 0 :
            break
    
#     while uart2.any() > 0:
#         #print(COLORS["green"] + str(uart2.any()),'\033[m' +"\n")
#         rxData2 += uart2.read()
#         print(COLORS["yellow"]+"[LOG SD] UART_2 read data : ",'\033[m' +"\n")
#         print(rxData2.decode('utf-8','ignore'))
#         
#         with open(filename2, "a") as file:
#                 file.write(rxData2.decode('utf-8','ignore'))
#                 file.write("\r\n")
#                 file.flush()
#                 file.close()
#         if len(rxData2)>3000:
#             rxData2=bytes()
#         
#     while uart3.any() > 0:
#         #print(COLORS["green"] + str(uart3.any()),'\033[m' +"\n")
#         rxData3 += uart3.read()
#         print(COLORS["yellow"]+"[LOG SD] UART_3 read data : ",'\033[m' +"\n")
#         print(rxData3.decode('utf-8','ignore'))
#         
#         with open(filename3, "a") as file:
#                 file.write(rxData3.decode('utf-8','ignore'))
#                 file.write("\r\n")
#                 file.flush()
#                 file.close()
#         if len(rxData3)>3000:
#             rxData3=bytes()

    
