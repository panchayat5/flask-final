from turtle import width
from flask import Blueprint
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

second1 = Blueprint("second1", __name__, static_folder="static", template_folder="templates")

pd.set_option('display.max_columns', None)

sales = pd.read_csv('static/csv/supermarket_sales.csv')

def TotalSales_WRT_Month(filename):
    Total_Sales = sales.groupby('Month').Total.sum()
    months = range(1,4)
        
    plt.figure(figsize=(10,7))
    colors = ['#e01616', '#612f75', '#db3d7a']
        
    plt.bar(months, Total_Sales, color = colors)
        
    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
    labels = ['Jaunuary', 'February', 'March']
    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)
        
    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
    plt.show()
    export_picture(filename)

def export_picture(filename):
    plt.legend()
    plt.savefig(filename)
    plt.close

TotalSales_WRT_Month("Month")

WIDTH: 210
HEIGHT: 297
pdf = FPDF()
pdf.add_page()
pdf.image("Month.png", 5, 20, WIDTH /2 -5)
pdf.output("analysis.pdf",'F')

