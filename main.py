
from FB import login
from FbGroupScraper import FbGroupScraper
from regex import group_regex

login()
print("Commands \ngroup: scrape a fb group\nquit: quit execution")

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

        group_scraper = FbGroupScraper(link, name)
        group_scraper.start()

