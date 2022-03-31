import json
import re

from FB import FbAccount
from FbGroupScraper import FbGroupScraper
from regex import group_regex

accounts = {}
print("""Commands
        group: scrape a fb group
        quit: quit execution
        message [from] [to]
        accounts: show all currently logged in accounts
        login [space separated slugs]: login with this slug
        logout [slug]: logout from the account with this slug""")

while True:
    command = input()

    if command == "quit":
        break
    elif re.compile(r'group .+').match(command):
        # fetch group data from JSON file
        file = open("persistent/groups.json", "r")
        # fetch this group from file
        group = json.loads(file.read())[command.split(' ')[1]]
        file.close()

        group_scraper = FbGroupScraper(group["link"], group["name"], accounts, group["lang"])
        group_scraper.start()

    elif re.compile(r'login .+').match(command):
        for slug in command.split(' ')[1:]:
            # iterates through all provided account slugs
            accounts[slug] = FbAccount(slug)
        print("login completed")
    elif re.compile(r'logout .+').match(command):
        slug = command.split(' ')[1]
        accounts.pop(slug)
    elif command == "accounts":
        print(accounts)
    elif re.compile(r'message .+ .+').match(command):

        # extracts sender and receiver
        slug = command.split(' ')[1]
        receiver = command.split(' ')[2]

        if accounts[slug] is None:
            print("Login before sending a message")
            break

        message = input("Write message: ")
        print(accounts[slug].send_message(receiver, message))
    else:
        print("Command not recognized")
