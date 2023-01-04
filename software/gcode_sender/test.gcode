;START_GCODE
M73 P0 R24 
M73 Q0 S24 
M201 X1000 Y1000 Z200 E5000 ; sets maximum accelerations, mm/sec^2 
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm / sec
M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2 
M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec 
M107
M862.3 P "MK3S" ; printer model check
M862.1 P0.4 ; nozzle diameter check
M115 U3.11.0 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode
M104 S230 ; set extruder temp
M140 S0 ; set bed temp
M109 S230 ; wait for extruder temp
G28 W ; home all without mesh bed level
G80 ; mesh bed leveling

G1 Z0.3 F720 
G1 Y-3 F1000 ; go outside print area 
G92 E0 
G1 X60 E9 F1000 ; intro line 
G1 X100 E9 F1000 ; intro line

G92 E0 
M221 S95 ; Set flow

G0 Z0.2 F10800 ; Move to z height
G1 E-0.8 F1800 ; Retract
G1 Z0.3 F10800 ; Z hop
G0 X10.0 Y0.4356 F10800; Moving to line position
G1 Z0.2 F10800 ; Z hop return
G1 E0.8 F1800 ; Un-retract
G1 X10.0 Y200.0 E67.7582 F2400; Create Line 

;END_GCODE
G1 Z9 F720 ; Move print head up 
G1 X0 Y200 F3600 ; park 
G1 Z57 F720 ; Move print head further up 
G4 ; wait 
M221 S100 ; reset flow

M104 S0 ; turn off temperature
M107 ; turn off fan 
M84 ; disable motors 
M73 P100 R0 
M73 Q100 S0