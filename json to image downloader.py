import mapillary.interface as mly
import requests
import json
import os
import shutil

MLY_ACCESS_TOKEN = 'MLY|5866439510132094|d34070c74df8fceb8de54cf3415119a6' #Mapillary API Access Token
mly.set_access_token(MLY_ACCESS_TOKEN)

# Assign directory
directory = r'C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\lat long image downloader\json_to_jpg'

# Loop through JSON files in the directory

for filename in os.listdir(directory):
    json_file = os.path.join(directory, filename)

    with open(json_file, 'r') as f:
        data = json.load(f)

    for feature in data['features']:
        sequence_id = feature['properties']['sequence_id']
        image_id = feature['properties']['id']

        # Create sequence directory if it doesn't exist
        sequence_directory = os.path.join(directory, sequence_id)
        os.makedirs(sequence_directory, exist_ok=True)

        # Get image URL
        url = f"https://graph.mapillary.com/{image_id}?fields=thumb_2048_url"
        headers = {'Authorization': f'OAuth {MLY_ACCESS_TOKEN}'}
        response = requests.get(url, headers=headers)
        response_data = response.json()
        image_url = response_data['thumb_2048_url']

        # Download and save the image
        image_path = os.path.join(sequence_directory, f"{image_id}.jpg")
        with open(image_path, 'wb') as handler:
            image_data = requests.get(image_url, stream=True).content
            handler.write(image_data)

        # Create image directory if it doesn't exist
        image_directory = os.path.join(directory, f"{json_file.replace('.json','')}")
        os.makedirs(image_directory, exist_ok=True)

        # Move sequence directories to image directory
        shutil.move(image_path, image_directory) 
        os.removedirs(sequence_directory)

        # Delete empty sequence directories


print('done!')
