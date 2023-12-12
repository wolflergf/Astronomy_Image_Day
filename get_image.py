import requests
from dotenv import load_dotenv
import os

load_dotenv()
my_key = os.getenv('API_KEY')

END_POINT = 'https://api.nasa.gov/planetary/apod'
image_params = {
    'api_key': my_key,
    'count': 1
}

def get_image():
    response = requests.get(END_POINT, params=image_params)
    response.raise_for_status()
    data = response.json()
    title = (data[0]['title'])
    explanation = (data[0]['explanation'])
    url = (data[0]['hdurl'])
    return title, explanation, url