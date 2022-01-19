import matplotlib.pyplot as hadi #use matplotlib packages for ploting and give your alias "hadi" or whatever

hadi.rcParams["font.family"] = "Book Antiqua" #use matplotlib packages for changing font style of the graph
hadi.rcParams.update({'font.size': 11.5}) #use matplotlib packages for changing the font size

data = {"Physics":70, "Mathematics":50, "Chemistry":30, "Comp. Science":100} #the data

major = list(data.keys()) #give an instruction to group the major from the data list
students = list(data.values()) #give an instruction to group the number of students from the data list

#give an instruction to create a bar chart included major and students data
hadi.bar(major, students, color ="purple") 

hadi.xlabel(r'Major') #give a name for x-axis
hadi.ylabel('Number of students') #give a name for y-axis

#create a title for the chart
hadi.title("The number of students in Science Department ITERA")

#create an instruction to show a chart
hadi.show()
