r_hand = {
    #             mrogimrp
    1:          0b10000001,
    2:          0b10000010,
    3:          0b10000011,
    4:          0b10000100,
    5:          0b10000101,
    6:          0b10000110,
    7:          0b10000111,
    8:          0b10001000,
    9:          0b10001001,
    0:          0b10001010,
    "lpar":     0b00001100,
    "rpar":     0b00000011,
    "lsqare":   0b00101100,
    "rsquare":  0b00100011,
    "langle":   0b00001110,
    "rangle":   0b00000111,
    "lcurly":   0b00101110,
    "rcurly":   0b00100111,
    "backquo":  0b00000100,
    "singquo":  0b00000010,
    "fslash":   0b00000001,
    "bslash":   0b00010000,
    "carat":    0b00100110,
    "dash":     0b00001011,
    "underbar": 0b00101001,
    "dollar":   0b00001101,
    "hash":     0b00001001,
    "amp":      0b00101101,
    "colon":    0b00001010,
    "semicol":  0b00101010,
    "bar":      0b01001011,
    "pct":      0b00101011,
    "plus":     0b00000101,
    "tilde":    0b00100101,
    "dquote":   0b00000110,
    "at":       0b00101111,
    "asterisk": 0b00001111,
}


l_hand = {
    #           mprmigor
    "e":      0b00001000,
    "t":      0b00010000,
    "a":      0b00100000,
    "o":      0b01000000,
    "i":      0b00011000,
    "n":      0b00101000,
    "s":      0b01001000,
    "h":      0b00110000,
    "r":      0b01010000,
    "d":      0b01100000,
    "l":      0b00111000,
    "c":      0b01110000,
    "u":      0b01101000,
    "m":      0b01011000,
    "w":      0b01111000,
    "f":      0b00001100,
    "g":      0b00010100,
    "y":      0b00100100,
    "p":      0b01000100,
    "b":      0b00011100,
    "v":      0b00101100,
    "k":      0b01001100,
    "j":      0b00110100,
    "x":      0b01010100,
    "q":      0b01100100,
    "z":      0b00111100,
    "squote": 0b00100010,
    "comma":  0b00010010,
    "dquote": 0b00110010,
    "dot":    0b00001010,
    "bang":   0b00011010,
    "que":    0b00101010,
    "dash":   0b01001010,
    "eq":     0b01101010,
    "shift":  0b00001001,
    "space":  0b00101001,
    "esc":    0b01111001,
    "alt":    0b00110001,
    "ctrl":   0b00010001,
    "bksp":   0b01000001,
    "del":    0b00100001,
    "ins":    0b00101101,
    "pgdn":   0b00011001,
    "pgup":   0b01100001,
    "home":   0b01110001,
    "end":    0b00111001,
}

dup = False

for k, v in r_hand.items():
    if r_hand.values().count(v) > 1:
        dup = True
        print "Symbols layout conflict on %s with value %s" % (k, v)

for k, v in l_hand.items():
    if l_hand.values().count(v) > 1:
        dup = True
        print "Letter conflict on %s with value %s" % (k, v)
map_fname = "chord_map_autogen.h"
if not dup:
    with open(map_fname, 'w') as chord_map:
        chord_map.write("/* This file was autogenerated by layout.py */\n")
        chord_map.write("/* Right hand map */\n")
        chord_map.writelines(["#define CHORD_%s %d\n" % (k, v) for k, v in
                              sorted(r_hand.items())])
        chord_map.write("/* Left hand map */\n")
        chord_map.writelines(["#define CHORD_%s %d\n" % (k, v) for k, v in
                              sorted(l_hand.items())])
