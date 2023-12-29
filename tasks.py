import pretty_errors
import os
import sys

from robocorp import browser
from robocorp.tasks import task

pretty_errors.activate()
username = "user@automationanywhere.com"
password = "Automation123"
challenge_url = "https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-Login.html"

try:
    @task
    def solve_challenge():
        """Configure browser"""
        browser.configure(
            browser_engine="chromium",
            screenshot="only-on-failure",
            headless=False,
        )
        """Navigate to the page"""
        page = browser.goto(challenge_url)
        page.wait_for_load_state(state='domcontentloaded')

        """Accept cookies"""
        page.wait_for_selector(selector="//*[@id='onetrust-accept-btn-handler']")
        page.click(selector="//*[@id='onetrust-accept-btn-handler']")

        """Enter credentials"""
        page.fill(selector="//*[@id='inputEmail']", value=username)
        page.fill(selector="//*[@id='inputPassword']", value=password)
        page.click("button:text('Sign in')")

        """Wait for result and take screenshot"""
        page.wait_for_selector("//div[contains(@class, 'modal-content')]", state='visible')
        page.screenshot(path=os.getcwd() + "\\result.png")

        """End the process"""
        page.close()
        sys.exit()

except Exception as e:
    print("Exception: ", e)
    sys.exit()

if __name__ == '__main__':
    solve_challenge()
