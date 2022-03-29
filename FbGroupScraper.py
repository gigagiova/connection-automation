from settings import SCROLLS


class FbGroupScraper:

    def __init__(self, url, group_name, accounts):
        self.name = group_name
        self.url = url
        self.previous_batches = set()
        self.accounts = list(accounts.values())

    def start(self):
        """A method for scrolling the page."""

        account_index = 0
        # cumulative scroll

        while True:

            # current account
            acc = account_index % len(self.accounts)

            if account_index < len(self.accounts):
                self.accounts[acc].scroll_down(acc * SCROLLS)
            else:
                self.accounts[acc].scroll_down((len(self.accounts) - 1) * SCROLLS)

            output = self.accounts[acc].scrape_batch(
                self.name,
                self.url,
                self.previous_batches
            )

            account_index += 1
            self.previous_batches.update(output[0])

            if output[1]:
                # we have scrolled all the way down
                break
