import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


# Get environment details
# print(os.environ)

token = os.environ.get("NOTION_TOKEN")
databaseId = os.environ.get("DATABASE_ID")

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

print("token test: ", token)
print("database id: ", databaseId)


def readDatabase(databaseId, headers):
    readUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'

    res = requests.request("POST", readUrl, headers=headers)

    # test data
    data = res.json()
    print("Read Database Status Code", res.status_code)
    print("Read Database Response Text", res.text)

    # dump data in file
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


readDatabase(databaseId, headers)


def createPage(databaseId, headers):

    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                  {
                      "text": {
                          "content": "Hello One"
                      }
                  }
                ]

            },
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "This is one"
                        }
                    }
                ]

            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Active"
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)

    print("Create Page Status Code", res.status_code)
    print("Create Page Response Text", res.text)


createPage(databaseId, headers)


def updatePage(pageId, headers):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Pretty Good"
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(updateData)

    response = requests.request("PATCH", updateUrl, headers=headers, data=data)

    print("Update Page Status Code: ", response.status_code)
    print("Update Page Response Text: ", response.text)


pageId = 'a9befb72-d5f6-46ba-b1d9-80eaa5836135'
updatePage(pageId, headers)
