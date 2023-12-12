import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
my_key = os.getenv('API_KEY')

# Define API endpoint
END_POINT = 'https://api.nasa.gov/planetary/apod'

# Define parameters for API request
image_params = {
    'api_key': my_key,
    'count': 1
}

def get_image():
    # Send GET request to API endpoint with defined parameters
    response = requests.get(END_POINT, params=image_params)
    
    # Raise exception if request was unsuccessful
    response.raise_for_status()
    
    # Parse response data as JSON
    data = response.json()
    
    # Extract title, explanation, and URL from response data
    title = (data[0]['title'])
    explanation = (data[0]['explanation'])
    url = (data[0]['hdurl'])
    
    # Return title, explanation, and URL
    return title, explanation, url