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
        login [slug]: login with this slug
        logout [slug]: logout from the account with this slug""")

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
        lang = input("Message language (ita or en): ")

        group_scraper = FbGroupScraper(link, name, accounts, lang)
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
