from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time

# ---------------------------------------
# EDGE OPTIONS
# ---------------------------------------

options = Options()

options.use_chromium = True

# ---------------------------------------
# OPEN EDGE
# ---------------------------------------

driver = webdriver.Edge(
    service=Service(
        EdgeChromiumDriverManager().install()
    ),
    options=options
)

# ---------------------------------------
# USER INPUT
# ---------------------------------------

url = input("\nEnter Full Flipkart Product URL:\n")

# ---------------------------------------
# OPEN WEBSITE
# ---------------------------------------

driver.get(url)

print("\nOpening website...")

# ---------------------------------------
# WAIT
# ---------------------------------------

time.sleep(10)

# ---------------------------------------
# SCROLL PAGE
# ---------------------------------------

for i in range(5):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(3)

print("\nScrolling completed!")

# ---------------------------------------
# FIND REVIEWS
# ---------------------------------------

reviews = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'t-ZTKy')]"
)

# ---------------------------------------
# OUTPUT
# ---------------------------------------

if not reviews:

    print("\nNo reviews found!")

else:

    print(f"\nFound {len(reviews)} reviews\n")

    for i, review in enumerate(reviews[:10]):

        print(f"\nReview {i+1}:")
        print(review.text)

input("\nPress Enter to close browser...")

driver.quit()
