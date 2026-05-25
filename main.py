from src import data_loader
from src import calculations

#LEGACY
revenue = calculations.revenue(data_loader.load_sales())

print(revenue)

profit = calculations.profit(revenue, data_loader.load_expenses())

print(profit)

roi = calculations.roi(profit, data_loader.load_expenses())

print(roi)

roas = calculations.roas(data_loader.load_ads())

print(roas)

margin = calculations.margin(profit, revenue)

print(margin)

