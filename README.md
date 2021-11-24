# watch_ssunel-face_detection
- 쑤넬이 CCTV 모니터링 도커이미지1 - 얼굴인식기API
- 쑤넬이 이미지를 캡쳐한후 (1) 얼굴인식기API에게 보낸다.
- 얼굴 인식이 완료된 후 감정인식 -> 감정 분류를 진행한다.

### run api and test
```cli
docker build -t <imagename> .
docker run -it --gpus all -p <hostport>:<containerport(5050)> <imagename> /bin/bash
```

- run test inside of container

```cli
sh run.sh 5050 # run api
(ctl+p+q) docker exec -it <container id> /bin/bash
python api_test.py
```


### reference
- https://github.com/hukkelas/DSFD-Pytorch-Inference
