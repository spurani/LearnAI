from datetime import datetime as dt
import time

hosts_temp=r"\C:\Users\adhyapakss\PycharmProjects\mod_7_proj\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.live.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")

    else:
        print("Fun hours...")
    time.sleep(5)
