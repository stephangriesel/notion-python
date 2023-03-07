from dotenv import load_dotenv
load_dotenv()

import os 

# Get environment details
# print(os.environ)

token = os.environ.get("NOTION_TOKEN")
token = os.environ.get("DATABASE_ID")

print(os.environ.get("NOTION_TOKEN"))
print(os.environ.get("DATABASE_ID"))

import requests
from datetime import datetime, timezone

DATABASE_ID = "8ed35ea0fd1c4019a453871faef4cceb"

headers = {
  "Authorization": "Bearer" + "NOTION_TOKEN",
  "Content-Type": "application/json",
  "Notion-Version": "2022-06-28"
}

def get_pages():
  url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

  payload = {"page_size": 100}
  response = requests.post(url, json=payload, headers=headers)

  data = response.json()

  # Comment out to dump all data to a file
  import json
  with open('db.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

  results = data("results")
  return results

pages = get_pages()
for page in pages:
  page_id = page["id"]
  props = page["properties"]
  url = props["URL"]["title"][0]["text"]["content"]
  title = props["Title"]["rich_text"][0]["text"]["content"]
  published = props["Published"]["date"]["start"]
  published = datetime.fromisoformat(published)
  print(url, title, published)