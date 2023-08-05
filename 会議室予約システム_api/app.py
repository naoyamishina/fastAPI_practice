import streamlit as st
import requests
import json
import random
import datetime

page = st.sidebar.selectbox("ページ選択",["users", "rooms", "bookings"])

if page=="users":
    st.title("APIテスト画面（ユーザー）")

    with st.form(key = "user"):
        user_id: int = random.randint(1,10)
        username: str = st.text_input('ユーザー名', max_chars=12)
        data = {
            "user_id": user_id,
            "username": username
        }
        submit_botton = st.form_submit_button(label ="Submit")

    if submit_botton:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンスデータ")
        url="http://127.0.0.1:8000/users"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())

if page=="rooms":
    st.title("APIテスト画面（rooms）")

    with st.form(key = "room"):
        room_id: int = random.randint(1,10)
        room_name: str = st.text_input('room名', max_chars=12)
        capacity: int = st.number_input('最大人数', step=1)
        data = {
            "room_id": room_id,
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
    st.title("APIテスト画面（booking）")

    with st.form(key = "booking"):
        booking_id: int = random.randint(1,10)
        user_id: int = random.randint(1,10)
        room_id: int = random.randint(1,10)
        booked_num: int = st.number_input('最大人数', step=1)
        date = st.date_input("日付", min_value=datetime.date.today())
        start_time = st.time_input("開始時刻",value=datetime.time(hour=9,minute=0))
        end_time = st.time_input("終了時刻",value=datetime.time(hour=20,minute=0))
        data = {
            "booking_id": booking_id,
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
        submit_botton = st.form_submit_button(label ="Submit")

    if submit_botton:
        st.write("## 送信データ")
        st.json(data)
        st.write("## レスポンスデータ")
        url="http://127.0.0.1:8000/bookings"
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())
