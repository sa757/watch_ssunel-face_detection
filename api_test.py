import json, requests, base64

if __name__ == "__main__":


    url    = "http://0.0.0.0:5050/face_detection"
    header = {"Content-Type": "application/json; charset=UTF-8"}
    
    image_file = './baby.jpg'
    
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    payload = json.dumps({"image": im_b64})
    
    response = requests.post(url, data=payload, headers=header)
    response.close()

    if response.ok==True:
        print(json.loads(response.text))
    else:
        raise ValueError(f"Failed...{response.text}")

# import glob
# import os
# import cv2
# import time
# import face_detection
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# def draw_faces(im, bboxes):
#     for bbox in bboxes:
#         x0, y0, x1, y1 = [int(_) for _ in bbox]
#         cv2.rectangle(im, (x0, y0), (x1, y1), (0, 0, 255), 2)


# if __name__ == "__main__":
#     impaths = "images"
#     impaths = glob.glob(os.path.join(impaths, "*.jpg"))
#     detector = face_detection.build_detector(
#         "DSFDDetector",
#         max_resolution=1080
#     )
#     for impath in impaths:
#         if impath.endswith("out.jpg"): continue
#         im = cv2.imread(impath)
#         print("Processing:", impath)
#         t = time.time()
#         dets = detector.detect(
#             im[:, :, ::-1]
#         )[:, :4]
#         print(f"Detection time: {time.time()- t:.3f}")
#         draw_faces(im, dets)
#         imname = os.path.basename(impath).split(".")[0]
#         output_path = os.path.join(
#             os.path.dirname(impath),
#             f"{imname}_out.jpg"
#         )

#         cv2.imwrite(output_path, im)
        
