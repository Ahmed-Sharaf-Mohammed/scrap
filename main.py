from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from docx import Document

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("http://e-books.helwan.edu.eg/storage/29946/index.html#/reader/chapter/8")

try:
    # Wait for the div element with the class 'WordSection2' to load
    specific_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "WordSection2"))
    )
    # Get the HTML content
    html_content = specific_div.get_attribute('innerHTML')

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Create a new Word Document
    doc = Document()

    # Set to track already processed text
    processed_text = set()

    # Extract and format content
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        # Initialize the paragraph
        paragraph = doc.add_paragraph()

        # Collect bold text separately
        bold_texts = []
        for sub_element in element.find_all('b'):
            bold_text = sub_element.get_text(separator=" ", strip=True)
            if bold_text and bold_text not in processed_text:
                bold_texts.append(bold_text)
                processed_text.add(bold_text)

        # Add bold text to the paragraph
        for bold_text in bold_texts:
            run = paragraph.add_run(bold_text + " ")
            run.bold = True

        # Remove bold texts from the full text to avoid duplication
        full_text = element.get_text(separator=" ", strip=True)
        for bold_text in bold_texts:
            full_text = full_text.replace(bold_text, "").strip()

        # Add the remaining text (non-bold) if it exists and hasn't been processed yet
        if full_text and full_text not in processed_text:
            paragraph.add_run(full_text)
            processed_text.add(full_text)

        # Handle the headings (h1, h2, h3, etc.)
        if element.name.startswith('h'):
            heading_text = element.get_text(separator=" ", strip=True)
            if heading_text not in processed_text:
                doc.add_paragraph(heading_text, style='Heading ' + element.name[1])
                processed_text.add(heading_text)

    # Save the Word document
    doc.save("formatted_extracted_content.docx")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
