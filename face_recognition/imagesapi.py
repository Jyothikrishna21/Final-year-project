from PIL import Image
import io
import requests
from images_update import makenew

def getimages():
    url = "http://localhost:3000/api/missingpeople/getallpersons"
    response = requests.get(url)

    if response.status_code == 200:
        finaldata = response.json()
        makenew()
        
        for person in finaldata:
            fdata = person['image']['data']['data'] 
            
            newobj = bytes(fdata)
            
            newname = f"{person['name']}_{person['adhaar_number']}"

            img = Image.open(io.BytesIO(newobj))
            img.save(f"./images/{newname}.png")
            
            print(f"Image saved as {newname}.png")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

