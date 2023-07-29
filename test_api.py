import requests
import json

def main():
    url = "http://127.0.0.1:8000/item"
    data = {
      "name": "T_shirt",
      "description": "white",
      "price": 4000,
      "tax": 1.1
    }
    res = requests.post(url, json.dumps(data))
    print (res.json())

if __name__ == '__main__':
  main()
