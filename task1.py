import re

# Log faylı məzmunu
with open('server_logs.txt', 'r') as file:
    logs = file.read()

# Regex ifadəsi
pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS)')

# Nəticələri çıxarmaq
matches = pattern.finditer(logs)

for match in matches:
    print(f"IP: {match.group('ip')}, Tarix: {match.group('date')}, Metod: {match.group('method')}")
