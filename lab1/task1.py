from ping3 import ping
import csv

def RTT(url):
    rtt = ping(url) * 1000
    return(rtt)

hosts = ["www.google.com",
         "www.geeksforgeeks.org",
         "www.imperva.com",
         "www.w3schools.com",
         "stackoverflow.com",
         "sky.pro",
         "yandex.ru",
         "vk.com",
         "www.youtube.com",
         "www.twitch.tv"]

with open("rtt_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "RTT (ms)"])

    for host in hosts:
        rtt = RTT(host)
        if rtt:
            writer.writerow([host, f"{rtt:.2f}"])
        else:
            writer.writerow([host, "Connection failed"])


