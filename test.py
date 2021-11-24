import ssl
import cv2
import face_detection

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    detector = face_detection.build_detector("DSFDDetector", confidence_threshold=.5, nms_iou_threshold=.3, max_resolution=1080)
    im = cv2.imread("baby.jpg")[:, :, ::-1].copy()
    detections = detector.detect(im)
    print("***TEST SUCCESS***")
    print(detections[:3,:])
    print("...")

        
