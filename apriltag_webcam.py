import cv2
from apriltag import Detector

#baixar pip install apriltag

def main():
    
    detector = Detector()

    width = 640
    height = 480

    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        
        ret, frame = cap.read()

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        detections = detector.detect(gray)

        
        for detection in detections:
            
            rect = detection.corners.astype(int)
            
            cv2.polylines(frame, [rect], True, (0, 0, 255), 2)

            
            tag_id = detection.tag_id
            
            cv2.putText(frame, f"ID: {tag_id}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        
        cv2.imshow('Camera', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
