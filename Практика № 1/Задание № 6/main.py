from datetime import datetime


now = datetime.now()
print(f"Дата: {now.date()}.")
print(f"Время: {now.time()}.")
print(f"Номер дня недели: {now.weekday()}.")

diff = datetime(2026, 7, 1) - now
print(f"Дней до 1 июля 2026 года: {diff.days}.")
