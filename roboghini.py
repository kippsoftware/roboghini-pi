import cherrypy
from camera import Camera
from drive import Drive

camera = Camera()
camera.start()

drive = Drive(camera)
drive.start()

class CameraServer :
  @cherrypy.expose
  def index(self) :
    return file("index.html").read()
  @cherrypy.expose
  def camera(self, t=""):
    cherrypy.response.headers['Content-Type'] = "image/jpeg"
    return camera.sourceJPEG
  @cherrypy.expose
  def detect(self, t=""):
    cherrypy.response.headers['Content-Type'] = "image/jpeg"
    return camera.analyzedJPEG

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 9000
cherrypy.quickstart(CameraServer())
