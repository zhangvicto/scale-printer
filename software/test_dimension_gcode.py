from load_cell.mass import measure_mass, tare
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings, square_size
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim
from time import perf_counter

mode = 'P'
mass_data = []
dimension_data = []

for i in range(1,9):


    iter = i
    time_start = perf_counter()

    creep = 0.0005*5000/(3*60)*4 # grams/sec * 4 load cells

    with open("./gcode_gen/test.gcode", "w") as f:
        
        gcode = genStart(iter=iter, nozzleD=0.4, Te=230, Tb=0, Vp=settings['moveSpeed'])
        gcode += gcode_gen(mode, iter, settings)
        gcode += genEnd(iter)

        f.write(gcode)
    
    # Tare Weight before Starting Print
    time_zero = perf_counter() - time_start
    zero_weight = tare()

    # Account for Creep
    initial_zero = zero_weight - time_zero*creep

    # Pass in Printing Parameters
    send_gcode(iter, './gcode_gen/test.gcode')

    
    measure_time = perf_counter() - time_zero

    # Once print finishes, check weight
    mass = measure_mass()
    if mass is not None: 
        mass_real = mass - measure_time*creep - initial_zero
        print("Measuring Mass. \n")
        mass_data.append(mass_real)
    else: 
        print("Measuring Error Occurred. \n")
        mass_data.append(None)


    # Find Dimension of the Print
    print("Starting CV Process. \n")
    img = image_process() # Process Image
    edge = edges(img) # Canny Edge Detection

    distX = analyze_edge(edge) # Get the bed x-axis length in terms of pixels

    x=[]
    y=[]

    # Calculate Print Location
    if distX is not None:
        ratio = distX/255 # Pixels per mm
        print('Ratio: {}'.format(ratio))
        # Pixel = mm * ratio

        if mode == 'L': 
            if distX > 0: 
                xOffset = 20
                x1 = xOffset + round((iter-1)*15*ratio)
                x2 = round(x1 + 10*ratio)
                x = [x1, x2]
                print(x)
                print(x)
                y1 = round(180*ratio) - 20
                y2 = round(180*ratio)
                y = [y1, y2]
            else: 
                x = [None, None]
                y = [None, None]

        if mode == 'P': 
            if distX: 
                initial_gap = 10 if iter==1 else 0
                gap = 10
                x1 = round((initial_gap + gap/2 + (iter-1)*square_size)*ratio)
                x2 = round(x1 + (square_size + gap)*ratio)
                x = [x1, x2]
                print(x)
                yOffset = -5
                y1 = round((200 - (square_size + gap + yOffset))*ratio)
                y2 = round((200- yOffset)*ratio)
                y = [y1, y2]
                print(y)
            else: 
                x = [None, None]
                y = [None, None]
        
        if mode == 'C': 
            x = [None, None]
            y = [None, None]

    dimensions = find_dim(x, y, distX, edge, iter) # Find dim

    if dimensions is not None: 
        widths = dimensions[0]
        lengths = dimensions[1]
        dimension_data.append(dimensions)
    else: 
        dimension_data.append(None)

    print("Mass: {}. Dimensions: {}.".format(mass_data, dimension_data))