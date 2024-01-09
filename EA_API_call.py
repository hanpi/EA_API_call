# Import statements
import pandas as pd
import requests                   # For API call
import pprint                     # "pretty print" JSON data in a more human readable-format (not currently used)
import matplotlib.pyplot as plt

#Create my own function to make a call to the EA API for a specified year and location ID, and convert JSON object to dataframe

def EaApiCall(id, year):
  """takes a location id and year, makes a call on EA's API for that location and year, converts the JSON content into a flat dataframe, and returns the dataframe"""
  base = 'http://environment.data.gov.uk/water-quality'
  id = id

  # For API structure, base and parameter information, see https://environment.data.gov.uk/water-quality/view/doc/reference

  endpoint = f"{base}/id/sampling-point/{id}/measurements"
  payload = {'year':year}

  response = requests.get(
    endpoint,
    params = payload
  )

  # RESPONSE OBJECT: the value is a code which has meaning (e.g. 200 for 'OK', 404 for 'URL does not exist')
  print(f"API call for year {year} RESPONSE OBJECT CODE: {response}")

  # retrieve the JSON formatted content (the data payload) of the response
  content = response.json()

  # JSON => Pandas DataFrame conversion using normalize to flatten nested structure
  df = pd.DataFrame(pd.json_normalize(content['items']))

  # return created dataframe
  return df

df_AN_Woodbri = EaApiCall('AN-WOODBRI', 2000)
for y in range(2001,2024):
  df_AN_Woodbri = pd.concat([df_AN_Woodbri, EaApiCall('AN-WOODBRI', y)])


#print(df_AN_Woodbri.head(1))
#print(df_AN_Woodbri.tail(1))
