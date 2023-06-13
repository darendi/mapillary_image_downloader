import mapillary.interface as mly
import requests
import json


MLY_ACCESS_TOKEN = 'MLY|5866439510132094|d34070c74df8fceb8de54cf3415119a6' #Mapillary API Access Token
mly.set_access_token(MLY_ACCESS_TOKEN)

data = json.loads(
# [east_lng,_south_lat,west_lng,north_lat]
    mly.images_in_bbox(
        bbox={
            "east": 104.9375137971326,
            "south": 11.549363550818883,
            "west": 104.93397469226208, 
            "north": 11.551673410794246,
        },
        image_type="flat",
        compass_angle=(30, 60)
    )
)

with open("3_commerceexpat_30_60_NE.json", mode="w") as f:
    json.dump(data, f, indent=4)

print('done!')

