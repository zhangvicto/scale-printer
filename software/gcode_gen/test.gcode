; generated by PrusaSlicer 2.5.0+win64 on 2023-01-09 at 21:19:14 UTC 




M73 P0 R0.45 
M73 Q0 S0.45 
M201 X1000 Y1000 Z200 E5000 ; sets maximum accelerations, mm/sec^2 
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm / sec
M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2 
M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec 
M107
;TYPE:Custom
M862.3 P "MK3S" ; printer model check
M862.1 P0.4 ; nozzle diameter check
M115 U3.11.0 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode
M104 S230 ; set extruder temp
M140 S0 ; set bed temp
M109 S230 ; wait for extruder temp
G28 W ; home all without mesh bed level
G1 Z0.2 F720 
G1 Y186 F1000 
G92 E0 
G1 X40 E9 F1000 ; intro line 
G1 X60 E9 F1000 ; intro line

G92 E0 
M221 S95

; Don't change E values below. Excessive value can damage the printer.

M907 E538 ; set extruder motor current
G21 ; set units to millimeters
G90 ; use absolute coordinates
M83 ; use relative distances for extrusion
M900 K0 ; Filament gcode LA 1.5
M107
;LAYER_CHANGE
;Z:0.2
;HEIGHT:0.2
;BEFORE_LAYER_CHANGE
G92 E0.0
;0.2


