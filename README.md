Web Penetration Testing Tool

این ابزار برای انجام تست‌های نفوذ وب طراحی شده است و به شما کمک می‌کند تا آسیب‌پذیری‌های رایج سایت‌ها را شناسایی کنید. از جمله ویژگی‌های این ابزار می‌توان به بررسی آسیب‌پذیری‌های SQL Injection، XSS، اسکن پورت‌ها، بررسی دایرکتوری‌های مخفی و دریافت اطلاعات سرور از Shodan اشاره کرد.

پیش‌نیازها

قبل از استفاده از این ابزار، باید چندین کتابخانه و ابزار را نصب کنید:

1. Python 3


2. Nmap


3. Shodan API Key



نصب کتابخانه‌ها

برای نصب کتابخانه‌های لازم، از دستورات زیر در ترموکس یا سیستم خود استفاده کنید:

```pkg update && pkg upgrade -y```

```pkg install python git nano -y```

```pip install requests bs4 argparse shodan python-nmap```

نصب Nmap

برای نصب Nmap:

```pkg install nmap -y```

دریافت Shodan API Key

برای استفاده از قابلیت‌های Shodan، ابتدا باید در Shodan ثبت‌نام کنید و سپس API Key خود را دریافت کنید.

نحوه استفاده

پس از نصب پیش‌نیازها، می‌توانید ابزار را به‌راحتی از طریق خط فرمان اجرا کنید.

ساختار کلی دستورات

```python pentest_tool.py --target <URL_or_IP> [OPTIONS]```
پارامترها

--target <URL_or_IP>: آدرس سایت یا IP که قصد تست آن را دارید.

--sql: تست SQL Injection.

--xss: تست XSS.

--ports: اسکن پورت‌ها.

--dirs: اسکن دایرکتوری‌های مخفی.

--files: بررسی فایل‌های حساس (مثل robots.txt, .git, و .htaccess).

--shodan: دریافت اطلاعات سرور از Shodan.


مثال‌ها

1. برای تست SQL Injection:



```python pentest_tool.py --target http://example.com --sql```

2. برای تست XSS:



```python pentest_tool.py --target http://example.com --xss```

3. برای اسکن پورت‌ها:



```python pentest_tool.py --target http://example.com --ports```

4. برای اسکن دایرکتوری‌های مخفی:



```python pentest_tool.py --target http://example.com --dirs```

5. برای بررسی فایل‌های حساس:



```python pentest_tool.py --target http://example.com --files```

6. برای دریافت اطلاعات از Shodan:



```python pentest_tool.py --target http://example.com --shodan```

7. برای انجام چندین تست همزمان:



```python pentest_tool.py --target http://example.com --sql --xss --ports --dirs --shodan```

خروجی‌ها

نتایج تست‌ها به‌صورت متنی در ترمینال نمایش داده می‌شوند. به‌عنوان مثال:

SQL Injection: اگر سایت آسیب‌پذیر به SQL Injection باشد، پیام [+] سایت آسیب‌پذیر به SQL Injection است! نمایش داده می‌شود.

XSS: اگر سایت آسیب‌پذیر به XSS باشد، پیام [+] سایت آسیب‌پذیر به XSS است! نمایش داده می‌شود.

اسکن پورت‌ها: لیست پورت‌ها و وضعیت آن‌ها نمایش داده می‌شود.

دایرکتوری‌های مخفی: دایرکتوری‌های مخفی که در سرور پیدا شده‌اند، به کاربر نشان داده می‌شود.

فایل‌های حساس: اگر فایلی مثل robots.txt یا .git در دسترس باشد، پیام پیدا شدن آن‌ها به کاربر نمایش داده می‌شود.

Shodan: اطلاعات مربوط به سرور هدف از طریق Shodan، شامل IP، سازمان و سیستم عامل، نمایش داده می‌شود.


نکات

این ابزار برای استفاده قانونی و اخلاقی طراحی شده است. همیشه با مجوز مناسب از آن استفاده کنید.

از این ابزار برای تست سایت‌ها یا سرورهایی که مالک آن‌ها هستید یا اجازه انجام تست بر روی آن‌ها را دارید، استفاده کنید.

ابزار به‌صورت همزمان از threading برای انجام تست‌ها استفاده می‌کند، بنابراین نتایج تست‌ها به‌سرعت نمایش داده می‌شوند.

