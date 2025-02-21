import cv2
import mysql.connector
from pyzbar.pyzbar import decode

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="benny=2004",
    database="EventManager"
)
cursor = conn.cursor()

def mark_attendance(qr_data):
    registration_id, event = qr_data.split(",")

    # Check if the participant exists and is absent
    query = """SELECT name, attendance FROM Registrations WHERE id = %s AND event = %s"""
    cursor.execute(query, (registration_id, event))
    result = cursor.fetchone()

    if result:
        name, attendance = result
        if attendance == "Absent":
            # Mark as present
            update_query = """UPDATE Registrations SET attendance = 'Present' WHERE id = %s AND event = %s"""
            cursor.execute(update_query, (registration_id, event))
            conn.commit()
            print(f"✅ Attendance marked for {name} ({event})")
        else:
            print("⚠ Already marked as present.")
    else:
        print("❌ Invalid QR Code.")

# Open webcam for scanning
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    for barcode in decode(frame):
        qr_data = barcode.data.decode("utf-8").strip()
        mark_attendance(qr_data)
        cap.release()
        cv2.destroyAllWindows()
        exit()
    
    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Close database connection
cursor.close()
conn.close()
