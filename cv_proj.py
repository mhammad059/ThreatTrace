from ultralytics import YOLO

model = YOLO(r"F:\Work\NUST\Semester 7\CV\Project\ultralytics-main\ultralytics-main\runs\detect\train\best.pt")
results = model.predict(source="0", show = True)

print(results)