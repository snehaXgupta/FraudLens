from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# ---------------------------------------
# CHROME OPTIONS
# ---------------------------------------

options = Options()

options.add_argument("--start-maximized")

# ---------------------------------------
# OPEN CHROME
# ---------------------------------------

driver = webdriver.Chrome(options=options)

# ---------------------------------------
# USER INPUT
# ---------------------------------------

url = input("\nEnter Full Flipkart Product URL:\n")

# ---------------------------------------
# OPEN WEBSITE
# ---------------------------------------

driver.get(url)

print("\nOpening website...")

# Wait for page load
time.sleep(10)

# ---------------------------------------
# SCROLL MULTIPLE TIMES
# ---------------------------------------

for i in range(5):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(3)

print("\nScrolling completed!")

# ---------------------------------------
# GET PAGE SOURCE
# ---------------------------------------

page_source = driver.page_source

# ---------------------------------------
# CHECK REVIEW TEXT
# ---------------------------------------

if "review" in page_source.lower():

    print("\nReviews content exists on page!")

else:

    print("\nNo review content found!")

# ---------------------------------------
# SAVE HTML
# ---------------------------------------

with open("flipkart_page.html", "w", encoding="utf-8") as file:

    file.write(page_source)

print("\nHTML saved successfully!")

input("\nPress Enter to close browser...")

driver.quit()