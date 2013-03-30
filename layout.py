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
    "LPAR":     0b00001100,
    "RPAR":     0b00000011,
    "LSQARE":   0b00101100,
    "RSQUARE":  0b00100011,
    "LANGLE":   0b00001110,
    "RANGLE":   0b00000111,
    "LCURLY":   0b00101110,
    "RCURLY":   0b00100111,
    "BACKQUO":  0b00000100,
    "SINGQUO":  0b00000010,
    "FSLASH":   0b00000001,
    "BSLASH":   0b00010000,
    "CARAT":    0b00100110,
    "DASH":     0b00001011,
    "UNDERBAR": 0b00101001,
    "DOLLAR":   0b00001101,
    "HASH":     0b00001001,
    "AMP":      0b00101101,
    "COLON":    0b00001010,
    "SEMICOL":  0b00101010,
    "BAR":      0b01001011,
    "PCT":      0b00101011,
    "PLUS":     0b00000101,
    "TILDE":    0b00100101,
    "DQUOTE":   0b00000110,
    "AT":       0b00101111,
    "ASTERISK": 0b00001111,
    "SUPER":    0b01000100,
    "ENTER":    0b01001000,
}


l_hand = {
    #           mprmigor
    "E":      0b00001000,
    "T":      0b00010000,
    "A":      0b00100000,
    "O":      0b01000000,
    "I":      0b00011000,
    "N":      0b00101000,
    "S":      0b01001000,
    "H":      0b00110000,
    "R":      0b01010000,
    "D":      0b01100000,
    "L":      0b00111000,
    "C":      0b01110000,
    "U":      0b01101000,
    "M":      0b01011000,
    "W":      0b01111000,
    "F":      0b00001100,
    "G":      0b00010100,
    "Y":      0b00100100,
    "P":      0b01000100,
    "B":      0b00011100,
    "V":      0b00101100,
    "K":      0b01001100,
    "J":      0b00110100,
    "X":      0b01010100,
    "Q":      0b01100100,
    "Z":      0b00111100,
    "SQUOTE": 0b00100010,
    "COMMA":  0b00010010,
    "DQUOTE": 0b00110010,
    "DOT":    0b00001010,
    "BANG":   0b00011010,
    "QUE":    0b00101010,
    "DASH":   0b01001010,
    "EQ":     0b01101010,
    "SHIFT":  0b00001001,
    "SPACE":  0b00101001,
    "TAB":    0b01001001,
    "ESC":    0b01111001,
    "ALT":    0b00110001,
    "CTRL":   0b00010001,
    "BKSP":   0b01000001,
    "DEL":    0b00100001,
    "INS":    0b00101101,
    "PGDN":   0b00011001,
    "PGUP":   0b01100001,
    "HOME":   0b01110001,
    "END":    0b00111001,
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
map_fname = "chord_map.h"
if not dup:
    with open(map_fname, 'w') as chord_map:
        chord_map.write("/* This file was autogenerated by layout.py */\n")
        chord_map.write("/* Right hand map */\n")
        chord_map.writelines(["#define CHORD_%s %d\n" % (k, v) for k, v in
                              sorted(r_hand.items())])
        chord_map.write("/* Left hand map */\n")
        chord_map.writelines(["#define CHORD_%s %d\n" % (k, v) for k, v in
                              sorted(l_hand.items())])
