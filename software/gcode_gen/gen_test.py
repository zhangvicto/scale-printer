def generate_gcode(x_pos, y_pos, z_pos, end_x_pos, end_y_pos, end_z_pos, extrusion_rate, feedrate, travel_speed, retraction_z_lift, extrusion_multiplier, z_hop_height, acceleration, max_xy_jerk, max_z_jerk, max_e_jerk, retraction_speed, retraction_length, first_layer_height, first_layer_speed):
    # Set the position of the 3D printer's nozzle to the starting point of the line
    gcode_command = "G0 X{} Y{} Z{}\n".format(x_pos, y_pos, z_pos)

    # Set the extrusion rate and turn the extruder on
    gcode_command += "G1 E{} F{}\n".format(extrusion_rate, feedrate)

    # Move the nozzle to the end point of the line
    gcode_command += "G1 X{} Y{} Z{}\n".format(end_x_pos, end_y_pos, end_z_pos)

    # Turn the extruder off
    gcode_command += "G1 E0 F{}\n".format(feedrate)

    # Add start gcode
    start_gcode = ";Start gcode\n"
    start_gcode += "G28 ;Home all axes\n"
    start_gcode += "G1 Z5 F5000 ;Lift nozzle\n"
    start_gcode += "G92 E0 ;Reset extrusion distance\n"
    start_gcode += "G1 Z{} F{} ;Set the first layer height and speed\n".format(first_layer_height, first_layer_speed)
    start_gcode += "M204 S{} ;Set acceleration\n".format(acceleration)
    start_gcode += "M566 X{} Y{} Z{} E{} ;Set jerk\n".format(max_xy_jerk, max_xy_jerk, max_z_jerk, max_e_jerk)
    start_gcode += "M207 S1 F{} T{} ;Set retract length and speed\n".format(retraction_speed, retraction_length)
    start_gcode += "M221 S{} ;Set extrusion multiplier\n".format(extrusion_multiplier)
    start_gcode += "M83 ;Use relative distances for extrusion\n"

    # Add end gcode
    end_gcode = ";End gcode\n"
    end_gcode += "G1 E-1 F300 ;Retract the filament a bit before lifting the nozzle, to release some pressure\n"
    end_gcode += "G1 E-1 F300 ;Retract the filament a bit before lifting the nozzle, to release some pressure\n"
    end_gcode += "G1 F{} Z{} ;Lift the nozzle\n".format(travel_speed, z_hop_height)
    end_gcode += "G92 E0 ;Reset extrusion distance\n"

    # Open a file for writing the gcode
    with open("line.gcode", "w") as gcode_file:
        # Write the start gcode to the file
        gcode_file.write(start_gcode)

        # Write the gcode for the line to the file
        gcode_file.write(gcode_command)

        # Write the end gcode to the file
        gcode_file.write(end_gcode)

# Generate gcode for a line that starts at (0, 0, 0) and ends at (200, 0, 0) with a first layer height of 0.3mm, an extrusion multiplier of 1.2, and an acceleration of 1000mm/s^2
generate_gcode(0, 0, 0.3, 200, 0, 0.3, 1, 1000, 500, 5, 1.2, 5, 1000, 5, 0.5, 5, 300, 1, 0.3, 30)