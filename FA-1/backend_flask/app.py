from flask import Flask, request, jsonify
from db_config import db, cursor
from datetime import datetime

app = Flask(__name__)

# ---------------- USER ---------------- #

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    sql = "INSERT INTO User(name,email,password,phone,role) VALUES(%s,%s,%s,%s,'user')"

    cursor.execute(sql,(data["name"],data["email"],data["password"],data["phone"]))

    db.commit()

    return jsonify({"message":"User registered"})


@app.route("/login", methods=["POST"])
def login():

    data=request.json

    sql="SELECT * FROM User WHERE email=%s AND password=%s"

    cursor.execute(sql,(data["email"],data["password"]))

    user=cursor.fetchone()

    return jsonify(user if user else {"error":"Invalid login"})


# ---------------- ADMIN ---------------- #

@app.route("/admin", methods=["POST"])
def add_admin():

    data=request.json

    sql="INSERT INTO Admin(name,email,password) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["name"],data["email"],data["password"]))

    db.commit()

    return jsonify({"message":"Admin added"})


@app.route("/admin", methods=["GET"])
def view_admins():

    cursor.execute("SELECT * FROM Admin")

    return jsonify(cursor.fetchall())


# ---------------- DEPARTMENT ---------------- #

@app.route("/department", methods=["POST"])
def add_department():

    data=request.json

    sql="INSERT INTO Department(dept_name,office_location) VALUES(%s,%s)"

    cursor.execute(sql,(data["name"],data["location"]))

    db.commit()

    return jsonify({"message":"Department added"})


@app.route("/department", methods=["GET"])
def view_department():

    cursor.execute("SELECT * FROM Department")

    return jsonify(cursor.fetchall())


# ---------------- CATEGORY ---------------- #

@app.route("/category", methods=["POST"])
def add_category():

    data=request.json

    sql="INSERT INTO Category(category_name,description) VALUES(%s,%s)"

    cursor.execute(sql,(data["name"],data["description"]))

    db.commit()

    return jsonify({"message":"Category added"})


@app.route("/category", methods=["GET"])
def view_category():

    cursor.execute("SELECT * FROM Category")

    return jsonify(cursor.fetchall())


# ---------------- LOCATION ---------------- #

@app.route("/location", methods=["POST"])
def add_location():

    data=request.json

    sql="INSERT INTO Location(location_name,description) VALUES(%s,%s)"

    cursor.execute(sql,(data["name"],data["description"]))

    db.commit()

    return jsonify({"message":"Location added"})


@app.route("/location", methods=["GET"])
def view_location():

    cursor.execute("SELECT * FROM Location")

    return jsonify(cursor.fetchall())


# ---------------- LOST ITEM ---------------- #

@app.route("/lost", methods=["POST"])
def lost_item():

    data=request.json

    sql="""INSERT INTO LostItem(title,description,date_lost,status,user_id,category_id,location_id)
           VALUES(%s,%s,%s,'Lost',%s,%s,%s)"""

    cursor.execute(sql,(data["title"],data["description"],data["date"],data["user_id"],data["category_id"],data["location_id"]))

    db.commit()

    return jsonify({"message":"Lost item reported"})


@app.route("/lost", methods=["GET"])
def view_lost():

    cursor.execute("SELECT * FROM LostItem")

    return jsonify(cursor.fetchall())


# ---------------- FOUND ITEM ---------------- #

@app.route("/found", methods=["POST"])
def found_item():

    data=request.json

    sql="""INSERT INTO FoundItem(title,description,date_found,status,user_id,category_id,location_id)
           VALUES(%s,%s,%s,'Found',%s,%s,%s)"""

    cursor.execute(sql,(data["title"],data["description"],data["date"],data["user_id"],data["category_id"],data["location_id"]))

    db.commit()

    return jsonify({"message":"Found item added"})


@app.route("/found", methods=["GET"])
def view_found():

    cursor.execute("SELECT * FROM FoundItem")

    return jsonify(cursor.fetchall())


# ---------------- IMAGE ---------------- #

@app.route("/image", methods=["POST"])
def add_image():

    data=request.json

    sql="INSERT INTO Image(image_url,upload_date,lost_id,found_id) VALUES(%s,%s,%s,%s)"

    cursor.execute(sql,(data["url"],data["date"],data["lost_id"],data["found_id"]))

    db.commit()

    return jsonify({"message":"Image uploaded"})


# ---------------- CLAIM ---------------- #

@app.route("/claim", methods=["POST"])
def claim():

    data=request.json

    sql="INSERT INTO Claim(user_id,found_id,claim_date,status) VALUES(%s,%s,%s,'Pending')"

    cursor.execute(sql,(data["user_id"],data["found_id"],data["date"]))

    db.commit()

    return jsonify({"message":"Claim submitted"})


@app.route("/claim", methods=["GET"])
def view_claim():

    cursor.execute("SELECT * FROM Claim")

    return jsonify(cursor.fetchall())


# ---------------- RETURN RECORD ---------------- #

@app.route("/return", methods=["POST"])
def return_item():

    data=request.json

    sql="INSERT INTO ReturnRecord(return_date,found_id,claim_id) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["date"],data["found_id"],data["claim_id"]))

    db.commit()

    return jsonify({"message":"Item returned"})


@app.route("/return", methods=["GET"])
def view_return():

    cursor.execute("SELECT * FROM ReturnRecord")

    return jsonify(cursor.fetchall())


# ---------------- NOTIFICATION ---------------- #

@app.route("/notification", methods=["POST"])
def send_notification():

    data=request.json

    sql="INSERT INTO Notification(message,date_sent,user_id) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["message"],data["date"],data["user_id"]))

    db.commit()

    return jsonify({"message":"Notification sent"})


# ---------------- FEEDBACK ---------------- #

@app.route("/feedback", methods=["POST"])
def feedback():

    data=request.json

    sql="INSERT INTO Feedback(user_id,comments,ratings) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["user_id"],data["message"],data["rating"]))

    db.commit()

    return jsonify({"message":"Feedback submitted"})


# ---------------- REPORT ---------------- #

@app.route("/report", methods=["POST"])
def report():

    data=request.json

    sql="INSERT INTO Report(description,date_submitted,user_id) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["description"],data["date"],data["user_id"]))

    db.commit()

    return jsonify({"message":"Report submitted"})


# ---------------- AUDIT LOG ---------------- #

@app.route("/audit", methods=["POST"])
def audit():

    data=request.json

    sql="INSERT INTO AuditLog(action,action_date,admin_id) VALUES(%s,%s,%s)"

    cursor.execute(sql,(data["action"],datetime.now(),data["admin_id"]))

    db.commit()

    return jsonify({"message":"Audit logged"})


# ---------------- RUN SERVER ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
    