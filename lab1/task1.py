import csv

from ping3 import ping


hosts = ["www.google.com",
         "www.geeksforgeeks.org",
         "www.imperva.com",
         "www.mail.ru",
         "stackoverflow.com",
         "sky.pro",
         "yandex.ru",
         "vk.com",
         "www.youtube.com",
         "www.twitch.tv"]

def RTT(url):
    return ping(url) * 1000

with open("rtt_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "RTT (ms)"])

    for host in hosts:
        rtt = RTT(host)
        if rtt:
            writer.writerow([host, f"{rtt:.2f}"])
        else:
            writer.writerow([host, "Connection failed"])


