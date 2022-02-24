import threading, picamera, time, io

class Camera(threading.Thread) :
  """ Wraps the camera with a thread """
  def __init__(self) :
    threading.Thread.__init__(self, name="Camera")
    self.sourceJPEG = ""
    self.analyzedJPEG = ""
    self.keepRunning = True
  def run(self) :
    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.resolution = (320, 240)
    camera.framerate = 10
    while True :
      time.sleep(2)
      stream = io.BytesIO()
      try :
        for x in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
          stream.seek(0)
          self.sourceJPEG = stream.read()
          if not self.keepRunning :
            break
          stream.seek(0)
          stream.truncate()
      except Exception as e:
        print e
