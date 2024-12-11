import re
from collections import Counter

# Log faylını oxumaq
try:
    with open('server_logs.txt', 'r') as file:
        logs = file.read()
except FileNotFoundError:
    print("server_logs.txt faylı tapılmadı.")
    exit()

# Regex ifadəsi (IP ünvanı və status kodunu çıxarmaq üçün)
pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(?:GET|POST|PUT|DELETE|HEAD|OPTIONS) .*?" (?P<status>\d{3})')

# Uğursuz giriş cəhdlərini saymaq (status kodu 401 olanlar)
failed_attempts = Counter(match.group('ip') for match in pattern.finditer(logs) if match.group('status') == '401')

# Nəticələri TXT faylına saxlamaq
with open('log_analysis.txt ', 'w') as txt_file:
    for ip, count in failed_attempts.items():
        txt_file.write(f"{ip}: {count}\n")

print(f"{len(failed_attempts)} IP ünvanı 'log_analysis.txt ' faylında saxlanıldı.")
