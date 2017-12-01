from gpiozero import PWMLED
from time import sleep
from signal import pause

led00 = PWMLED(2)
led01 = PWMLED(4)
led02 = PWMLED(15)
led03 = PWMLED(13)
led04 = PWMLED(21)
led05 = PWMLED(25)
led06 = PWMLED(8)
led07 = PWMLED(5)
led08 = PWMLED(10)
led09 = PWMLED(16)
led10 = PWMLED(17)
led11 = PWMLED(27)
led12 = PWMLED(26)
led13 = PWMLED(24)
led14 = PWMLED(9)
led15 = PWMLED(12)
led16 = PWMLED(6)
led17 = PWMLED(20)
led18 = PWMLED(19)
led19 = PWMLED(14)
led20 = PWMLED(18)
led21 = PWMLED(11)
led22 = PWMLED(7)
led23 = PWMLED(23)
led24 = PWMLED(22)

all_leds = []
all_leds.append(led00)
all_leds.append(led01)
all_leds.append(led02)
all_leds.append(led03)
all_leds.append(led04)
all_leds.append(led05)
all_leds.append(led06)
all_leds.append(led07)
all_leds.append(led08)
all_leds.append(led09)
all_leds.append(led10)
all_leds.append(led11)
all_leds.append(led12)
all_leds.append(led13)
all_leds.append(led14)
all_leds.append(led15)
all_leds.append(led16)
all_leds.append(led17)
all_leds.append(led18)
all_leds.append(led19)
all_leds.append(led20)
all_leds.append(led21)
all_leds.append(led22)
all_leds.append(led23)
all_leds.append(led24)

star_led = led00

top_leds = []
top_leds.append(led18)
top_leds.append(led11)
top_leds.append(led21)
top_leds.append(led09)
top_leds.append(led05)
top_leds.append(led10)

middle_leds = []
middle_leds.append(led03)
middle_leds.append(led12)
middle_leds.append(led07)
middle_leds.append(led06)
middle_leds.append(led20)
middle_leds.append(led01)
middle_leds.append(led14)

bottom_leds = []
bottom_leds.append(led02)
bottom_leds.append(led04)
bottom_leds.append(led08)
bottom_leds.append(led13)
bottom_leds.append(led15)
bottom_leds.append(led16)
bottom_leds.append(led17)
bottom_leds.append(led19)
bottom_leds.append(led22)
bottom_leds.append(led23)
bottom_leds.append(led24)

def allOff():
    for led in all_leds:
        led.off()

while True:
    allOff()

    star_led.pulse()
    sleep(0.2)

    for led in top_leds:
        led.pulse()
    sleep(0.5)

    for led in middle_leds:
        led.pulse()
    sleep(0.5)
    
    for led in bottom_leds:
        led.pulse()
    sleep(0.5)

    sleep(10)

    for led in all_leds:
        led.off()
        sleep(0.5)

    for led in all_leds:
        led.value = 0.5
        sleep(0.5)
    
    for led in all_leds:
        led.value = 1
        sleep(0.1)

    for led in all_leds:
        led.value = 0.5
        sleep(0.1)
    
    for led in all_leds:
        led.value = 1
        sleep(0.1)
