from google import genai
from pydantic import BaseModel

client = genai.Client(api_key='AIzaSyDYvwJcun3O4Pxb0cB1JKAwQ4FAYnLuid8')

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Give me information of the United States.',
    config={ 
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo, 
    }, 
)

print(response.text)