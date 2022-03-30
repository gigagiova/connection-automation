from settings import SCROLLS


class FbGroupScraper:

    def __init__(self, url, group_name, accounts, lang):
        self.name = group_name
        self.url = url
        self.previous_batches = set()
        self.accounts = list(accounts.values())
        self.lang = lang

    def start(self):
        """A method for scrolling the page."""

        account_index = 0

        while True:

            # current account
            acc = account_index % len(self.accounts)

            # scrapes the next batch, always using the same profile for simplicity
            output = self.accounts[0].scrape_batch(self.url, self.previous_batches)

            # actually sends the messages
            self.accounts[acc].send_batch(output[0], f"fb_connection_{self.lang}", self.name)
            self.previous_batches.update(output[0])

            if output[1]:
                # we have scrolled all the way down
                break

            # updates round robin index
            account_index += 1
