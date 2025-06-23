🛒 Flipkart Product Scraper

This project is a complete end-to-end system that:

- 🔍 Scrapes product details from Flipkart using Python
- 💾 Stores data in a MySQL database
- 🌐 Exposes data through a Flask REST API
- 🖥️ Displays products in a searchable, paginated web interface
- 📤 Allows export of product data as CSV
- 🕒 Auto-scrapes data daily using Windows Task Scheduler

---
![image](https://github.com/user-attachments/assets/b47faf0d-abf7-4861-ab46-9733769e08df)

Project Structure
flipkart-scraper/
├── api.py # Flask API to expose and display data
├── scraper.py # Scraper script using BeautifulSoup
├── db_config.py # MySQL DB connection utility
├── templates/
│ └── products.html # HTML template for /view route
├── run_scraper.bat # Batch file for Task Scheduler
├── venv/ # Virtual environment (auto-generated)

---

🛠️ Features

| Feature                | Description                            |
|------------------------|----------------------------------------|
| 🔎 Scraping            | Scrapes product name, price, and rating from Flipkart |
| 🗃️ MySQL Integration    | Stores all data in a structured database |
| 🔌 REST API            | Access product data in JSON via `/products` |
| 🌐 Web UI              | View/search data at `/view` route     |
| 📤 CSV Export          | Export data with `/export` route      |
| 🔁 Pagination          | Web interface supports paging         |
| 🕒 Auto-Schedule       | Scraper runs daily via Task Scheduler |

---

 Technologies Used

- Python 3.x
- BeautifulSoup
- Requests
- Flask
- MySQL + mysql-connector-python
- HTML + Bootstrap 5

Setup Instructions

1️ Clone & Navigate

bash
git clone https://github.com/your-username/flipkart-scraper.git
cd flipkart-scraper
2️ Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate
3️ Install Requirements
bash
pip install flask mysql-connector-python beautifulsoup4 requests
4️ Set Up MySQL
sql
CREATE DATABASE flipkart_data;

USE flipkart_data;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price VARCHAR(50),
    rating VARCHAR(20)
);
🛠️ Update your db_config.py with your MySQL password.
________________________________________
 Run the App
Run Scraper:
bash
python scraper.py
Run API Server:
bash
python api.py
Visit:
http://127.0.0.1:5000/view
________________________________________
Export CSV
URL	Action
/export	Download full CSV
/export?q=Samsung	Filtered CSV Export
________________________________________
Automate with Task Scheduler (Windows)
1.	Create a file: run_scraper.bat
2.	Add:
@echo off
cd C:\path\to\flipkart-scraper
call venv\Scripts\activate.bat
venv\Scripts\python.exe scraper.py
3.	Use Task Scheduler → Create Basic Task → Run daily.
________________________________________
Screenshots
Add screenshots of /view, search, and CSV download
________________________________________
Status
Project: Complete and Production-Ready
________________________________________
📄 License
MIT License – free to use, modify, and share.
What You Can Do Next:
- Add screenshots to the **screenshots** folder and link in README.
- Upload this to GitHub for portfolio.
- Use it in your resume with:  
  “Built a full-stack Flipkart Scraper with search, export, pagination, and daily auto-scheduling.”

Want me to help with a GitHub-ready version (including `.gitignore`, `requirements.txt`, etc.)?

