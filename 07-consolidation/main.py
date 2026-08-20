# We're building this:
# GitHub API
#     ↓
# HTTP GET request
#     ↓
# JSON response
#     ↓
# Python dictionary
#     ↓
# Pydantic validation
#     ↓
# Clean Python object
#     ↓
# model_dump()
#     ↓
# JSON file

# In code terms:
# httpx → JSON → dict → Pydantic → model → dict → json.dump()

# We install:
# pip install httpx

# Why httpx?
# Because Python itself doesn't give you the same convenient API-request experience that fetch() gives you in JavaScript.
# httpx is a Python HTTP client.

# HTTP response
#       ↓
# response.json()
#       ↓
# Python dictionary

# This exact shape is every API call, including LLMs:
# httpx.get(url)          →  request goes out over HTTP
# response.status_code    →  did it work? (200 ok, 404 not found, 500 server error, 401 auth...)
# response.json()         →  the JSON body, parsed into a Python dict
# A Claude/OpenAI call is the same three lines — just httpx.post(url, json=..., headers=...) with your prompt in the body and your API key in the headers.

import httpx
from pydantic import BaseModel, ValidationError

url = "https://api.github.com/users/adityahongal"

# response = httpx.get(url)              # send the HTTP GET request
  
# print(response.status_code)            # 200 = OK
# data = response.json()                 # parse the JSON body → Python dict

# print(data)
# print(type(data))
# print(data["login"])
# print(data["name"])
# print(data["public_repos"])
# print(data["followers"])

class GitHubUser(BaseModel):
    login : str
    name : str | None
    public_repos : int
    followers : int

# user = GitHubUser(**data)
# print(user)
# print(user.model_dump())

# Error Handling

#                     ┌── network failure
#                     │
# API request ────────┤
#                     │
#                     └── bad/invalid data

# we have two different failure paths:
# HTTP/API problem
#        ↓
# httpx.HTTPError


# Bad data
#        ↓
# ValidationError

def main():
    try:
      response = httpx.get(url)                 
      response.raise_for_status()          # turn a 4xx/5xx status into an exception - imp
      data = response.json()
      user = GitHubUser(**data)
      print("✅", user.model_dump())

     #   creating a seperate profile.json and storing fetched data into it

      import json
      from pathlib import Path
  
      out_path = Path(__file__).parent / "profile.json"
      with open(out_path, "w", encoding="utf-8") as f:
            json.dump(user.model_dump(), f, indent=4) 
      print("Saved →", out_path.name)
      
    except httpx.HTTPError as e:             # network failure OR bad status (404/500/timeout)
      print("Network/HTTP error:", e)      
      
    except ValidationError as e:             # response didn't match the model's shape
      print("Validation error:", e)        
  
    print("program continued ✅")            

# - response.raise_for_status() — a 404/500 is not automatically an error in httpx; you get a
# response object with a bad status_code. This line converts a bad status into a raised exception
# so your except can catch it. Without it, a 404 would sail through and then blow up later at .json().
# - httpx.HTTPError is the base class covering both network problems (no internet, bad domain) and bad statuses. One except catches the whole family.

if __name__ == "__main__" :
   main()