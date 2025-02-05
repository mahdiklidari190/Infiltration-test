import requests
import argparse
import shodan
import nmap
import threading
from bs4 import BeautifulSoup

# تنظیمات ابزار
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"

# اسکن پورت‌ها با Nmap
def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-65535')
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port} is {nm[host][proto][port]['state']}")

# بررسی SQL Injection
def check_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url + payload)
    if "sql" in response.text.lower():
        print("[+] سایت آسیب‌پذیر به SQL Injection است!")
    else:
        print("[-] سایت امن به نظر می‌رسد.")

# بررسی XSS
def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        print("[+] سایت آسیب‌پذیر به XSS است!")
    else:
        print("[-] سایت امن به نظر می‌رسد.")

# اسکن دایرکتوری‌های مخفی
def scan_directories(target, wordlist="wordlist.txt"):
    with open(wordlist, "r") as f:
        paths = f.read().splitlines()
    for path in paths:
        url = f"{target}/{path}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] پیدا شد: {url}")

# بررسی فایل‌های حساس
def check_sensitive_files(target):
    sensitive_files = ["robots.txt", ".git", ".htaccess"]
    for file in sensitive_files:
        url = f"{target}/{file}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] پیدا شد: {url}")

# دریافت اطلاعات سرور با Shodan
def get_shodan_info(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        info = api.host(ip)
        print(f"IP: {info['ip_str']}")
        print(f"سازمان: {info.get('org', 'N/A')}")
        print(f"سیستم عامل: {info.get('os', 'N/A')}")
    except shodan.APIError as e:
        print(f"خطا در Shodan: {e}")

# دریافت ورودی‌ها از کاربر
def main():
    parser = argparse.ArgumentParser(description="ابزار تست نفوذ وب")
    parser.add_argument("--target", type=str, help="آدرس سایت یا IP")
    parser.add_argument("--sql", action="store_true", help="تست SQL Injection")
    parser.add_argument("--xss", action="store_true", help="تست XSS")
    parser.add_argument("--ports", action="store_true", help="اسکن پورت‌ها")
    parser.add_argument("--dirs", action="store_true", help="اسکن دایرکتوری‌های مخفی")
    parser.add_argument("--files", action="store_true", help="بررسی فایل‌های حساس")
    parser.add_argument("--shodan", action="store_true", help="دریافت اطلاعات سرور از Shodan")

    args = parser.parse_args()

    if args.target:
        if args.ports:
            threading.Thread(target=scan_ports, args=(args.target,)).start()
        if args.sql:
            threading.Thread(target=check_sql_injection, args=(args.target,)).start()
        if args.xss:
            threading.Thread(target=check_xss, args=(args.target,)).start()
        if args.dirs:
            threading.Thread(target=scan_directories, args=(args.target,)).start()
        if args.files:
            threading.Thread(target=check_sensitive_files, args=(args.target,)).start()
        if args.shodan:
            threading.Thread(target=get_shodan_info, args=(args.target,)).start()

if __name__ == "__main__":
    main()
