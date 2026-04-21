import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:5000"

st.set_page_config(page_title="Lost & Found System", layout="wide")

st.title("Lost & Found Management System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Register",
        "Login",
        "Add Admin",
        "View Admins",
        "Add Department",
        "Add Category",
        "Add Location",
        "Report Lost Item",
        "Report Found Item",
        "View Lost Items",
        "View Found Items",
        "Upload Image",
        "Claim Item",
        "Return Item",
        "Send Notification",
        "Submit Report",
        "Feedback"
    ]
)

# ---------------- DASHBOARD ---------------- #

if menu == "Dashboard":

    try:
        lost = requests.get(API + "/lost").json()
        found = requests.get(API + "/found").json()
    except:
        lost = []
        found = []

    col1, col2 = st.columns(2)

    col1.metric("Lost Items", len(lost))
    col2.metric("Found Items", len(found))

# ---------------- REGISTER ---------------- #

elif menu == "Register":

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone")

    if st.button("Register"):

        data = {
            "name": name,
            "email": email,
            "password": password,
            "phone": phone
        }

        requests.post(API + "/register", json=data)

        st.success("User Registered")

# ---------------- LOGIN ---------------- #

elif menu == "Login":

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        r = requests.post(API + "/login", json={"email": email, "password": password})

        st.write(r.json())

# ---------------- ADMIN ---------------- #

elif menu == "Add Admin":

    name = st.text_input("Admin Name")
    email = st.text_input("Admin Email")
    password = st.text_input("Password")

    if st.button("Add Admin"):

        requests.post(API + "/admin", json={
            "name": name,
            "email": email,
            "password": password
        })

        st.success("Admin Added")

elif menu == "View Admins":

    r = requests.get(API + "/admin")

    df = pd.DataFrame(r.json())

    st.dataframe(df)

# ---------------- DEPARTMENT ---------------- #

elif menu == "Add Department":

    name = st.text_input("Department Name")
    location = st.text_input("Office Location")

    if st.button("Add Department"):

        requests.post(API + "/department", json={
            "name": name,
            "location": location
        })

        st.success("Department Added")

# ---------------- CATEGORY ---------------- #

elif menu == "Add Category":

    name = st.text_input("Category Name")
    desc = st.text_area("Description")

    if st.button("Add Category"):

        requests.post(API + "/category", json={
            "name": name,
            "description": desc
        })

        st.success("Category Added")

# ---------------- LOCATION ---------------- #

elif menu == "Add Location":

    name = st.text_input("Location Name")
    desc = st.text_area("Description")

    if st.button("Add Location"):

        requests.post(API + "/location", json={
            "name": name,
            "description": desc
        })

        st.success("Location Added")

# ---------------- LOST ITEM ---------------- #

elif menu == "Report Lost Item":

    title = st.text_input("Title")
    desc = st.text_area("Description")
    date = st.date_input("Date")
    user_id = st.number_input("User ID", step=1)

    category_id = st.number_input("Category ID", step=1)
    location_id = st.number_input("Location ID", step=1)

    if st.button("Submit Lost Item"):

        requests.post(API + "/lost", json={
            "title": title,
            "description": desc,
            "date": str(date),
            "user_id": int(user_id),
            "category_id": int(category_id),
            "location_id": int(location_id)
        })

        st.success("Lost Item Reported")

# ---------------- FOUND ITEM ---------------- #

elif menu == "Report Found Item":

    title = st.text_input("Title")
    desc = st.text_area("Description")
    date = st.date_input("Date")
    user_id = st.number_input("User ID", step=1)

    category_id = st.number_input("Category ID", step=1)
    location_id = st.number_input("Location ID", step=1)

    if st.button("Submit Found Item"):

        requests.post(API + "/found", json={
            "title": title,
            "description": desc,
            "date": str(date),
            "user_id": int(user_id),
            "category_id": int(category_id),
            "location_id": int(location_id)
        })

        st.success("Found Item Added")

# ---------------- VIEW LOST ---------------- #

elif menu == "View Lost Items":

    r = requests.get(API + "/lost")

    df = pd.DataFrame(r.json())

    st.dataframe(df)

# ---------------- VIEW FOUND ---------------- #

elif menu == "View Found Items":

    r = requests.get(API + "/found")

    df = pd.DataFrame(r.json())

    st.dataframe(df)

# ---------------- IMAGE ---------------- #

elif menu == "Upload Image":

    url = st.text_input("Image URL")
    date = st.date_input("Upload Date")
    lost_id = st.number_input("Lost ID", step=1)
    found_id = st.number_input("Found ID", step=1)

    if st.button("Upload Image"):

        requests.post(API + "/image", json={
            "url": url,
            "date": str(date),
            "lost_id": int(lost_id),
            "found_id": int(found_id)
        })

        st.success("Image Uploaded")

# ---------------- CLAIM ---------------- #

elif menu == "Claim Item":

    user_id = st.number_input("User ID", step=1)
    found_id = st.number_input("Found Item ID", step=1)
    date = st.date_input("Claim Date")

    if st.button("Claim Item"):

        requests.post(API + "/claim", json={
            "user_id": int(user_id),
            "found_id": int(found_id),
            "date": str(date)
        })

        st.success("Claim Submitted")

# ---------------- RETURN ---------------- #

elif menu == "Return Item":

    found_id = st.number_input("Found ID", step=1)
    claim_id = st.number_input("Claim ID", step=1)
    date = st.date_input("Return Date")

    if st.button("Return Item"):

        requests.post(API + "/return", json={
            "found_id": int(found_id),
            "claim_id": int(claim_id),
            "date": str(date)
        })

        st.success("Item Returned")

# ---------------- NOTIFICATION ---------------- #

elif menu == "Send Notification":

    user_id = st.number_input("User ID", step=1)
    msg = st.text_area("Message")
    date = st.date_input("Date")

    if st.button("Send Notification"):

        requests.post(API + "/notification", json={
            "user_id": int(user_id),
            "message": msg,
            "date": str(date)
        })

        st.success("Notification Sent")

# ---------------- REPORT ---------------- #

elif menu == "Submit Report":

    user_id = st.number_input("User ID", step=1)
    desc = st.text_area("Report Description")
    date = st.date_input("Date")

    if st.button("Submit Report"):

        requests.post(API + "/report", json={
            "user_id": int(user_id),
            "description": desc,
            "date": str(date)
        })

        st.success("Report Submitted")

# ---------------- FEEDBACK ---------------- #

elif menu == "Feedback":

    user_id = st.number_input("User ID", step=1)
    rating = st.slider("Rating", 1, 5)
    msg = st.text_area("Message")

    if st.button("Send Feedback"):

        requests.post(API + "/feedback", json={
            "user_id": int(user_id),
            "rating": rating,
            "message": msg
        })

        st.success("Feedback Sent")