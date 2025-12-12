# Gym Membership Management System

A simple Python + MySQL based application used to manage gym members, track payments, and monitor subscription validity.  
This project supports full CRUD operations and includes an automatic alert system for upcoming membership expiries.

---

## 🚀 Features

### 1. Member Management
- Add new members  
- Store phone number, start date, and subscription duration  
- Update membership by extending validity  
- Delete member records  
- View complete member list  

### 2. Subscription Validity Check
- Check if a member's subscription is active or expired  
- Automatically calculate end date based on subscription months  

### 3. Auto Expiry Alert
- Shows members whose plans will expire within the next **3 days**  
- Helps the gym admin remind customers for renewal  

### 4. Payment Management
- Add payment records  
- Store payment date and amount  
- Link payments to corresponding members  
- View full payment history  

---

## 🗂️ Database Structure (MySQL)

### **members Table**
| Column      | Type        |
|-------------|-------------|
| member_id   | INT (PK)    |
| name        | VARCHAR(50) |
| phone       | VARCHAR(20) |
| start_date  | DATE        |
| end_date    | DATE        |

### **payments Table**
| Column      | Type        |
|-------------|-------------|
| pay_id      | INT (PK)    |
| member_id   | INT (FK)    |
| amount      | INT         |
| pay_date    | DATE        |

---

## 🛠️ Technologies Used
- **Python 3**
- **MySQL**
- **mysql-connector-python** library

Install connector:
```bash
pip install mysql-connector-python