G0 Z0.2 F720 ; Move to z height
G0 X0.0 Y0.0 F4800 ; Moving to plane position
M204 S800
; printing plane start id:0 copy 0 
G1 E-1.5 F1800 ; Retract
G1 Z0.4 F720 ; Z hop
G0 X20.4356 Y0.0 F4800 ; Move to box start
G1 Z0.2 F720 ; Z hop return
G1 E1.5 F1800 ; Un-retract
G1 X20.4356 Y15.0 E0.93544 F2400 ; Draw perimeter (up)
G1 X35.4356 Y15.0 E0.93544 F2400 ; Draw perimeter (right)
G1 X35.4356 Y0.0 E0.93544 F2400 ; Draw perimeter (down)
G1 X20.4356 Y0.0 E0.93544 F2400 ; Draw perimeter (down)
G0 X20.8712 Y0.4356 F4800 ; Step inwards to print next perimeter
G1 X20.8712 Y14.5644 E0.88111 F2400 ; Draw perimeter (up)
G1 X35.0 Y14.5644 E0.88111 F2400 ; Draw perimeter (right)
G1 X35.0 Y0.4356 E0.88111 F2400 ; Draw perimeter (down)
G1 X20.8712 Y0.4356 E0.88111 F2400 ; Draw perimeter (down)
G0 X21.3069 Y0.8712 F4800 ; Step inwards to print next perimeter
G1 X21.3069 Y14.1288 E0.82678 F2400 ; Draw perimeter (up)
G1 X34.5644 Y14.1288 E0.82678 F2400 ; Draw perimeter (right)
G1 X34.5644 Y0.8712 E0.82678 F2400 ; Draw perimeter (down)
G1 X21.3069 Y0.8712 E0.82678 F2400 ; Draw perimeter (down)
G0 X21.7425 Y1.3069 F4800 ; Step inwards to print next perimeter
G1 X21.7425 Y13.6931 E0.77244 F2400 ; Draw perimeter (up)
G1 X34.1288 Y13.6931 E0.77244 F2400 ; Draw perimeter (right)
G1 X34.1288 Y1.3069 E0.77244 F2400 ; Draw perimeter (down)
G1 X21.7425 Y1.3069 E0.77244 F2400 ; Draw perimeter (down)
G0 X21.8514 Y1.4158 F4800 ; Move to fill start
G0 X22.4674 Y1.4158 F4800 ; Move
G1 X21.8514 Y2.0318 E0.05433 F2400 ; Fill
G0 X21.8514 Y2.6479 F4800 ; Move
G1 X23.0835 Y1.4158 E0.10867 F2400 ; Fill
G0 X23.6996 Y1.4158 F4800 ; Move
G1 X21.8514 Y3.2639 E0.163 F2400 ; Fill
G0 X21.8514 Y3.88 F4800 ; Move
G1 X24.3156 Y1.4158 E0.21733 F2400 ; Fill
G0 X24.9317 Y1.4158 F4800 ; Move
G1 X21.8514 Y4.4961 E0.27166 F2400 ; Fill
G0 X21.8514 Y5.1121 F4800 ; Move
G1 X25.5477 Y1.4158 E0.326 F2400 ; Fill
G0 X26.1638 Y1.4158 F4800 ; Move
G1 X21.8514 Y5.7282 E0.38033 F2400 ; Fill
G0 X21.8514 Y6.3442 F4800 ; Move
G1 X26.7799 Y1.4158 E0.43466 F2400 ; Fill
G0 X27.3959 Y1.4158 F4800 ; Move
G1 X21.8514 Y6.9603 E0.489 F2400 ; Fill
G0 X21.8514 Y7.5764 F4800 ; Move
G1 X28.012 Y1.4158 E0.54333 F2400 ; Fill
G0 X28.628 Y1.4158 F4800 ; Move
G1 X21.8514 Y8.1924 E0.59766 F2400 ; Fill
G0 X21.8514 Y8.8085 F4800 ; Move
G1 X29.2441 Y1.4158 E0.65199 F2400 ; Fill
G0 X29.8601 Y1.4158 F4800 ; Move
G1 X21.8514 Y9.4245 E0.70633 F2400 ; Fill
G0 X21.8514 Y10.0406 F4800 ; Move
G1 X30.4762 Y1.4158 E0.76066 F2400 ; Fill
G0 X31.0923 Y1.4158 F4800 ; Move
G1 X21.8514 Y10.6566 E0.81499 F2400 ; Fill
G0 X21.8514 Y11.2727 F4800 ; Move
G1 X31.7083 Y1.4158 E0.86933 F2400 ; Fill
G0 X32.3244 Y1.4158 F4800 ; Move
G1 X21.8514 Y11.8888 E0.92366 F2400 ; Fill
G0 X21.8514 Y12.5048 F4800 ; Move
G1 X32.9404 Y1.4158 E0.97799 F2400 ; Fill
G0 X33.5565 Y1.4158 F4800 ; Move
G1 X21.8514 Y13.1209 E1.03232 F2400 ; Fill
G0 X22.0041 Y13.5842 F4800 ; Move
G1 X34.0199 Y1.5685 E1.05972 F2400 ; Fill
G0 X34.0199 Y2.1845 F4800 ; Move
G1 X22.6201 Y13.5842 E1.00539 F2400 ; Fill
G0 X23.2362 Y13.5842 F4800 ; Move
G1 X34.0199 Y2.8006 E0.95106 F2400 ; Fill
G0 X34.0199 Y3.4166 F4800 ; Move
G1 X23.8523 Y13.5842 E0.89672 F2400 ; Fill
G0 X24.4683 Y13.5842 F4800 ; Move
G1 X34.0199 Y4.0327 E0.84239 F2400 ; Fill
G0 X34.0199 Y4.6488 F4800 ; Move
G1 X25.0844 Y13.5842 E0.78806 F2400 ; Fill
G0 X25.7004 Y13.5842 F4800 ; Move
G1 X34.0199 Y5.2648 E0.73372 F2400 ; Fill
G0 X34.0199 Y5.8809 F4800 ; Move
G1 X26.3165 Y13.5842 E0.67939 F2400 ; Fill
G0 X26.9326 Y13.5842 F4800 ; Move
G1 X34.0199 Y6.4969 E0.62506 F2400 ; Fill
G0 X34.0199 Y7.113 F4800 ; Move
G1 X27.5486 Y13.5842 E0.57073 F2400 ; Fill
G0 X28.1647 Y13.5842 F4800 ; Move
G1 X34.0199 Y7.7291 E0.51639 F2400 ; Fill
G0 X34.0199 Y8.3451 F4800 ; Move
G1 X28.7807 Y13.5842 E0.46206 F2400 ; Fill
G0 X29.3968 Y13.5842 F4800 ; Move
G1 X34.0199 Y8.9612 E0.40773 F2400 ; Fill
G0 X34.0199 Y9.5772 F4800 ; Move
G1 X30.0129 Y13.5842 E0.35339 F2400 ; Fill
G0 X30.6289 Y13.5842 F4800 ; Move
G1 X34.0199 Y10.1933 E0.29906 F2400 ; Fill
G0 X34.0199 Y10.8094 F4800 ; Move
G1 X31.245 Y13.5842 E0.24473 F2400 ; Fill
G0 X31.861 Y13.5842 F4800 ; Move
G1 X34.0199 Y11.4254 E0.1904 F2400 ; Fill
G0 X34.0199 Y12.0415 F4800 ; Move
G1 X32.4771 Y13.5842 E0.13606 F2400 ; Fill
G0 X33.0931 Y13.5842 F4800 ; Move
G1 X34.0199 Y12.6575 E0.08173 F2400 ; Fill
; stop printing plane id:0 copy 0
G1 Z9 F720 ; Move print head up 
G1 X100 Y200 F3600 ; park 
G1 Z57 F720 ; Move print head further up 
G4 ; wait 
M221 S100 ; reset flow

