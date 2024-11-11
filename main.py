from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from docx import Document

# Set up the Selenium WebDriver (Ensure the correct path to your chromedriver is provided)
driver = webdriver.Chrome()

# Open the webpage
driver.get("http://e-books.helwan.edu.eg/storage/29946/index.html#/reader/chapter/8")

# Explicit wait: Wait for a specific element (e.g., div with a specific class) to be present
try:
    # Wait for the div element to load (replace 'WordSection2' with the actual class you're looking for)
    specific_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "WordSection2"))
    )
    # Once the element is loaded, extract the inner HTML
    html_content = specific_div.get_attribute('innerHTML')
    # print(html_content)

    # Create a new Document
    doc = Document()

    # If you want to extract just the text content:
    text_content = specific_div.text
    #print("Text Content:", text_content)

    # Add plain text
    doc.add_paragraph(f"{text_content}")

    # Save the document to a file
    doc.save("extracted_content.docx")

except TimeoutException:
    print("Timed out waiting for page to load or element to be present.")

finally:
    # Close the browser
    driver.quit()
