import streamlit as st
import requests
import json
import pandas as pd
import datetime

page = st.sidebar.selectbox("ページ選択",["users", "rooms", "bookings"])

if page=="users":
    st.title("ユーザー登録")

    with st.form(key = "user"):
        username: str = st.text_input('ユーザー名', max_chars=12)
        data = {
            "username": username
        }
        submit_botton = st.form_submit_button(label ="Submit")

    if submit_botton:
        st.write("## 送信データ")
        st.write("## レスポンスデータ")
        url="http://127.0.0.1:8000/users"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success("ユーザー登録完了")
        st.write(res.status_code)
        st.json(res.json())

if page=="rooms":
    st.title("会議室登録")

    with st.form(key = "room"):
        room_name: str = st.text_input('room名', max_chars=12)
        capacity: int = st.number_input('最大人数', step=1)
        data = {
            "room_name": room_name,
            "capacity": capacity
        }
        submit_botton = st.form_submit_button(label ="Submit")

    if submit_botton:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンスデータ")
        url="http://127.0.0.1:8000/rooms"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())

if page=="bookings":
    st.title("会議室予約画面")

    #ユーザー一覧取得
    url_users = "http://127.0.0.1:8000/users"
    res = requests.get(url_users)
    users = res.json()
    st.json(users)

    #ユーザー名をキー、ユーザーIDをバリュー
    users_dict = {}
    for user in users:
        users_dict[user['username']] = user["user_id"]
    st.write(users_dict)

    #会議室一覧取得
    url_rooms = "http://127.0.0.1:8000/rooms"
    res = requests.get(url_rooms)
    rooms = res.json()

    #会議室一覧表示
    st.write("### 会議室一覧")
    df_rooms=pd.DataFrame(rooms)
    df_rooms.columns = ["会議室名", "定員", "会議室id"]
    st.table(df_rooms)

    #予約一覧取得
    url_bookings = "http://127.0.0.1:8000/bookings"
    res = requests.get(url_bookings)
    bookings = res.json()
    df_bookings=pd.DataFrame(bookings)

    #ユーザーidをキー、ユーザー名をバリュー
    users_id = {}
    for user in users:
        users_id[user['user_id']] = user["username"]

    #roomidをキー、room名,capacityをバリュー
    rooms_id = {}
    for room in rooms:
        rooms_id[room['room_id']] = {
            "room_name": room["room_name"],
            "capacity": room["capacity"],
        }
    
    #IDを各値に変換
    to_username= lambda x: users_id[x]
    to_room_name = lambda x: rooms_id[x]["room_name"]
    to_datetime = lambda x: datetime.datetime.fromisoformat(x).strftime('%Y/%m/%d %H:%M')

    #特定の値に適用
    df_bookings["user_id"] = df_bookings["user_id"].map(to_username)
    df_bookings["room_id"] = df_bookings["room_id"].map(to_room_name)
    df_bookings["start_datetime"] = df_bookings["start_datetime"].map(to_datetime)
    df_bookings["end_datetime"] = df_bookings["end_datetime"].map(to_datetime)

    #カラム名変更
    df_bookings = df_bookings.rename(columns={
        "user_id": "予約者名",
        "room_id": "会議室名",
        "booked_num": "予約人数",
        "start_datetime": "開始日時",
        "end_datetime": "終了日時",
        "booking_id": "予約番号"
    })

    #予約一覧表示
    st.write("### 会議室一覧")
    st.table(df_bookings)

    #会議名をキー、roomIDとcapacityをバリュー
    rooms_dict = {}
    for room in rooms:
        rooms_dict[room['room_name']] = {
            "room_id": room["room_id"],
            "capacity": room["capacity"],
        }

    with st.form(key = "booking"):
        username: str = st.selectbox("予約者名", users_dict.keys())
        room_name: str = st.selectbox("会議室名", rooms_dict.keys())
        booked_num: int = st.number_input('最大人数', step=1, min_value=1)
        date = st.date_input("日付", min_value=datetime.date.today())
        start_time = st.time_input("開始時刻",value=datetime.time(hour=9,minute=0))
        end_time = st.time_input("終了時刻",value=datetime.time(hour=20,minute=0))
        submit_botton = st.form_submit_button(label ="予約")

    if submit_botton:
        user_id: int = users_dict[username]
        room_id: int = rooms_dict[room_name]["room_id"]
        capacity: int = rooms_dict[room_name]["capacity"]
        data = {
            "user_id": user_id,
            "room_id": room_id,
            "booked_num": booked_num,
            "start_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat(),
            "end_datetime": datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
            ).isoformat(),
        }
        #定員より多い予約人数の場合
        if booked_num > capacity:
            st.error(f"{room_name}の定員は、{capacity}以下です。")
        #開始時刻 >= 終了時刻
        elif start_time >= end_time:
            st.error("開始時刻が終了時刻を超えています")
        #利用時間を超えている場合
        elif start_time < datetime.time(hour=9, minute=0, second=0) or end_time > datetime.time(hour=22, minute=0, second=0):
            st.error("利用時間は9:00~22:00になります")
        else:
            #会議室予約
            url="http://127.0.0.1:8000/bookings"
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success("予約完了")
            elif res.status_code == 404 and res.json()['detail'] == "Already booked":
                st.success("既に予約が入っています")
            st.json(res.json())
