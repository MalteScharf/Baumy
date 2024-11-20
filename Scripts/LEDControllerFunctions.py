from pi5neo import Pi5Neo
import time

## config

neo = Pi5Neo('/dev/spidev0.0', 50, 800)

## Functions manipulate LEDs

def off(neo):
    neo.fill_strip(0, 0, 0)
    neo.update_strip()  # Commit changes to the LEDs

def onebyone(neo):
    for i in range(neo.num_leds):
        neo.set_led_color(i, 0, 255, 0)  # Green loading bar
        neo.update_strip()
        time.sleep(0.1)

