from testAT import Send_AT
import time
from gpiozero import CPUTemperature

while True:
    try:
        cpu = CPUTemperature()
        cpu_temp = f'{cpu.temperature:.2f}'
        group = '00'
        send_msg = f'GET /upload_data?group_name=group{group}&key=CPU_Temp&value={cpu_temp} HTTP/1.0'
        # print(send_msg)
        Send_AT('AT+CIPSTART="TCP","140.116.179.11","8087"')
        time.sleep(1)
        Send_AT(f'AT+CIPSEND={len(send_msg)}')
        time.sleep(1)
        Send_AT(send_msg)
        Send_AT('AT+CIPCLOSE')
        time.sleep(10)
    except KeyboardInterrupt:
        break
