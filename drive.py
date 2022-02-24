import car, cv2, threading, time, numpy

TARGET = cv2.CascadeClassifier("cascade.xml")

class Drive(threading.Thread) :
  """ Analyzes the camera image and decides where to go """
  def __init__(self, camera) :
    threading.Thread.__init__(self, name="Drive")
    self.camera = camera

  def loadImage(self) :
    image = numpy.fromstring(self.camera.sourceJPEG, dtype=numpy.uint8)
    return cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
  
  def serveImage(self, image) :
    try :
      self.camera.analyzedJPEG = cv2.imencode(".jpg", image)[1].tostring()
    except Exception as e:
      pass

  def observeWorld(self) :
    image = self.loadImage()
    self.boxes = TARGET.detectMultiScale(
      image,
      scaleFactor = 1.03,
      minNeighbors = 2,
      minSize = (10, 10),
      flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    for (x,y,w,h) in self.boxes :
      cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)
      break
    self.serveImage(image)

  def turnAround(self) :
    self.car.left()
    self.car.reverse(0.05, 0.04)
    time.sleep(2)
    self.car.stop()
    time.sleep(2)
    if False :
      self.car.straight()
      self.car.right()
      self.car.forward(0.05, 0.04)
      time.sleep(2)
      self.car.straight()
      self.car.stop()

  def shouldStop(self, targetWidth) :
    return targetWidth > 320 * 0.2
    
  def shouldGoLeft(self, midpoint) :
    return midpoint < 320 * 0.4

  def shouldGoRight(self, midpoint) :
    return midpoint > 320 * 0.6

  def drive(self) :
    self.car.straight()
    for (x,y,w,h) in self.boxes :
      midpoint = x + w / 2.0
      if self.shouldStop(w) :
        if self.car.drive :
          self.car.stop()
          self.turnAround()
      elif self.shouldGoRight(midpoint) :
        self.car.right()
      elif self.shouldGoLeft(midpoint) :
        self.car.left()      
      else :
        if not self.car.drive :
          self.car.forward(0.05, 0.20)
      break
    if len(self.boxes) == 0 :
      if not self.car.drive :
        self.car.forward(0.05, 0.20)

  def run(self) :
    time.sleep(2)
    self.car = car.Car()
    self.car.left()
    time.sleep(1)
    self.car.straight()
    self.car.right()
    time.sleep(1)
    self.car.straight()
    while True :
      self.observeWorld()
      self.drive()
