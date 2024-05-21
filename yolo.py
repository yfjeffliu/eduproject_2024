from ultralytics import YOLO

model = YOLO('yolov8n.pt')
from datetime import datetime

# while True:
#     results = model('tcp://127.0.0.1:8888', stream=True)
#     print(results)
#     for result in results:
#         boxes = result.boxes
#         probs = result.probs
print(datetime.now())
res = model.predict('uploads/test2.jpg', show=True)
print(datetime.now())

print(res)