# Particle Swarm Optimization of 3D Printing Parameters on Open-Source Commercial 3D Printer

<img src="/image/printer.jpg" alt="printer" />

# Current Progress
- [x] Mechanical Design
- [x] Test Load Cells
- [x] Test Camera
- [ ] Test Dimensional Measurement {80%}
- [ ] PSO Implementation {90%}
- [ ] Documentation {50%}

## Additional Features 
- [ ] Web Server {5%}
- [ ] Refinement {5%}

# Hardware
## Mechanical Design
<img src="/image/v1.png" alt="v1" />
The mechanical is designed around the Prusa MK3s, as it is a versatile printer that can be easily modified. Load cells and a camera were mounted on the printer using 3D printed parts. 

Load Cell Configuration: 
<img src="/image/load-cell.jpg" alt="image" />


## Bill of Materials
Found in repo. 
Total cost excluding printer is CAD $150.00 (to be updated).

# Software
Flowchart: 
<img src="/image/flowchart.png" alt="flowchart" />

## PSO Algo Implementation
The PSO algorithm runs each calibration sequence by taking an initial guess to generate the first iteration, then using the results of the first iteration to generate the next iteration. The process repeats until the results are desirable or if the max number of iteration is reached. This implementation is adapted from a previous experiment: https://doi.org/10.1089/3dp.2022.0012. 

## Computer Vision
A camera is used to measure the length of each print, as the pixel size can be roughly estimated using the dimension of the bed.
<img src="/image/camera-view.png" alt="camera" />

## Load Cell
Load cell measurement is taken and averaged. Measurement is taken after every iteration and used to generate the next iteration. 
<img src="/image/load-cell-readings.png" alt="image" />

## Gcode Generation
The Gcode for each interation is generated automatically, using PSO results from the previous run. 

# The Build 
(More detailed instructions in paper in the future)
1. Mount all mechanical components
2. Electrical wiring for all load cells and Raspberry Pi
3. Setup Raspberry Pi with any OS that supports Python
4. git pull repo

## Wiring Diagram 
(coming soon)

# User Instructions

## Requirements
Before running any calibration sequence, the required libraries must be installed for Python. 

If pip is not installed, install it first. 
```
sudo apt-get pip3
```

Then go to the subdirectory where the scripts are located.
```
cd scale-printer/software
```

Run install the requirements using pip.
```
pip3 install -r requirements.txt
```

## Begin Optimization
SSH into the Raspberry Pi and start the script. 
(Assuming you are still in the /softare subdirectory, if not, go to the proper directory)
```
python setup.py
```

Proceed with the instructions. Select your desired calibration method (line, plane, cube). Now just wait and let the printer do its magic!

## Calibrating Sensors
All the load cells will be calibrated before the actual print calibration sequence. Ensure that you are getting correct values for the weights. If they are not right, then there may be wiring or issues with the power supply.  


# Open-Source Licenses
<img src="/image/oshw_facts.png" alt="licenses" />

Thank you to Dr. Joshua Pearce, the Western University FAST Research Lab, and the Thompson Endowment for supporting this project. 