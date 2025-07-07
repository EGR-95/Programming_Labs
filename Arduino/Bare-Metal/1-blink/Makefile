MCU=atmega328p
F_CPU=16000000UL
CC=avr-gcc
OBJCOPY=avr-objcopy
CFLAGS=-Wall -Os -mmcu=$(MCU) -DF_CPU=$(F_CPU)

TARGET=blink

all:
	$(CC) $(CFLAGS) -o $(TARGET).elf $(TARGET).c
	$(OBJCOPY) -O ihex -R .eeprom $(TARGET).elf $(TARGET).hex

flash: all
	avrdude -c arduino -p m328p -P /dev/ttyUSB0 -b 115200 -U flash:w:$(TARGET).hex
	
clean:
	rm -f *.elf *.hex

