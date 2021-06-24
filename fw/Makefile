
HEXFILE ?= blinkHelloWorld.hex

AVRDUDE_FLAGS := -v
AVRDUDE_FLAGS += -p m32u4

# Programmer "avr109" is Caterina bootloader.
# NOTE: Serial port may change.
AVRDUDE_FLAGS += -c avr109 
AVRDUDE_FLAGS += -P $(shell ls /dev/ttyACM* | sort | head -n1)

AVRDUDE_FLAGS += -U flash:w:$(HEXFILE):i
AVRDUDE_FLAGS += -D # Disable auto erase for flash memory.

prog:
	avrdude $(addprefix ,$(AVRDUDE_FLAGS))
