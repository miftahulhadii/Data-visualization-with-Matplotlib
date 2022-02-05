import matplotlib.pyplot as hadi #use matplotlib packages for ploting and give your alias "hadi" or whatever 

hadi.rcParams["font.family"] = "Book Antiqua" #use matplotlib packages for changing font style of the graph
hadi.rcParams.update({'font.size': 11.5}) #use matplotlib packages for changing the font size

#input data. 
#X as a Big PL Club, and Y as the number of PL titles 
 
x = ['Chelsea', 'Liverpool', 'Arsenal', 'Spurs','MU', 'City']      

y = [6, 19, 13, 2, 20, 7]

colors = ['blue','red','purple','white','maroon','skyblue']

#give an instruction to create a line chart
hadi.pie(y, labels = x, colors = colors)

#create a title
hadi.title("The winners of PL titles of all-time")

#create a legend
hadi.legend([r"Chelsea", r"Liverpool", r"Arsenal", r"Spurs",r"MU", r"City"])
           
#create an instruction to show a graph
hadi.show()
