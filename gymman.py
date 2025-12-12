import mysql.connector
from datetime import datetime, timedelta

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="your_database_name"
)

cur = con.cursor()

def add_member():
    mid = int(input("Member ID: "))
    name = input("Name: ")
    phone = input("Phone: ")
    start = input("Start date (YYYY-MM-DD): ")
    months = int(input("Subscription (months): "))

    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = start_date + timedelta(days=30 * months)

    cur.execute("INSERT INTO members VALUES (%s,%s,%s,%s,%s)",
                (mid, name, phone, start_date.date(), end_date.date()))
    con.commit()
    print("Member Added\n")

def view_members():
    cur.execute("SELECT * FROM members")
    for row in cur.fetchall():
        print(row)
    print()

def update_member():
    mid = int(input("Enter Member ID: "))
    months = int(input("Extend by (months): "))

    cur.execute("SELECT end_date FROM members WHERE member_id=%s", (mid,))
    end_date = cur.fetchone()[0]

    new_end = end_date + timedelta(days=30 * months)

    cur.execute("UPDATE members SET end_date=%s WHERE member_id=%s",
                (new_end, mid))
    con.commit()
    print("Membership Extended\n")

def delete_member():
    mid = int(input("Enter Member ID to delete: "))
    cur.execute("DELETE FROM members WHERE member_id=%s", (mid,))
    con.commit()
    print("Member Deleted\n")

def add_payment():
    pid = int(input("Payment ID: "))
    mid = int(input("Member ID: "))
    amount = int(input("Amount: "))
    date = input("Payment date (YYYY-MM-DD): ")

    cur.execute("INSERT INTO payments VALUES (%s,%s,%s,%s)",
                (pid, mid, amount, date))
    con.commit()
    print("Payment Recorded\n")

def view_payments():
    cur.execute("SELECT * FROM payments")
    for row in cur.fetchall():
        print(row)
    print()

def check_validity():
    mid = int(input("Enter Member ID: "))
    cur.execute("SELECT name, end_date FROM members WHERE member_id=%s", (mid,))
    data = cur.fetchone()

    name, end_date = data
    today = datetime.today().date()

    if today <= end_date:
        print(f"{name} membership valid till {end_date}")
    else:
        print(f"{name} membership expired on {end_date}")
    print()

def expiry_alert():
    today = datetime.today().date()
    alert_date = today + timedelta(days=3)

    cur.execute("SELECT member_id, name, end_date FROM members")
    result = cur.fetchall()

    print("\nEXPIRY ALERT (within 3 days):")
    for m in result:
        mid, name, end = m
        if today <= end <= alert_date:
            print(f"{name} → Expiring on {end}")
    print()

while True:
    print("1. Add Member")
    print("2. View Members")
    print("3. Update Membership")
    print("4. Delete Member")
    print("5. Add Payment")
    print("6. View Payments")
    print("7. Check Membership Validity")
    print("8. Expiry Alert")
    print("9. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_member()
    elif ch == 2:
        view_members()
    elif ch == 3:
        update_member()
    elif ch == 4:
        delete_member()
    elif ch == 5:
        add_payment()
    elif ch == 6:
        view_payments()
    elif ch == 7:
        check_validity()
    elif ch == 8:
        expiry_alert()
    elif ch == 9:
        break
    else:
        print("Invalid Choice\n")
