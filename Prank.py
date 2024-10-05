from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

class StealthYouTubeVisitor:
    def __init__(self):
        # Setup options to make the browser less detectable
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run the browser in the background
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--incognito")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        
        # Suppressing automation flags
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # Path to your WebDriver (Make sure to have the correct driver for your browser)
        self.driver = webdriver.Chrome(options=options)

    def visit_youtube(self):
        print("Visiting YouTube...")
        self.driver.get("https://www.youtube.com")

        # Wait to simulate user reading or interacting
        self.random_wait()

        # Simulate scrolling down like a human
        self.simulate_scroll()

        # Wait some more time
        self.random_wait()

        # Optionally, simulate some interaction (like a search or clicking a video)
        self.perform_search("Selenium Python tutorial")

        # Stay for a while, and then exit
        self.random_wait(5, 10)  # Stay a bit longer
        print("Closing browser.")
        self.driver.quit()

    def random_wait(self, min_sec=2, max_sec=5):
        # Wait for a random time between min_sec and max_sec
        wait_time = random.uniform(min_sec, max_sec)
        print(f"Waiting for {round(wait_time, 2)} seconds...")
        time.sleep(wait_time)

    def simulate_scroll(self):
        # Scroll down the page randomly
        print("Simulating scrolling...")
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(random.randint(3, 6)):
            body.send_keys(Keys.PAGE_DOWN)
            self.random_wait()

    def perform_search(self, query):
        print(f"Performing search for: {query}")
        try:
            search_box = self.driver.find_element(By.NAME, "search_query")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            self.random_wait()
        except Exception as e:
            print("Error performing search:", e)

if __name__ == "__main__":
    visitor = StealthYouTubeVisitor()
    visitor.visit_youtube()
