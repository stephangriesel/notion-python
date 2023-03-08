from dotenv import load_dotenv
load_dotenv()

import os 
import requests

# Get environment details
# print(os.environ)

token = os.environ.get("NOTION_TOKEN")
databaseId = os.environ.get("DATABASE_ID")

headers = {
  "Authorization": "Bearer " + token,
  "Notion-Version": "2022-06-28"
}

print(token)
print(databaseId)

def readDatabase(databaseId, headers):
  readUrl = f'https://api.notion.com/v1/databases/{databaseId}'

  res = requests.request("GET", readUrl, headers=headers)
  print(res.status_code)

def createPage():
  pass

def updatePage():
  pass

readDatabase(databaseId,headers)