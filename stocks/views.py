from django.shortcuts import render
import yfinance as yf
import pandas as pd

def home(request):
    stocks_list = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']  # dropdown options
    selected_stock = request.GET.get('stock', 'AAPL')  # default is AAPL

    # Fetch data from yfinance
    ticker = yf.Ticker(selected_stock)
    hist = ticker.history(period="2mo")  # Data period

    # Prepare data for Chart.js
    dates = hist.index.strftime('%Y-%m-%d').tolist()
    prices = hist['Close'].tolist()

    # Financial info
    info = ticker.info
    metrics = {
        'Market Capitalization': info.get('marketCap'),
        'P/E Ratio': info.get('trailingPE'),
        '52 Week High': info.get('fiftyTwoWeekHigh'),
        '52 Week Low': info.get('fiftyTwoWeekLow'),
        'Volume': info.get('volume')
    }

    return render(request, 'stocks/home.html', {
        'stocks_list': stocks_list,
        'selected_stock': selected_stock,
        'dates': dates,
        'prices': prices,
        'metrics': metrics
    })
