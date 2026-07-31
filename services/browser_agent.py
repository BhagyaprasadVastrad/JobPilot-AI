from playwright.sync_api import sync_playwright


class BrowserAgent:

    def start(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto("https://example.com")

            print("Opened browser successfully!")

            input("Press Enter to close browser...")

            browser.close()