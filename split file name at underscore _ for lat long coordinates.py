import os

directory = r'C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\source'

# Take values before underscore _ as x coords
with open('x_with data.txt', 'a') as f: # open/create 'x.txt' file in append mode 'a'
    for folder in os.listdir(directory): 
        lng = folder.split('_')[0] # splits the file name at underscore _
        f.write(lng + '\n') # write values of lng with a new line created after each value

# Take values after underscore _ as y coords
with open('y_with data.txt', 'a') as g: # open/create 'y.txt' file in append mode 'a'
    for folder in os.listdir(directory):
        lat = folder.split('_')[1] # splits the file name at underscore _
        g.write(lat + '\n') # write values of lng with a new line created after each value
