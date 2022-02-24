# roboghini-pi
self-driving car prototype using OpenCV

# The Robo-ghini Pi: DIY Computer Vision for a Self-driving Car

Automobiles that drive themselves are now cruising our roadways. It
isn't magic! Combining a 1/24 scale Lamborghini, a Raspberry Pi
computer, a digital camera, and integrating "Computer Vision" open
source software, Kipp will show off a DIY concept car that actually
drives itself.

# Train the Vision System

captureImages.py - read capture server and save images for cascade analysis

createSamples.sh - read positive and negative images; write .vec file

traincascade.sh - read .vec file; read negative images; create cascade.xml

# Drive the Roboghini Pi

car.py - wrap the gpio with pulse width modulation; implement the drive forward, reverse, left, right

camera.py - wrap the picamera with a thread

drive.py - read camera, run the cascade, drive the car

roboghini.py - run a cherrypy server to share the car camera

