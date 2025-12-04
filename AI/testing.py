from ultralytics import YOLO
import cv2
import os

# --- הגדרות ---
MODEL_PATH = "C:/Users/arial/LinkedInAssistant/runs/detect/train3/weights/best.pt"
INPUT_IMAGE = "AI\\testing.png"
OUTPUT_DIR = "cropped_posts"

# --- יצירת תיקייה אם לא קיימת ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- טעינת המודל ---
model = YOLO(MODEL_PATH)

# --- קריאת התמונה ---
img = cv2.imread(INPUT_IMAGE)
h, w, _ = img.shape

# --- הרצת זיהוי ---
results = model(img)[0]

counter = 1

# --- מעבר על כל האובייקטים ---
for box in results.boxes:
    conf = float(box.conf[0])
    cls = int(box.cls[0])

    # המידות בפיקסלים מוחלטים
    x1, y1, x2, y2 = box.xyxy[0].tolist()

    # המרת ערכים ל-int
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

    # יצירת crop
    crop = img[y1:y2, x1:x2]

    # שם הקובץ
    out_path = os.path.join(OUTPUT_DIR, f"post_{counter}.jpg")

    # שמירה
    cv2.imwrite(out_path, crop)
    print(f"[+] Saved: {out_path}  (conf={conf:.2f})")

    counter += 1

print("\nAll posts cropped successfully!")
