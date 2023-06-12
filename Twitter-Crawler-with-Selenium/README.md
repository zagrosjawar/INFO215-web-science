## about this code:
Crawling Twitter hashtag pages with Selenium. 

This program crawls over 6 random twitter pages using hashtag links.
In this simple version, there is no need to keep track of already visited pages.
The program only follow hyperlinks of hashtag links.

### steps: 
1. Load a twitter page from a given url using Selenium
2. Wait for some tweeter feeds to load. You may use WebDriverWait with EC.
3. Select a hashtag randomly from the twitter page.
4. Visit the randomly selected hashtag's hyperlink from step  3 and go to step 1.    
Keep counting the number of visited pages and stop crawling if you have visited 6 pages.


Note: Initial URL should look something like: https://twitter.com/search?q=%23Winter
Here %23 is representing # in UTF-8 encoding.

Certainly! Here's a detailed step-by-step guide on what Selenium is and how to set it up. Please note that this guide assumes you're using Selenium WebDriver with Python.

## Selenium

Selenium is an open-source automation framework that allows you to automate interactions with web browsers. It provides a suite of tools and libraries for browser automation, testing, and web scraping. Selenium WebDriver is the most commonly used component of Selenium, offering a simple and intuitive API to control web browsers programmatically.

### Setting Up Selenium

To set up Selenium WebDriver with Python, follow these step-by-step instructions:

#### Step 1: Install Python

Ensure that Python is installed on your system. You can download the latest version of Python from the official Python website: [python.org](https://www.python.org/downloads/)

#### Step 2: Install Selenium

Open a terminal or command prompt and execute the following command to install Selenium using pip, the Python package installer:
```
pip install selenium
```

#### Step 3: Download a Web Driver

Selenium WebDriver requires a specific web driver to interface with the chosen web browser. The web driver acts as a bridge between Selenium and the browser. 

1. Determine the web browser you want to automate (e.g., Chrome, Firefox, Safari).
2. Download the appropriate web driver for the selected browser. Here are the download links for some popular web drivers:
   - ChromeDriver: [chromedriver.chromium.org](https://sites.google.com/chromium.org/driver/)
   - GeckoDriver (Firefox): [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases)
   - SafariDriver (built-in on macOS): No separate installation required.
   - Other web drivers for different browsers are available on the Selenium website: [selenium.dev](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

3. Download the web driver executable compatible with your operating system and browser version.
4. Place the web driver executable in a directory that is included in your system's PATH environment variable.

#### Step 4: Set Up a Selenium Project

1. Create a new directory for your Selenium project.
2. Create a new Python file within the project directory (e.g., `main.py`).
3. Open the Python file in a text editor.

#### Step 5: Import Selenium and Set Up a WebDriver

In your Python file, import the necessary modules from the Selenium library and set up a WebDriver instance. Here's an example for Chrome:

```python
from selenium import webdriver

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
```

Replace `'Chrome'` with the appropriate WebDriver class for your chosen browser (e.g., `'Firefox'`, `'Safari'`, etc.). Make sure the web driver executable is accessible via the system's PATH environment variable.

#### Step 6: Use Selenium to Automate Browser Interactions

With the WebDriver set up, you can start using Selenium to automate browser interactions. For example, you can navigate to a webpage, interact with elements, fill out forms, and extract data.

Here's an example that navigates to a webpage and prints the page title:

```python
# Navigate to a webpage
driver.get('https://www.example.com')

# Print the page title
print(driver.title)
```

You can find more examples and information on Selenium's official documentation: [selenium.dev](https://www.selenium.dev/documentation/)

#### Step 7: Clean Up and Close the WebDriver

Once you have finished using the WebDriver, make sure to close it properly to release system resources:

```python
# Close the WebDriver
driver.quit()
```

#### Step 8: Execute the Selenium Script

To run your Selenium script, execute the Python

 file from the command line:

```
python main.py
```

Ensure that you are in the project directory when running the command.

Congratulations! You have successfully set up Selenium WebDriver with Python. You can now automate browser interactions, perform web testing, or develop web scraping applications using Selenium's powerful automation capabilities.

Remember to review the Selenium documentation for a deeper understanding of its features and advanced usage.

Happy automating! (by ChatGPT ;) )
