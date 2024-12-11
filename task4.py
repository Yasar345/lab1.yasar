import re
import csv
from collections import defaultdict

# Log faylı məzmununu oxumaq
with open('server_logs.txt', 'r') as file:
    logs = file.read()

# Regex ifadəsi (IP ünvanı, tarix və HTTP metodunu çıxarmaq üçün)
pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS).*?" (?P<status>\d{3})'
)

# Uğursuz cəhdləri toplamaq üçün sözlük
failed_attempts = defaultdict(lambda: {"count": 0, "dates": [], "method": None})

# Regex nəticələrini emal etmək
for match in pattern.finditer(logs):
    ip = match.group("ip")
    date = match.group("date")
    method = match.group("method")
    status = match.group("status")
    
    if status == "401":  # Yalnız uğursuz giriş cəhdlərini sayırıq
        failed_attempts[ip]["count"] += 1
        failed_attempts[ip]["dates"].append(date)
        failed_attempts[ip]["method"] = method

# CSV faylına yazmaq
with open('log_analysis.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Sütun başlıqları
    writer.writerow(["IP ünvanı", "Tarix", "HTTP metodu", "Uğursuz cəhdlər"])
    
    for ip, details in failed_attempts.items():
        # Bütün tarixləri vergüllə birləşdiririk
        dates = "; ".join(details["dates"])
        method = details["method"]
        count = details["count"]
        writer.writerow([ip, dates, method, count])

print(f"{len(failed_attempts)} IP ünvanı 'log_analysis.csv' faylında saxlanıldı.")
