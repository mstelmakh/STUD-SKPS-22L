import gpio4
import time
import sys

class GPIOwrap(gpio4.SysfsGPIO):
    def __init__(self, pin, direction):
        super().__init__(pin)
        self.export = True
        self.direction = direction

    def __del__(self):
        self.export = False

pin = 21
freq = 50
if __name__ == "__main__": 
	pin21 = GPIOwrap(pin, "out")
	start = time.perf_counter()
	while time.perf_counter() - start < 100:
		time.sleep(1/freq * 0.075)
		pin21.value = 0
		time.sleep(1/freq * 0.925)
		pin21.value = 1
