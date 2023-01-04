;Start gcode
G28 ;Home all axes
G1 Z5 F5000 ;Lift nozzle
G92 E0 ;Reset extrusion distance
G1 Z0.3 F30 ;Set the first layer height and speed
M204 S1000 ;Set acceleration
M566 X5 Y5 Z0.5 E5 ;Set jerk
M207 S1 F300 T1 ;Set retract length and speed
M221 S1.2 ;Set extrusion multiplier
M83 ;Use relative distances for extrusion
G0 X0 Y0 Z0.3
G1 E1 F1000
G1 X200 Y0 Z0.3
G1 E0 F1000
;End gcode
G1 E-1 F300 ;Retract the filament a bit before lifting the nozzle, to release some pressure
G1 E-1 F300 ;Retract the filament a bit before lifting the nozzle, to release some pressure
G1 F500 Z5 ;Lift the nozzle
G92 E0 ;Reset extrusion distance