M104 S0 ; turn off temperature
M140 S0 ; turn off heatbed
M107 ; turn off fan 
M84 ; disable motors 
M73 P100 R0 
M73 Q100 S0

; filament used [mm] = 30
; filament used [cm3] = 0.05
; filament used [g] = 0.08
; filament cost = 0.01
; total filament used [g] = 0.08
; total filament cost = 0.01
; estimated printing time (normal mode) = 00m 17s
; estimated printing time (silent mode) = 00m 17s

; prusaslicer_config = begin
; avoid_crossing_perimeters = 0
; avoid_crossing_perimeters_max_detour = 0
; bed_custom_model = 
; bed_custom_texture = 
; bed_shape = 0x0,250x0,250x210,0x210
; bed_temperature = 0
; before_layer_gcode = ;BEFORE_LAYER_CHANGE\nG92 E0.0\n;[layer_z]\n\n
; between_objects_gcode = 
; bottom_fill_pattern = monotonic
; bottom_solid_layers = 3
; bottom_solid_min_thickness = 0.5
; bridge_acceleration = 1000
; bridge_angle = 0
; bridge_fan_speed = 100
; bridge_flow_ratio = 0.95
; bridge_speed = 25
; brim_separation = 0.1
; brim_type = outer_only
; brim_width = 0
; clip_multipart_objects = 1
; color_change_gcode = M600\nG1 E0.4 F1500 ; prime after color change
; compatible_printers_condition_cummulative = "printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK3.*/ and nozzle_diameter[0]==0.4";"nozzle_diameter[0]!=0.8 and ! (printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material)"
; complete_objects = 0
; cooling = 1
; cooling_tube_length = 5
; cooling_tube_retraction = 91.5
; default_acceleration = 1000
; default_filament_profile = "Prusament PLA"
; default_print_profile = 0.15mm QUALITY @MK3
; deretract_speed = 0
; disable_fan_first_layers = 1
; dont_support_bridges = 0
; draft_shield = disabled
; duplicate_distance = 6
; elefant_foot_compensation = 0.2
; end_filament_gcode = "; Filament-specific end gcode"
; end_gcode = {if max_layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+1, max_print_height)} F720 ; Move print head up{endif}\nG1 X0 Y200 F3600 ; park\n{if max_layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+49, max_print_height)} F720 ; Move print head further up{endif}\nG4 ; wait\nM221 S100 ; reset flow\nM900 K0 ; reset LA\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|@0.25 nozzle MK3).*/}M907 E538 ; reset extruder motor current{endif}\nM104 S0 ; turn off temperature\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\nM84 ; disable motors
; ensure_vertical_shell_thickness = 1
; external_perimeter_extrusion_width = 0.6
; external_perimeter_speed = 35
; external_perimeters_first = 0
; extra_loading_move = -2
; extra_perimeters = 0
; extruder_clearance_height = 20
; extruder_clearance_radius = 45
; extruder_colour = ""
; extruder_offset = 0x0
; extrusion_axis = E
; extrusion_multiplier = 1
; extrusion_width = 0.5
; fan_always_on = 1
; fan_below_layer_time = 100
; filament_colour = #FF8000
; filament_cooling_final_speed = 3.4
; filament_cooling_initial_speed = 2.2
; filament_cooling_moves = 4
; filament_cost = 25.4
; filament_density = 1.24
; filament_diameter = 1.75
; filament_load_time = 0
; filament_loading_speed = 28
; filament_loading_speed_start = 3
; filament_max_volumetric_speed = 15
; filament_minimal_purge_on_wipe_tower = 15
; filament_notes = ""
; filament_ramming_parameters = "120 100 6.6 6.8 7.2 7.6 7.9 8.2 8.7 9.4 9.9 10.0| 0.05 6.6 0.45 6.8 0.95 7.8 1.45 8.3 1.95 9.7 2.45 10 2.95 7.6 3.45 7.6 3.95 7.6 4.45 7.6 4.95 7.6"
; filament_settings_id = "Generic PLA"
; filament_soluble = 0
; filament_spool_weight = 0
; filament_toolchange_delay = 0
; filament_type = PLA
; filament_unload_time = 0
; filament_unloading_speed = 90
; filament_unloading_speed_start = 100
; filament_vendor = Generic
; fill_angle = 45
; fill_density = 20%
; fill_pattern = grid
; first_layer_acceleration = 800
; first_layer_acceleration_over_raft = 0
; first_layer_bed_temperature = 0
; first_layer_extrusion_width = 0.42
; first_layer_height = 0.2
; first_layer_speed = 20
; first_layer_speed_over_raft = 30
; first_layer_temperature = 230
; full_fan_speed_layer = 4
; fuzzy_skin = none
; fuzzy_skin_point_dist = 0.8
; fuzzy_skin_thickness = 0.3
; gap_fill_enabled = 1
; gap_fill_speed = 40
; gcode_comments = 0
; gcode_flavor = marlin
; gcode_label_objects = 1
; gcode_resolution = 0.0125
; gcode_substitutions = 
; high_current_on_filament_swap = 0
; host_type = octoprint
; infill_acceleration = 1000
; infill_anchor = 2.5
; infill_anchor_max = 12
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0.5
; infill_first = 0
; infill_only_where_needed = 0
; infill_overlap = 25%
; infill_speed = 85
; interface_shells = 0
; ironing = 0
; ironing_flowrate = 15%
; ironing_spacing = 0.1
; ironing_speed = 15
; ironing_type = top
; layer_gcode = ;AFTER_LAYER_CHANGE\n;[layer_z]
; layer_height = 0.3
; machine_limits_usage = emit_to_gcode
; machine_max_acceleration_e = 5000,5000
; machine_max_acceleration_extruding = 1250,1250
; machine_max_acceleration_retracting = 1250,1250
; machine_max_acceleration_travel = 1500,1250
; machine_max_acceleration_x = 1000,960
; machine_max_acceleration_y = 1000,960
; machine_max_acceleration_z = 200,200
; machine_max_feedrate_e = 120,120
; machine_max_feedrate_x = 200,100
; machine_max_feedrate_y = 200,100
; machine_max_feedrate_z = 12,12
; machine_max_jerk_e = 4.5,4.5
; machine_max_jerk_x = 8,8
; machine_max_jerk_y = 8,8
; machine_max_jerk_z = 0.4,0.4
; machine_min_extruding_rate = 0,0
; machine_min_travel_rate = 0,0
; max_fan_speed = 100
; max_layer_height = 0.25
; max_print_height = 210
; max_print_speed = 200
; max_volumetric_extrusion_rate_slope_negative = 0
; max_volumetric_extrusion_rate_slope_positive = 0
; max_volumetric_speed = 0
; min_bead_width = 85%
; min_fan_speed = 100
; min_feature_size = 25%
; min_layer_height = 0.07
; min_print_speed = 15
; min_skirt_length = 4
; mmu_segmented_region_max_width = 0
; notes = 
; nozzle_diameter = 0.4
; only_retract_when_crossing_perimeters = 0
; ooze_prevention = 0
; output_filename_format = {input_filename_base}_{layer_height}mm_{initial_filament_type}_{printer_model}_{print_time}.gcode
; overhangs = 1
; parking_pos_retraction = 92
; pause_print_gcode = M601
; perimeter_acceleration = 800
; perimeter_extruder = 1
; perimeter_extrusion_width = 0.5
; perimeter_generator = arachne
; perimeter_speed = 50
; perimeters = 2
; physical_printer_settings_id = 
; post_process = 
; print_settings_id = 0.30mm DRAFT @MK3
; printer_model = MK3S
; printer_notes = Don't remove the following keywords! These keywords are used in the "compatible printer" condition of the print and filament profiles to link the particular print and filament profiles to this printer profile.\nPRINTER_VENDOR_PRUSA3D\nPRINTER_MODEL_MK3\n
; printer_settings_id = Original Prusa i3 MK3S & MK3S+
; printer_technology = FFF
; printer_variant = 0.4
; printer_vendor = 
; raft_contact_distance = 0.2
; raft_expansion = 1.5
; raft_first_layer_density = 90%
; raft_first_layer_expansion = 3
; raft_layers = 0
; remaining_times = 1
; resolution = 0
; retract_before_travel = 1
; retract_before_wipe = 0%
; retract_layer_change = 1
; retract_length = 0.8
; retract_length_toolchange = 4
; retract_lift = 0.4
; retract_lift_above = 0
; retract_lift_below = 209
; retract_restart_extra = 0
; retract_restart_extra_toolchange = 0
; retract_speed = 35
; seam_position = aligned
; silent_mode = 1
; single_extruder_multi_material = 0
; single_extruder_multi_material_priming = 0
; skirt_distance = 2
; skirt_height = 3
; skirts = 1
; slice_closing_radius = 0.049
; slicing_mode = regular
; slowdown_below_layer_time = 15
; small_perimeter_speed = 30
; solid_infill_below_area = 0
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0.5
; solid_infill_speed = 80
; spiral_vase = 0
; standby_temperature_delta = -5
; start_filament_gcode = "M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0"
; start_gcode = M862.3 P "[printer_model]" ; printer model check\nM862.1 P[nozzle_diameter] ; nozzle diameter check\nM115 U3.11.0 ; tell printer latest fw version\nG90 ; use absolute coordinates\nM83 ; extruder relative mode\nM104 S[first_layer_temperature] ; set extruder temp\nM140 S[first_layer_bed_temperature] ; set bed temp\nM190 S[first_layer_bed_temperature] ; wait for bed temp\nM109 S[first_layer_temperature] ; wait for extruder temp\nG28 W ; home all without mesh bed level\nG80 ; mesh bed leveling\n{if filament_settings_id[initial_tool]=~/.*Prusament PA11.*/}\nG1 Z0.3 F720\nG1 Y-3 F1000 ; go outside print area\nG92 E0\nG1 X60 E9 F1000 ; intro line\nG1 X100 E9 F1000 ; intro line\n{else}\nG1 Z0.2 F720\nG1 Y-3 F1000 ; go outside print area\nG92 E0\nG1 X60 E9 F1000 ; intro line\nG1 X100 E12.5 F1000 ; intro line\n{endif}\nG92 E0\nM221 S{if layer_height<0.075}100{else}95{endif}\n\n; Don't change E values below. Excessive value can damage the printer.\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3).*/}M907 E430 ; set extruder motor current{endif}\n{if print_settings_id=~/.*(SPEED @MK3|DRAFT @MK3).*/}M907 E538 ; set extruder motor current{endif}
; support_material = 0
; support_material_angle = 0
; support_material_auto = 1
; support_material_bottom_contact_distance = 0
; support_material_bottom_interface_layers = 0
; support_material_buildplate_only = 0
; support_material_closing_radius = 2
; support_material_contact_distance = 0.2
; support_material_enforce_layers = 0
; support_material_extruder = 0
; support_material_extrusion_width = 0.38
; support_material_interface_contact_loops = 0
; support_material_interface_extruder = 0
; support_material_interface_layers = 2
; support_material_interface_pattern = rectilinear
; support_material_interface_spacing = 0.2
; support_material_interface_speed = 80%
; support_material_pattern = rectilinear
; support_material_spacing = 2
; support_material_speed = 45
; support_material_style = grid
; support_material_synchronize_layers = 0
; support_material_threshold = 50
; support_material_with_sheath = 0
; support_material_xy_spacing = 60%
; temperature = 230
; template_custom_gcode = 
; thick_bridges = 0
; thin_walls = 0
; threads = 8
; thumbnails = 160x120
; thumbnails_format = PNG
; toolchange_gcode = 
; top_fill_pattern = monotonic
; top_infill_extrusion_width = 0.45
; top_solid_infill_speed = 40
; top_solid_layers = 4
; top_solid_min_thickness = 0.7
; travel_speed = 180
; travel_speed_z = 12
; use_firmware_retraction = 0
; use_relative_e_distances = 1
; use_volumetric_e = 0
; variable_layer_height = 1
; wall_distribution_count = 1
; wall_transition_angle = 10
; wall_transition_filter_deviation = 25%
; wall_transition_length = 0.4
; wipe = 1
; wipe_into_infill = 0
; wipe_into_objects = 0
; wipe_tower = 1
; wipe_tower_bridging = 10
; wipe_tower_brim_width = 2
; wipe_tower_no_sparse_layers = 0
; wipe_tower_rotation_angle = 0
; wipe_tower_width = 60
; wipe_tower_x = 170
; wipe_tower_y = 125
; wiping_volumes_extruders = 70,70
; wiping_volumes_matrix = 0
; xy_size_compensation = 0
; z_offset = 0
; prusaslicer_config = end