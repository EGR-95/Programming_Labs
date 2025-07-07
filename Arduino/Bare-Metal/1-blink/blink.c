#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    DDRB |= (1 << PB5); // Set PB5 (pin 13) as output

    while (1) {
        PORTB ^= (1 << PB5); // Toggle pin
        _delay_ms(500);
    }
}

