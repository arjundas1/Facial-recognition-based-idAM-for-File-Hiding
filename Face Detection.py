import cv2

haar_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')
lbp_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'lbpcascade_frontalface.xml')

def detect_faces(f_cascade, colored_img, scaleFactor=1.1):
    img_copy = colored_img
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);
    x=0
    y=0
    z=0
    w = 0
    if len(faces)==0:
        return img_copy,"None","None"
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img_copy,img_copy[y:y+w, x:x+h], faces[0]

def staticFaceDetectHaar(img):
    test1 = cv2.imread(img)
    test1 = detect_faces(haar_face_cascade,test1)
    cv2.imshow('finanl',test1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def staticFaceDetectLbp(img):
    test1 = cv2.imread(img)
    test1 = detect_faces(lbp_face_cascade,test1)
    cv2.imshow('finanl',test1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def liveFaceDetectLbp():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        frame = detect_faces(lbp_face_cascade,frame,1.1)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def liveFaceDetectHaar():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        frame = detect_faces(haar_face_cascade,frame,1.1)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
