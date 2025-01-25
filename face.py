import cv2
import webbrowser
import time

# Load the known face image and convert it to grayscale
known_face_image = cv2.imread("C:\python vscode\WIN_20240916_10_59_27_Pro.jpg")
known_face_gray = cv2.cvtColor(known_face_image, cv2.COLOR_RGB2GRAY)

# Initialize the face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Set up video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# Define target URL
target_url = "https://web.whatsapp.com"

# Main loop
browser_opened = False
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_region = gray_frame[y:y+h, x:x+w]

        # Resize the known face and the detected face region to the same size
        resized_known_face = cv2.resize(known_face_gray, (w, h))
        result = cv2.matchTemplate(face_region, resized_known_face, cv2.TM_CCOEFF_NORMED)

        # Determine if the detected face matches the known face
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        threshold = 0.6  # Adjust this threshold for better accuracy
        name = "unknown"
        
        if max_val > threshold:
            name = "anmol"

            # Draw a rectangle and label around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Open the web browser if not already opened
            if not browser_opened:
                webbrowser.open_new_tab(target_url)
                browser_opened = True
                time.sleep(7)  # Delay to avoid multiple openings

        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the video frame with annotations
    cv2.imshow("video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
