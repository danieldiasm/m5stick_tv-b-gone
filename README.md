# m5stick_tv-b-gone
This is a TV-B-Gone project using a M5 Stick

## What does it do?
Toggle power on devices using the IR port on a **M5 Stick C Plus**

Theoretically it would work in any M5 Stack device that have a IR port (like M5 Stack, Lite, Atom or Stick), with some code adaptations (The display for example, can exist or not)

## Adding more devices to control

I may do this later, but there is a lot of different protocols for IR control, on this Sony devices I've used a logic analyzer to get the protocol used and reproduce it.


## Look out for!
On M5 Stick, the internal IR is inverted, duty cycle on 100 means 0% and 0 means 100%. But using an external pin, it is inverted.