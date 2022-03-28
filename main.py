from FB import login, scrape_group
from regex import group_regex

login()
print("Commands \ngroup: scrape a fb group\nquit: quit execution")

while True:
    command = input()

    if command == "quit": break
    
    elif command == "group":
        link = input("Write group link")

        # check syntax of the link
        if not group_regex.match(link):
            print("group link seems broken")
            continue

        name = input("Write group name")

        scrape_group(link, name)
