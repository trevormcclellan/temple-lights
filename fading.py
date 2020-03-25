STEPS     = 1

import pigpio

pi = pigpio.pi()

def updateColor(color, step):
	color += step
	
	if color > 255:
		return 255
	if color < 0:
		return 0
		
	return color
    
def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)

def fadeIn(pin, currVar):
    while currVar < 255:
        currVar = updateColor(currVar, STEPS)
        setLights(pin, currVar)
    if currVar == 255:
        setLights(pin, 255)
        
def fadeOut(pin, currVar):
    while currVar != 0:
        currVar = updateColor(currVar, -STEPS)
        setLights(pin, currVar)
    if currVar == 0:
        setLights(pin, 0)    