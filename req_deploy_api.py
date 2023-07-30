import requests
import json

def main():
    url = "https://deploy_api-2-q4140702.deta.app/"
    data = {
      "x": 3,
      "y": 4,
    }
    res = requests.post(url, json.dumps(data))

    try:
        res.raise_for_status()  # レスポンスがエラーでないことを確認
        if res.text:  # レスポンスが空でないことを確認
            print("レスポンスボディ:", res.json())
        else:
            print("空のレスポンスです。")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTPエラーが発生しました: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"リクエストエラーが発生しました: {req_err}")
    except json.JSONDecodeError as json_err:
        print(f"JSONデコードエラーが発生しました: {json_err}")

if __name__ == '__main__':
  main()
