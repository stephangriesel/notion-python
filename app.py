from dotenv import load_dotenv
load_dotenv()

import os 
import requests
import json

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
  readUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'

  res = requests.request("POST", readUrl, headers=headers)

  # test data
  data = res.json()
  print(res.status_code)
  # print(res.text)

  # dump data in file
  with open('./db.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False)

def createPage():
  pass

def updatePage():
  pass

readDatabase(databaseId,headers)