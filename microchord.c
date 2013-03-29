/* USB chorded keyboard driver built on teensy2.0
 * Copyright (c) 2013 Ryan Brown <ryansb@csh.rit.edu
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include <avr/io.h>
#include <avr/pgmspace.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "usb_keyboard.h"
#include "chord_map.h"

#define LED_CONFIG    (DDRD |= (1<<6))
#define LED_ON        (PORTD &= ~(1<<6))
#define LED_OFF        (PORTD |= (1<<6))
#define CPU_PRESCALE(n)    (CLKPR = 0x80, CLKPR = (n))

uint8_t number_keys[10]=
    {KEY_0,KEY_1,KEY_2,KEY_3,KEY_4,KEY_5,KEY_6,KEY_7,KEY_8,KEY_9};

uint16_t idle_count=0;

int main(void)
{
    uint8_t d, reset_idle;
    uint8_t d_prev=0xFF;

    // set for 16 MHz clock
    CPU_PRESCALE(0);

    // Configure all port B and port D pins as inputs with pullup resistors.
    // See the "Using I/O Pins" page for details.
    // http://www.pjrc.com/teensy/pins.html
    DDRD = 0x00;
    PORTD = 0xFF;

    // Initialize the USB, and then wait for the host to set configuration.
    // If the Teensy is powered without a PC connected to the USB port,
    // this will wait forever.
    usb_init();
    while (!usb_configured()); /* wait */

    // Wait an extra second for the PC's operating system to load drivers
    // and do whatever it does to actually be ready for input
    _delay_ms(1000);

    // Configure timer 0 to generate a timer overflow interrupt every
    // 256*1024 clock cycles, or approx 61 Hz when using 16 MHz clock
    // This demonstrates how to use interrupts to implement a simple
    // inactivity timeout.
    TCCR0A = 0x00;
    TCCR0B = 0x05;
    TIMSK0 = (1<<TOIE0);

    while (1) {
        // read all port D pins
        d = PIND;
        d ^= 0xff;
        // check if any pins are low, but were high previously
        if ((d_prev ^ d) > 1) {
            if (d_prev < d) {
                // key was pressed, for debug send "p" for "pressed"
                usb_keyboard_press(KEY_P, 0);
            }
            else {
                // key was released, send the chord
                usb_keyboard_press(KEY_R, 0);
                switch (d) {
                    case CHORD_E:
                        usb_keyboard_press(KEY_E, 0);
                        break;

                    case CHORD_T:
                        usb_keyboard_press(KEY_T, 0);
                        break;
                    default: break;
                }
                d = 0;
            }
        }
        reset_idle = 0;
        // if any keypresses were detected, reset the idle counter
        if (reset_idle) {
            // stop interrupt routine so we can modify a shared counter
            cli();
            idle_count = 0;
            sei();
        }
        // wait a short delay to debounce input
        d_prev = d;
        _delay_ms(10);
    }
}

ISR(TIMER0_OVF_vect) {
    idle_count++;
    if (idle_count > 61 * 8) {
        idle_count = 0;
    }
}
