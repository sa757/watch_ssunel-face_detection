import io, ssl, json, base64, logging
from PIL import Image

import cv2
import numpy as np
from flask import Blueprint, request, jsonify

import face_detection

ssl._create_default_https_context = ssl._create_unverified_context
route_app = Blueprint('route_app', __name__)

@route_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@route_app.route('/face_detection', methods=['POST'])
def infer_face():
    jsn = request.get_json()
    im_b64 = jsn['image']
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    img = Image.open(io.BytesIO(img_bytes))
    np_img = np.array(img)
    cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)

    detector = face_detection.build_detector(
      "DSFDDetector", confidence_threshold=.5, nms_iou_threshold=.3, max_resolution=1080)

    im = cv_img[:, :, ::-1].copy()
    detections = detector.detect(im)
    
    result = {}
    
    for i in range(len(detections)):
        xmin, ymin, xmax, ymax = detections[i][:4]
        conf = detections[i][4]
        result[i] = {'xmin':float(xmin),'ymin':float(ymin),'xmax':float(xmax),'ymax':float(ymax),'conf':float(conf)}
        # cv2.rectangle(im, pt1=(xmin,ymin), pt2=(xmax,ymax), color=(0,0,255), thickness=2)
    
    return jsonify({'output': result, "version": "test"})
    
