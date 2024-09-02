from bs4 import BeautifulSoup
import pandas as pd
import aiohttp
import asyncio
import json


# https://www.cargurus.com/?px8324=p2&sourceContext=cargurusTM&cgcid=2161&cgagid=910472&ax8324=63580845&type=GoogleAdWordsSearch&kw=cargurus&matchtype=e&ad=261318744220&placement=&networktype=g&device=c&devicemodel=&adposition=&physloc=1014221&intloc=&aceid=&cid=141954540&agid=7773125700&tgtid=kwd-5133662569&fid=&gad_source=1&gclid=CjwKCAjwodC2BhAHEiwAE67hJEO4kocA_A_NSXI4lD6pqcZdFSmpxNkXjoKv8Y7SHfxP-Y7JuBYpZBoCG5oQAvD_BwE
class Scraper:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        # Opening JSON file
        file = open('car_data.json')
        
        # returns JSON object as a dictionary
        self.car_data = json.load(file)
    
    async def scrap_carGurus(self, make, model, zip):
        make = self.car_data["car_gurus_data"]["make"][make]
        model = make["model"][model]

        print("Make: ", make)
        print("Model:  ", model)
        # async with self.session.get(f"https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity={model}&zip={zip}") as resp:
        #     print(resp.status)
        #     print(await resp.text())


# Options for best value
# 1. Lowest price
# 2. Lowest miles

make = "Subaru"
model = "Impreza"
min_price = "" # Optional
max_price = "" # Optional
zip = "91744"
radius = "" # Default value => 100 miles

session = aiohttp.ClientSession()
scraper_instance = Scraper(session)
asyncio.run(scraper_instance.scrap_carGurus(make, model, zip))