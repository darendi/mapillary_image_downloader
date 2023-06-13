import mapillary.interface as mly
import json

MLY_ACCESS_TOKEN = 'MLY|5866439510132094|d34070c74df8fceb8de54cf3415119a6'
mly.set_access_token(MLY_ACCESS_TOKEN)

data = mly.get_image_close_to(
    longitude=104.9247653, latitude=11.5546877, radius=5, image_type="flat"
).to_dict()

with open("get_image_close_to_5.json", mode="w") as f:
    json.dump(data, f, indent=4)