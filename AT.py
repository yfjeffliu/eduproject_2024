import time
import serial
ser = serial.Serial("/dev/ttyS0",115200)  #SIM7000C USB port
def receiving(timeout=0.25):    #簡單做法, 基礎用0.25秒計時, 否則自行定義
    #ser.flushInput()           #清除接收緩衝區
    last_received=''
    try:
        while timeout>0:
            time.sleep(0.2)
            count = ser.inWaiting() #取得當下緩衝區字元數
            while count != 0:
                last_received += ser.read(count).decode('utf-8')    #getData += bytes.decode(ch)
                time.sleep(0.2)    #
                count = ser.inWaiting() #取得當下緩衝區字元數
            timeout = timeout-0.25
        return last_received.strip()

    except IOError as ex:
        raise RuntimeError('Failed to serial port') from ex
    except Exception as ex:
        raise ex
def Send_AT(cmd, timeout=0.25, ret='OK'):
    ser.write((cmd+'\r\n').encode('utf-8')) 
    #print(receiving(timeout=timeout))
    data = receiving(timeout=timeout)
    print(data)
    if ret in data:
        return ret
    else:
        return 'ERROR'
while True:
    try:
        command = input()
        if command =='q':
            break
        Send_AT(command)
    except KeyboardInterrupt:
        break
