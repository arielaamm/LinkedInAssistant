from ultralytics import YOLO

model = YOLO("yolov8s.pt")

# התחל אימון
model.train(data="data\\dataset\\post_dataset.yaml", epochs=100, imgsz=640)

results = model.val()  # בדיקה על סט הוולידציה
model.export(format="onnx")  # אפשר גם לשמור בפורמטים אחרים