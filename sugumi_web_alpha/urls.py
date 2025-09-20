# hello_django/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from sugumi_web_alpha import views
import yfinance as yf

def get_stock_price(symbol, date):
    """指定されたシンボルと日付の株価を取得する関数"""
    # 昨日の日付を取得
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    # yfinanceで株価データ取得
    df = yf.download(symbol, period="5d", interval="1d")
    print(type(df))
    try:
        price = int(df.loc[yesterday]['Close'][0] * 10) / 10
    except Exception:
        price = None
    return price

def kabu(request):
    symbol = "4755.T"
    price = get_stock_price(symbol, datetime.now())
    if price is None:
        return HttpResponse("株価情報の取得または解析に失敗しました")
    return HttpResponse(f"{price}")

# ↓ New basic view returning "Hello, Fly!" ↓
def hello(request):
    import django
    return HttpResponse(django.get_version())

from django.shortcuts import render
import requests
from django.http import HttpResponse
from datetime import datetime, timedelta

def menu(request):
    return render(request,'menu/index.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("kabu/", kabu, name="kabu"),
    path("hello/", hello, name="hello"),
    path("menu/", menu, name="menu"),
    path('', views.index, name='index'),
]

