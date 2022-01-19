import matplotlib.pyplot as hadi #use matplotlib packages for ploting and give your alias "hadi" or whatever 

hadi.rcParams["font.family"] = "Book Antiqua" #use matplotlib packages for changing font style of the graph
hadi.rcParams.update({'font.size': 11.5}) #use matplotlib packages for changing the font size

#input data. 
#X as a Big PL Club, and Y as the number of PL titles 
 
x = ['MU', 'City', 'Chelsea', 'Liverpool', 'Arsenal', 'Spurs']      

y = [20, 7, 6, 19, 13, 2] 

#give an instruction to create a line chart
hadi.pie(y, labels = x) 

#create a title
hadi.title("The winners of PL titles of all-time")
           
#create an instruction to show a graph
hadi.show()
