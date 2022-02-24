import time, threading
from gpiozero import OutputDevice

class Pulse(threading.Thread) :
  """ Wraps the output device with a pulse width modulator """
  def __init__(self, pin1, pin2, onSeconds, offSeconds) :
    threading.Thread.__init__(self)
    self.pin1 = pin1
    self.pin2 = pin2
    self.onSeconds = onSeconds
    self.offSeconds = offSeconds
  def run(self) :
    self.keepGoing = True
    while self.keepGoing :
      one = OutputDevice(self.pin1, initial_value=True)
      two = OutputDevice(self.pin2, initial_value=True)
      time.sleep(self.onSeconds)
      del one
      del two
      time.sleep(self.offSeconds)
      
class Car :
  """ Implements the drive control of the car """
  def __init__(self) :
    self.drive = None
  def left(self) :
    self.green = OutputDevice(6, initial_value=True)
    self.yellow = OutputDevice(13, initial_value=True)
  def right(self) :
    self.green = OutputDevice(14, initial_value=True)
    self.yellow = OutputDevice(15, initial_value=True)
  def straight(self) :
    self.green = None
    self.yellow = None
  def forward(self, onSeconds, offSeconds) :
    self.drive = Pulse(20, 21, onSeconds, offSeconds)
    self.drive.start()
  def stop(self) :
    self.drive.keepGoing = False
    self.drive = None
  def reverse(self, onSeconds, offSeconds) :
    self.drive = Pulse(19, 26, onSeconds, offSeconds)
    self.drive.start()
