from testAT import Send_AT
import time
from gpiozero import CPUTemperature

while True:
    try:
        cpu = CPUTemperature()        # 取得溫度
        cpu_temp = f'{cpu.temperature:.2f}'  # 將溫度的小數位數取固定長度
        group = '00'
        send_msg = f'GET /upload_data?group_name=group{group}&key=CPU_Temp&value={cpu_temp} HTTP/1.0' #整合資料傳送的訊息
        Send_AT('AT+CIPSTART="TCP","140.116.179.11","8087"')    # 連結TCP
        time.sleep(1)        # 等待連接用的延遲
        Send_AT(f'AT+CIPSEND={len(send_msg)}')    # 開始傳送資料，設定訊息長度作為資料長度
        time.sleep(1)        # 等待用的延遲
        Send_AT(send_msg)    # 傳送資料
        Send_AT('AT+CIPCLOSE')    # 關閉連線
        time.sleep(10)    # 每10秒循環
    except KeyboardInterrupt:    # 按下Ctrl+C 結束程式
        break
