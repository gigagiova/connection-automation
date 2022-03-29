import re

from FB import FbAccount
from FbGroupScraper import FbGroupScraper
from regex import group_regex

accounts = {}
print("Commands \ngroup: scrape a fb group\nquit: quit execution\nmessage [from] [to]\naccounts\nlogin\nlogout")

while True:
    command = input()

    if command == "quit":
        break
    elif command == "group":
        link = input("Write group link: ")

        # check syntax of the link
        if not group_regex.match(link):
            print("group link seems broken")
            continue

        name = input("Write group name: ")

        group_scraper = FbGroupScraper(link, name, accounts)
        group_scraper.start()

    elif re.compile(r'login .+').match(command):
        slug = command.split(' ')[1]
        accounts[slug] = FbAccount(slug)
    elif re.compile(r'logout .+').match(command):
        slug = command.split(' ')[1]
        accounts.pop(slug)
    elif command == "accounts":
        print(accounts)
    elif re.compile(r'message .+ .+').match(command):
        slug = command.split(' ')[1]
        receiver = command.split(' ')[2]
        if accounts[slug] is None:
            print("Login before sending a message")
            break
        print(accounts[slug].send_message(receiver))
    else:
        print("Command not recognized")
