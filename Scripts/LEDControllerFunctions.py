from pi5neo import Pi5Neo
import time

## Functions manipulate LEDs

class LEDFunctions(): 
    
    def __init__(self):
        self.neo = Pi5Neo('/dev/spidev0.0', 50, 800)

    def off(self):
        self.neo.fill_strip(0, 0, 0)
        self.neo.update_strip()  # Commit changes to the LEDs

    def onebyone(self, duration):
        for i in range(self.neo.num_leds):
            self.neo.set_led_color(i, 255, 255, 255)  
            self.neo.update_strip()
            time.sleep(duration)
            self.neo.fill_strip(0, 0, 0)
            self.neo.update_strip()

            #self.neo.clear_strip()
    
    def lightone(self, i,r,g,b):
        self.neo.set_led_color(i, r, g, b)  
        self.neo.update_strip()

led = LEDFunctions()
led.off()
#led.onebyone(0.5)
# led.lightone(4, 255,255,255)

