# 📚 Library Management System

## 📖 Project Overview

The **Library Management System** is a web application built using **Django** and **MySQL**. It is designed to streamline library operations by allowing **admins** to manage books (CRUD operations) and **students** to view available books.

---

## 🚀 Features

### **Admin Panel**
- ✅ **Admin Signup/Login**: Admins can create accounts and log in to manage the system.
- ✅ **Add, Update, Delete Books**: Full control over book inventory management.
- ✅ **View All Books**: Access a complete list of books in the library.

### **Student Panel**
- ✅ **View All Available Books**: Students can browse the catalog of available books without requiring authentication.

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript (Basic UI)

## 🚀 Technologies & Versions Used
| **Technology** | **Version** |
|--------------|------------|
| Python       | 3.10+      |
| Django       | 4.2+       |
| MySQL        | 8.0+       |
| HTML / CSS / JS | Any version |



---

## ⚙️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusernamelibrary-management-system.git

cd library-management-system
```




### **2️⃣ Create a Virtual Environment**
```sh
python -m venv env

source env/bin/activate  # For Mac/Linux

env\Scripts\activate     # For Windows
```


## 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt


```

## 4️⃣ Configure Database (MySQL)

Open settings.py and update the DATABASES section:
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```


Run migrations:
```sh
python manage.py makemigrations
python manage.py migrate

```

## 5️⃣ Create Superuser (Admin Login)

```sh
python manage.py createsuperuser

```
👤 Enter details: username, email, password.


## 6️⃣ Run the Development Server
```sh
python manage.py runserver

```
Now, visit http://127.0.0.1:8000 in your browser.



## 📜 API Reference

### Admin APIs

#### Admin Signup

```http
  POST /admin/signup/

```
Request Body:
```
{
  "email": "admin@example.com",
  "password": "securepassword"
}
```

#### Admin Login

```
POST /admin/login/

```
Request Body:
```
{
  "email": "admin@example.com",
  "password": "securepassword"
}

```

### Book APIs

#### Get all books

```
GET /books/

```
Request Body:
```
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "isbn": "123-456-789",
    "published_date": "2024-01-01"
  }
]

```
#### Get a specific book

```
GET /books/${id}/

```
#### Add a book

```
POST /books/

```
Request Body:
```
{
  "title": "New Book",
  "author": "Author Name",
  "isbn": "987-654-321",
  "published_date": "2024-02-01"
}

```

#### Update a book

```
PUT /books/${id}/

```
Request Body:
```
{
  "title": "Updated Book Title",
  "author": "Updated Author",
  "isbn": "111-222-333",
  "published_date": "2024-03-01"
}

```

#### Delete a book
```
DELETE /books/${id}/

```

## Running Tests

To run tests, run the following command
#### Run Django unit tests:
```bash
  python manage.py test

```


## Acknowledgements


📌 Assumptions Made

- Admins have full CRUD permissions, but students can only view books.

- User authentication is session-based (Django Authentication System).

- The frontend is minimal, mainly using HTML, CSS, and JavaScript.

- MySQL is the primary database, but it can be switched to SQLite for quick testing.

  
## 🛠 Contribution Guide

Contributions are always welcome!


Want to improve this project? Follow these steps:

- Fork the repository

- Create a feature branch (git checkout -b feature-branch)

- Commit your changes (git commit -m "Added new feature")

- Push to GitHub (git push origin feature-branch)

- Create a Pull Request



