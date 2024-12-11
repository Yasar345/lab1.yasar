import re
import json
from collections import Counter

# Log faylını oxumaq
try:
    with open('server_logs.txt', 'r') as file:
        logs = file.read()
except FileNotFoundError:
    print("server_logs.txt faylı tapılmadı.")
    exit()

# Regex ifadəsi (IP ünvanı və status kodunu çıxarmaq üçün)
pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(?:GET|POST|PUT|DELETE|HEAD|OPTIONS).*?" (?P<status>\d{3})')

# Uğursuz giriş cəhdlərini saymaq (status kodu 401 olanlar)
failed_attempts = Counter(match.group('ip') for match in pattern.finditer(logs) if match.group('status') == '401')

# JSON formatında saxlamaq üçün məlumatı hazırlamaq
failed_logins = {ip: count for ip, count in failed_attempts.items()}

# JSON faylında saxlamaq
with open('failed_logins.json', 'w') as json_file:
    json.dump(failed_logins, json_file, indent=4)

print(f"{len(failed_logins)} IP ünvanı 'failed_logins.json' faylında saxlanıldı.")
