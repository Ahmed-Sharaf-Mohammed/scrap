"""def diff(paragraph1, paragraph2):
    words1 = list(paragraph1.lower().split())
    words2 = list(paragraph2.lower().split())

    differences = []
    i = 0

    while i < len(words1) and i < len(words2):
        if words1[i] != words2[i]:
            differences.append(words2[i])
            i += 1
        else:
            i += 1

    # If there are remaining words in words2, add them to differences
    differences.extend(words2[i:])

    print(differences)

# Example usage:
paragraph2 = "hello hello add"
paragraph1 = "hello add hello hello hello hello"
diff(paragraph1, paragraph2)
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Initialize the WebDriver (Make sure the path is correct for your system)
driver = webdriver.Chrome(executable_path="path_to_chromedriver")  # Replace with your path to chromedriver
driver.get("http://e-books.helwan.edu.eg/storage/29946/index.html#/reader/chapter/8")

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time as needed for the content to load fully

# Get the page source after rendering JavaScript
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find all span elements
spans = soup.find_all("span")

# Print the text content of each span element
for span in spans:
    print(span.get_text())

# Close the WebDriver
driver.quit()
