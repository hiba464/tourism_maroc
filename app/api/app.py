from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from dotenv import load_dotenv
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

sys.path.append(project_root)

from database.database import connect_db
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("Mail_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("Mail_PASSWORD")

mail = Mail(app)

@app.route("/")
def home():
    return "Flask API Working"


# REGISTER
@app.route("/register", methods=["POST"])
def register():

    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(%s,%s,%s)
        """,
        (
            data["name"],
            data["email"],
            data["password"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "success": True
    })


# LOGIN
@app.route("/login", methods=["POST"])
def login():

    data = request.json

    conn = connect_db()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email=%s
        AND password=%s
        """,
        (
            data["email"],
            data["password"]
        )
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
     return jsonify({
        "success": True,
        "role": user["role"]
    })


# HOTELS
@app.route("/hotels")
def hotels():

    conn = connect_db()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM hotels
        """
    )

    hotels = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(hotels)


@app.route("/reserve", methods=["POST"])
def reserve():

    data = request.json

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT price
        FROM hotels
        WHERE name=%s
        """,
        (data["hotel_name"],)
    )

    hotel = cursor.fetchone()

    if not hotel:

        return jsonify({
            "success":False,
            "message":"Hotel Not Found"
        })

    from datetime import datetime

    check_in = datetime.strptime(
        data["check_in"],
        "%Y-%m-%d"
    )

    check_out = datetime.strptime(
        data["check_out"],
        "%Y-%m-%d"
    )

    nights = (
        check_out - check_in
    ).days

    total_price = (
        float(hotel["price"])
        * nights
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reservations
        (
            full_name,
            email,
            hotel_name,
            check_in,
            check_out,
            guests,
            total_price
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            data["full_name"],
            data["email"],
            data["hotel_name"],
            data["check_in"],
            data["check_out"],
            data["guests"],
            total_price
        )
    )
    print("INSERT OK")
    conn.commit()
    print("COMMIT OK")
    cursor.close()
    conn.close()
    msg = Message(
    subject="Reservation Confirmed - Tourism Maroc",
    sender=app.config["MAIL_USERNAME"],
    recipients=[data["email"]]
     )

    msg.body = f"""
Hello {data['full_name']},

Your reservation has been confirmed.

Hotel: {data['hotel_name']}
Check-in: {data['check_in']}
Check-out: {data['check_out']}
Guests: {data['guests']}

Total Price: {total_price} MAD

Thank you for choosing Tourism Maroc.
"""
    print("SENDING EMAIL...")
    mail.send(msg)
    print("EMAIL SENT")


    return jsonify({

        "success":True,

         "message":
    f"Confirmation email sent to {data['email']}",

        "hotel":
        data["hotel_name"],

        "customer":
        data["full_name"],

        "check_in":
        data["check_in"],

        "check_out":
        data["check_out"],

        "guests":
        data["guests"],

        "total":
        total_price

    })

# reviews
@app.route("/review", methods=["POST"])
def review():
    print("REVIEW RECEIVED")
    print(request.json)
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reviews
        (name,hotel_name,rating,comment)
        VALUES(%s,%s,%s,%s)
        """,
        (
            data["name"],
            data["hotel_name"],
            data["rating"],
            data["comment"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "success":True,
        "message":"Review Added"
    })


@app.route("/reviews")
def reviews():

    conn = connect_db()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM reviews
        ORDER BY id DESC
        """
    )

    reviews = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(reviews)


#admin/reservations
@app.route("/admin/reservations")
def admin_reservations():

    conn = connect_db()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM reservations
        ORDER BY id DESC
        """
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)



#/admin/stats
@app.route("/admin/stats")
def admin_stats():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reservations")
    reservations = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reviews")
    reviews = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM hotels")
    hotels = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({
        "users": users,
        "reservations": reservations,
        "reviews": reviews,
        "hotels": hotels
    })





@app.route("/admin/delete_reservation/<int:id>", methods=["DELETE"])
def delete_reservation(id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM reservations
        WHERE id=%s
        """,
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "success": True
    })

@app.route("/favorite", methods=["POST"])
def favorite():
    
    
    data = request.json

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO favorites
        (user_email, hotel_name)
        VALUES(%s,%s)
        """,
        (
            data["user_email"],
            data["hotel_name"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "success": True
    })




if __name__ == "_main_":
    port = int(os.environ.get("PORT", 8080))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )