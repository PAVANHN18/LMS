
# Leave Management System

A simple **Leave Management System** built with **Python** and **SQLite**.  
Supports adding employees, applying for leave, approving/rejecting leave, and checking leave balance. Currently implemented as a **CLI-based system**, but easily extendable to a **frontend + API** system.  

---

## **Table of Contents**
1. [Setup Steps](#setup-steps)  
2. [How to Use](#how-to-use)  
3. [Assumptions](#assumptions)  
4. [Edge Cases Handled](#edge-cases-handled)  
5. [Potential Improvements](#potential-improvements)  

---

## **Setup Steps**

1. **Clone or download the project**  
   ```bash
   git clone https://github.com/PAVANHN18/LMS.git
   cd LeaveManagementSystem
   ```

2. **Install Python (if not already installed)**  
   Python 3.8+ recommended

3. **Install required dependencies**  
   - SQLite is part of Python standard library, no extra install needed  
   - Optional: For API integration, install FastAPI:
     ```bash
     pip install fastapi uvicorn pydantic
     ```

4. **Run the CLI application**  
   ```bash
   python leave_management.py
   ```
   - This will create the database file `leave_management.db` automatically if it doesn’t exist.

5. **Database**  
   - Two tables are created:
     - `employees` → stores employee information and leave balance  
     - `leave_requests` → stores leave requests, their dates, reasons, and status  

---

## **How to Use**

1. **Add Employee**  
   - Enter name, email, department, and joining date (YYYY-MM-DD)  
   - Default leave balance: 20 days  

2. **Apply for Leave**  
   - Enter employee ID, start & end date, and reason  
   - System validates leave balance, overlapping leaves, joining date, and max leave duration  

3. **Approve/Reject Leave**  
   - Enter leave request ID and status (Approved/Rejected)  
   - Leave balance is deducted only if approved  

4. **Check Leave Balance**  
   - Enter employee ID to see remaining leave days  

---

## **Assumptions**

- Default leave balance is **20 days per employee**.  
- Maximum leave duration per request: **30 days**.  
- Leaves cannot be applied for **past dates**.  
- Joining date in future is allowed but flagged.  
- Email is **unique for each employee**.  
- Only **Pending leave requests** can be approved or rejected.  

---

## **Edge Cases Handled**

- Invalid date formats (YYYY-MM-DD only)  
- Leave end date before start date  
- Applying leave before joining date  
- Leave balance exceeded  
- Overlapping leave requests (Pending/Approved)  
- Leave requests exceeding maximum duration  
- Duplicate employee email  
- Non-existent employee or leave request IDs  

---

## **Potential Improvements**

- **Frontend Integration**: Convert CLI into **HTML + JS frontend** calling API endpoints  
- **API Layer**: Use **FastAPI** for RESTful endpoints  
- **Authentication & Roles**: Add admin and employee login  
- **Notifications**: Email/SMS notifications for leave approvals  
- **Audit Logs**: Track all actions for accountability  
- **Reporting**: Monthly leave summary per employee  
- **Database Upgrade**: Move from SQLite to MySQL/PostgreSQL for multi-user deployments  
