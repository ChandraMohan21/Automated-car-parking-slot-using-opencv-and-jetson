import cv2

camera = cv2.VideoCapture(2)

print("[INFO] Initializing camera.")

cv2.namedWindow("Camera")

while True: 
    ret, frame = camera.read()
    
    if not ret:
        print("[ERROR] Failed to initialize camera.")
        break
    
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1)
    
    if key == 27:  # ESC key
        print("[INFO] Camera terminated.")
        break
    elif key == 32:  # SPACE key
        img_name = "parking_lot.png"
        print("[INFO] Saving '{}' ...".format(img_name))
        cv2.imwrite(img_name, frame)
        print("[INFO] '{}' saved successfully!".format(img_name))
        break  # Exit the loop after capturing and saving one frame

# Release the camera and close the window outside the loop
camera.release()
cv2.destroyAllWindows()
