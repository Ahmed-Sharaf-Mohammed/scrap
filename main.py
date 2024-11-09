from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from docx import Document
from docx.shared import Pt
import time

# Path to your ChromeDriver
service = Service(r"C:\Users\Ahmed-Sharaf\PycharmProjects\pythonProject\chromedriver-win64\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
url = "http://e-books.helwan.edu.eg/storage/29946/index.html#/reader/chapter/8"
driver.get(url)

# Wait for JavaScript-rendered content to load
time.sleep(10)  # Adjust the time based on your connection speed

# Get the page source and parse it
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Locate the target div
content_div = soup.find("div", class_="WordSection2")

# Extract and clean the text content
if content_div:
    paragraphs = content_div.find_all(["p", "h2", "span"])
    text_content = []

    for para in paragraphs:
        text = para.get_text(strip=True)
        if text:
            text_content.append(text)

# Close the WebDriver
driver.quit()

# Save the content to a Word document
document = Document()

for paragraph in text_content:
    # Customize styling (e.g., Arabic font and size)
    p = document.add_paragraph(paragraph)
    run = p.runs[0]
    run.font.name = "Simplified Arabic"  # Specify Arabic font
    run.font.size = Pt(14)  # Font size

# Save the document
output_path = r"C:\Users\Ahmed-Sharaf\Documents\extracted_content.docx"
document.save(output_path)

print(f"Content saved to {output_path}")
