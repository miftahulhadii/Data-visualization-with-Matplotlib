import matplotlib.pyplot as hadi #use matplotlib packages for ploting and give your alias "hadi" or whatever 

hadi.rcParams["font.family"] = "Arial" #use matplotlib packages for changing font style of the graph
hadi.rcParams.update({'font.size': 11.5}) #use matplotlib packages for changing the font size

#input data. 
#X as an Electric field, and Y as an Energy 
 
x1 = [3, 2, 1, 0, -1, -2, -3]      
y1 = [0.1, 0.15, 0.35, 7, 10, 5, 4.5]

x2 = [3, 2, 1, 0, -1, -2, -3]      
y2 = [0.5, 10, 2.5, 5, 4, 5, 2]

x3 = [3, 2, 1, 0, -1, -2, -3]      
y3 = [2, 5, 5, 2, 3, 3, 3,]

x4 = [3, 2, 1, 0, -1, -2, -3]      
y4 = [2, 4, 3, 4, 3, 1, 1]

hadi.xlabel(r'$E$ (V/nm)') #give a label for x-axis
hadi.ylabel(r'Saturation Time (ns)') #give a label for y-axis

#give a different color for different thickness from 0.5 nm until 2 nm
hadi.plot(x1, y1, marker="o", color="red") 
hadi.plot(x2, y2, marker="o", color="orange")
hadi.plot(x3, y3, marker="o", color="blue")
hadi.plot(x4, y4, marker="o", color="black")

#create a legend for the additional information in the graph
hadi.legend([r"$t$$_{free}$ = 0.5 nm", r"$t$$_{free}$ = 1 nm", r"$t$$_{free}$ = 1.5 nm", r"$t$$_{free}$ = 2 nm"])

#create an instruction to show a graph
hadi.show()
