import cv2, numpy, time

TARGET = cv2.CascadeClassifier("stopsign/cascade.xml")

def detect(filename) :
  jpegfile = open(filename).read()
  image = cv2.imdecode(numpy.fromstring(jpegfile, dtype=numpy.uint8),
                       cv2.CV_LOAD_IMAGE_GRAYSCALE)
  t = time.time()
  cascade = TARGET.detectMultiScale(
    image,
    scaleFactor=1.01,
    minNeighbors=2,
    minSize=(10, 10),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
  )
  print "od %f" % (time.time() - t)
  for (x,y,w,h) in cascade :
    print cascade
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)
    cv2.imshow("roboghini", image)
    cv2.waitKey(0)
    break

if __name__ == "__main__" :
  for filenum in range(20) :
    filename = "stopsign/stop%03d.jpeg" % filenum
    print filename
    detect(filename)
