# Inverter and new electrical system

Currently I have no way to continiously power my [Starlink RV](https://www.starlink.com/rv) directly from the boat’s electrical system.
That’s mostly due to not having an inverter aboard, and partially because my battery bank is only 12V, Starlink needs 48.

Since I need to get an inverter for my boat anyway, [Multi RS Solar](https://www.victronenergy.com/inverters-chargers/multi-rs-solar) seems like a good choice.
At only 11 kgs of weight, it will act as: battery charger, inverter, solar charge controller.  3-in-1.  I’ll be able to get rid of small 12V Victron MPPT charge controllers that I currently use, which will save space and reduce amount of wiring.

Once 5KW of 230VAC is here, it’ll power: Starlink, washer/dryer, things that can’t be charged from 12VDC, microwave, and many other cool devices.  By wiring four lead-acid batteries in series, I’ll be able to provide enough juice for onboard climate control, water heater, and other fun gizmos.

I couldn’t care less about starting my diesel engine, all that will get gutted anyway the moment I replace hydraulics with 10KW IP67 electric motors.  Powering those will require LiFePo4 batteries, at least $12K worth of.  But the motors are 48VDC so the same battery bank should be able to power both my boat’t electronics and propulsion system.  Having one battery bank to do it all is not ideal, but will do for the time being.  I’ll likely get two banks later and might even get two Multi RS Solar to completely separate my hulls’ circuits.


## Shore power

My current ProMariner shore-to-battery charger is 12V, will have to replace it with something new, but it’s not urgent as long as my solar array and wind turbines pull the weight.  There’s [Skylla-TG](https://www.victronenergy.com/chargers/skylla-24v-48v) from Victron that could charge a 48V bank, but it’s like 10 kg of weight and requires 230VAC input, I might just get rid of shore input altogether — it only adds weight and creates additional fire and electrolysis hazard below water line.


## 12V

This change will require a 48-to-12 DC-DC converter to power my lights and other electronics.
Victron’s [Orion-Tr 48/12-30](https://www.victronenergy.com/dc-dc-converters/orion-tr-dc-dc-converters-isolated) looks great.  430W of continious output ought to be enough for anybody.


## Solar

I’ll need at least two more 100W Sunpower flexible solar panels.
As I add more and more panels, the setup will likely require additional charge controllers, but that’s a good problem to have.


## How much it’s gonna cost

| Syntax                        |       Price |
| ----------------------------- | ----------: |
| Multi RS Solar                |   $2,335.00 |
| Orion-Tr 48/12-30             |     $222.70 |
| 12V jump box                  |     $172.46 |
| 2 x 100W SunPower solar panel |     $310.00 |
| Deep cycle 12V marine battery |      $89.80 |
| Total                         | $(a lot).00 |


## References

 - [Datasheet-Multi-RS-Solar-EN-.pdf](https://www.victronenergy.com/upload/documents/Datasheet-Multi-RS-Solar-EN-.pdf)
 - [Datasheet-Orion-Tr-DC-DC-converters-isolated-100-250-400W-EN.pdf](https://www.victronenergy.com/upload/documents/Datasheet-Orion-Tr-DC-DC-converters-isolated-100-250-400W-EN.pdf)
