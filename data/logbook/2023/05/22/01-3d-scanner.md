# 3D Scanner

Bought a very old (but supposedly very good) 3D scanner on eBay.
Creaform HandyScan 3D — REVscan.  2008 or so, but it has lasers and not those useless LEDs.
FireWire, hence had to buy 3 (!) adapters just to connect it to USB-C.
Also bought a used Windows laptop, since the software that Creaform provides
only runs on Windows.  There's also a power supply that hooks up to a very
strange cable — didn't want it to fry any of my good laptops if anything goes wrong.

The software (VxScan 3.1.2) required a CD Key.
Creaform were very and very friendly and gave it to me in no time.
What I have is a discontinued model, so I really appreciate their help.

One of the big hiccups was getting the sensors connected to the PC.
That scanner device features two CMOS sensors, Dragonfly by Point Grey Research — what a name!
Point Grey seems to now be owned by [Teledyne FLIR](https://www.flir.com).
Here's where to get Windows drivers for those cameras: [FlyCapture SDK](https://www.flir.com/products/flycapture-sdk/?vertical=machine+vision&segment=iis).

FlyCap2 2.13.3.61 is detecting my dual cameras as a single device (probably due to the hub), the model name is "Dragonfly".
The sensor is Sony ICX204AL, driver FirePRO (PGR1394.sys) — 2.7.3.161.
The best news? — I'm able to see the image!  The picture seems to be coming only from one of the sensors though, black and white.
7.5 FPS on average.  Updated to 15 FPS in settings, now it's much smoother.

One of the camera's board appears to be dead.  No way to flash the firmware.
Flir.com's tech support is beyond amazing, even though I never bought the product directly though them, they seem to care about this old-ass camera more than I do.

Went ahead and bought an OEM edition of Creaform's scanner off eBay for $500 — Omega Willowwood.
Lucky me, when it arrived, had almost exactly the same hardware inside, and the boards were Dragonfly v1.8 HIBW.
Swapped the boards, now my HandyScan has both cameras working!

The hard part now is to make the software use the new camera, since the siral number is different.
But it's just software trickery at this point, the hardware is working.
