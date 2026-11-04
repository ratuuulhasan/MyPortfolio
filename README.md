# 🚀 Premium Dynamic Portfolio Website

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-3.15-red?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A fully dynamic, highly customizable, and premium portfolio website built with **Django**, **PostgreSQL**, and **Bootstrap**. It features a custom-built Admin Panel, allowing you to update your entire website (Projects, Skills, Blog, Certifications, Experience, etc.) without touching a single line of code.

---

## 📑 Table of Contents
1. [Key Features](#-key-features)
2. [Tech Stack](#-tech-stack)
3. [Project Structure](#-project-structure)
4. [Getting Started (Local Setup)](#-getting-started-local-setup)
5. [Environment Variables](#-environment-variables)
6. [How to Use the Admin Panel](#-how-to-use-the-admin-panel)
7. [Deployment Guide](#-deployment-guide)
8. [License](#-license)

---

## ✨ Key Features

### 🌐 Public Site (Frontend)
- **Fully Responsive:** Perfectly optimized for Mobile, Tablet, and Desktop.
- **Dark / Light Mode:** Toggle between themes; preference is saved in `localStorage`.
- **Premium UI/UX:** Glassmorphism effects, smooth scrolling, and 3D tilt effects on cards.
- **AOS Animations:** Beautiful on-scroll animations (Fade-up, zoom-in, etc.).
- **Dynamic Sections:** Hero (with Typing Effect), About, Education, Experience, Skills (with animated progress bars), Projects, Certifications, Blog, and Contact.
- **Blog System:** Read full articles, with a comment section for visitors.
- **Contact Form:** Visitors can send messages directly to your database and email.
- **SEO & OpenGraph:** Optimized meta tags for social media sharing.

### 🛡️ Admin Panel (Backend)
- **Custom Dashboard:** Beautiful, intuitive UI to manage everything.
- **CRUD Operations:** Create, Read, Update, and Delete Skills, Projects, Education, Experience, Certifications, Social Links, and Blog Posts.
- **Message Inbox:** Read and manage messages sent by visitors via the Contact form.
- **Site Settings:** Update Site Title, Meta Description, Logo, Favicon, and toggle section visibility.
- **Dynamic Theme Color:** Change the primary color of the website directly from the dashboard.
- **Password Management:** Change your admin password securely.
- **Secret Admin Access:** A hidden `❤️` icon in the footer acts as a secret gateway to the admin login! (No one else will know).

---

## 💻 Tech Stack

- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL (Production), SQLite (Local/Dev)
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla), AOS (Animate On Scroll)
- **Deployment Ready:** Configured for platforms like Render, Railway, or VPS.

---

## 📂 Project Structure

```text
portfolio_project/
│
├── manage.py
├── requirements.txt
├── .env                  # (Secret environment variables)
├── README.md
│
├── portfolio_project/    # Main Django Configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolio/            # Main App (Pages & Admin Panel)
│   ├── models.py         # Database schemas
│   ├── views.py          # Business logic (Public & Admin)
│   ├── forms.py          # Django Forms with Bootstrap styling
│   ├── urls.py           # Route handling
│   └── context_processors.py # Global variables (Profile, Settings)
│
├── static/               # Static Assets
│   ├── css/style.css     # Custom Premium CSS
│   └── js/main.js        # Animations, Dark Mode, Slider logic
│
└── templates/            # HTML Templates
    ├── base.html         # Master layout
    ├── public/           # Frontend pages (home, blog_detail, contact)
    ├── admin_panel/      # Custom Admin Panel Templates
    └── partials/         # Navbar, Footer