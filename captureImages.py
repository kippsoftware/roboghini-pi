import urllib2, time
from PIL import Image

HOST = "10.0.0.25"
PORT = 9000

def captureImages(folder, count, prefix) :
  for whichImage in range(count) :
    im = Image.open(urllib2.urlopen("http://%s:%s/camera" % (HOST, PORT)))
    im = im.convert(mode="L")
    filename = "%s/%s%03d.jpeg" % (folder, prefix, whichImage)
    im.save(filename)
    print filename + "\a"
    time.sleep(2)

captureImages("stopsign", 20, "stop")
