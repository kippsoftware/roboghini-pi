# MOCK
IMAGE = open("stopsign/stop017.jpeg").read()

class PiCamera :
  def capture_continuous(self, stream, mime, use_video_port = True):
    stream.write(IMAGE)
    yield True
    
