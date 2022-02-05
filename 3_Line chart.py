import matplotlib.pyplot as hadi #use matplotlib packages for ploting and give your alias "hadi" or whatever 

hadi.rcParams["font.family"] = "Book Antiqua" #use matplotlib packages for changing font style of the graph
hadi.rcParams.update({'font.size': 11.5}) #use matplotlib packages for changing the font size

#input data. 
#X as a year, and Y as a revenue 
 
x = [2010, 2012, 2014, 2016, 2018, 2020, 2022]      

y1 = [107.044, 207.063, 259.124, 222, 230, 180, 400]      
y2 = [430.225, 351.858, 598.677, 428.000, 256.908, 485.701, 385.484]

hadi.xlabel(r'Year') #give a label for x-axis
hadi.ylabel(r'Revenue') #give a label for y-axis

#give an instruction to create a line chart
hadi.plot(x, y1, color="red") 
hadi.plot(x, y2, color="orange")

#create a legend for the additional information in the graph
hadi.legend([r"Google", r"Microsoft"])

#create a title
hadi.title("Company revenue in the last 12 years")
           
#create an instruction to show a graph
hadi.show()
