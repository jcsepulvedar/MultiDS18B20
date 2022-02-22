# MultiDS18B20

## Motivation

###
In order to modularize as best as possible a remote smart weather station using a raspberyy pi, I thought "what happens if I need multiple temperature sensors? If one breaks? Can I swap it easily? And looking at some of the existing libraries I saw that none of them could completely help me with that (ca. 2017), they either only worked with 1 sensor or would require to hard code each sensor uID which would defeat the whole purpose. Also the OneWire library was not enough sadly

So I came up with this short algorithm that can read multiple sensors and its completely independent from the ID.

I made this being a complete amateur in ptyhon so there are probably better options for me but this did the trick.

The raspberry pi needs to have its GPIO activated and working.
If I'm not mistaken the DS18B20s cannot be hot swapped so plugging/unplugging one will require a system reboot.

## TODO
###
Make a proper library.
