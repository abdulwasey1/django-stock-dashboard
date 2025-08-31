📈 Stock Dashboard (Django + yFinance + Chart.js)

A simple Django web application to visualize stock market data.
Users can select a stock from a dropdown and view:

📊 Interactive line chart of historical prices (1 year by default, powered by Chart.js)

📑 Key financial metrics (Market Cap, P/E Ratio, 52-Week High/Low, Volume)

🔄 Automatic updates when a different stock is selected

🚀 Features

Choose from popular stocks (AAPL, MSFT, GOOG, AMZN, TSLA)

Fetch live & historical data using yFinance

Render stock prices dynamically with Chart.js

Display financial metrics in a simple table

🛠️ Tech Stack

Backend: Django, yFinance

Frontend: HTML, Django Templates, Chart.js (via CDN)

Other: Pandas (data handling), SQLite (default DB), Virtual Environment for dependencies

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/yourusername/stock-dashboard.git
cd stock-dashboard

2. Create Virtual Environment
python -m venv venv


Activate it:

Windows:
venv\Scripts\activate


Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install django yfinance matplotlib pandas

4. Run Migrations
python manage.py migrate

5. Start Development Server
python manage.py runserver


Visit: http://127.0.0.1:8000/
