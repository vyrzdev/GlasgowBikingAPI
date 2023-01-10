import os
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


import requests
from datetime import datetime
from json import dumps
from os import remove
CITY_CODE = 237

data = requests.get("https://api.nextbike.net/maps/nextbike-live.json", params={'city': CITY_CODE})
unwrapped = data.json()
country = unwrapped['countries'][0]
city = country['cities'][0]
stations = city['places']

print("Fetching data for logging.")
data_file_name = datetime.utcnow().strftime(f"%Y-%m-%d-%H-%M.json")
with open(f"./api/data/{data_file_name}", 'w') as new_data:
    new_data.write(dumps(stations))

for file in os.listdir('./api/index/'):
    os.remove(f"./api/index/{file}")

data_files = os.listdir("./api/data/")
data_files.reverse()
data_info = {
    "total": len(data_files),
    "most_recent": data_files[0],
    "oldest": data_files[-1],
    "page_size": 50
}
with open('./api/index/info.json', 'w') as info:
    info.write(dumps(data_info))

split_data_files = list(chunks(data_files, 50))
for i, split in enumerate(split_data_files):
    with open(f"./api/index/page-{i}.json", 'w') as page:
        page.write(dumps(split))
