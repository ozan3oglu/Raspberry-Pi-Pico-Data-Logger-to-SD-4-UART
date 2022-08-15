# Raspberry-Pi-Pico-Data-Logger-to-SD-2-Uart-
By using two serial connections using Raspberry Pi Pico, it allows to view two log files separately on the terminal and to open a new file in the micro sd card every time the device is powered on and write the two serial data to two different text files. In addition, this process can be performed without using a computer, by using an external power supply. In this method, when the device starts to get power, it starts to do its job.
Since there is no RTC Clock in Raspberry pi, real-time accurate time and date writing cannot be performed, but this process works as it should when a computer connection is established. The code directory to be added is also shown below;

* rtc=machine.RTC()
* timestamp=rtc.datetime()
* datestring="%02d_%02d_%04d"%(timestamp[2],timestamp[1],timestamp[0])
* timestring="%02d.%02d.%02d"%(timestamp[4],timestamp[5],timestamp[6])

With the help of a led, we can control that the data flow is provided and written into the sd card when external power is used. In addition, 4 UART channels are also on. The desired channels can be opened by removing the comment lines in the code.

PCB view


![PCB_2D](https://user-images.githubusercontent.com/110588407/184586287-c513dcb0-42ca-4e31-ac8f-c0b8cbe59f72.png)

