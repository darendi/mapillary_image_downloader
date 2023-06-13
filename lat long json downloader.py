import mapillary.interface as mly
import pandas as pd
import json
import os

MLY_ACCESS_TOKEN = 'MLY|5866439510132094|d34070c74df8fceb8de54cf3415119a6' #Mapillary API Access Token
mly.set_access_token(MLY_ACCESS_TOKEN)

# Read coordinates from CSV file
location = pd.read_csv(r"C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\lat long image downloader\intersections point coords.csv")
json_folder_location = (r"C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\lat long image downloader\json_to_jpg")

# Extract longitude and latitude coordinates as float arrays
x_coord = location['x_coord'].astype(float)
y_coord = location['y_coord'].astype(float)

# Create a new folder to store the generated JSON files
folder_name = 'generated_json_files' 
os.makedirs(folder_name, exist_ok=True)

# Iterate over coordinates and download images
for i, j in zip(x_coord, y_coord): 
    
    # Create a new folder to store the generated JSON files
    #folder_name = os.path.join(json_folder_location, f"{i}_{j}") 
    #os.makedirs(folder_name, exist_ok=True)

    data = mly.get_image_close_to(longitude=i, latitude=j, radius=5, image_type="flat",).to_dict() #loop through x_coord and y_coord values in .csv file
    file_name = f"{i}_{j}.json" #file name for each json file iteration 
    file_path = os.path.join(folder_name, file_name) #place json file in created folder
    
    with open(file_path, mode="w") as f: #cwrite json file

        json.dump(data, f, indent=4) 

print('done!')