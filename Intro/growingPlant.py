'''
Each day a plant is growing by upSpeed meters.
Each night that plant's height decreases by downSpeed meters due to the lack of sun heat.
Initially, plant is 0 meters tall.
We plant the seed at the beginning of a day.
We want to know when the height of the plant will reach a certain level.
'''
def growingPlant(upSpeed, downSpeed, desiredHeight):
	d=0
	t=0
	while t<=desiredHeight:
		d+=1
		t=t+upSpeed
		if t>=desiredHeight:
			return d
			break
		t=t-downSpeed
	return d-1