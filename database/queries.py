from database.database import connect_db


# REGISTER
def add_user(name, email, password):

    db = connect_db()

    cursor = db.cursor()

    sql = """
    INSERT INTO users(name, email, password)
    VALUES(%s, %s, %s)
    """

    values = (name, email, password)

    cursor.execute(sql, values)

    db.commit()

    cursor.close()
    db.close()

    return "✅ User registered successfully"


# LOGIN
def get_user(email, password):

    db = connect_db()

    cursor = db.cursor(dictionary=True)

    sql = """
    SELECT * FROM users
    WHERE email = %s
    AND password = %s
    """

    values = (email, password)

    print("EMAIL:", email)
    print("PASSWORD:", password)

    cursor.execute(sql, values)

    user = cursor.fetchone()

    print("USER:", user)

    cursor.close()
    db.close()

    return user

INSERT_RESERVATION = """
INSERT INTO reservations
(
    full_name,
    email,
    hotel_name,
    check_in,
    check_out,
    guests
)
VALUES
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
"""
