# Mobile Application Testing Project (Appium)

## Overview

This project demonstrates mobile web browser automation (Chrome on Android) using Appium and Python.
It focuses on validating product details across two different e-commerce platforms by extracting and comparing data such as title, price, and color.

The goal is to ensure consistency of product information across multiple sources.

---

## Objective

* Automate mobile web testing on Android devices
* Extract product data dynamically using XPath
* Compare product details between two websites
* Identify mismatches and ensure data accuracy

---

## Technologies Used

* **Python**
* **Appium**
* **Selenium WebDriver**
* **Android Automation (UiAutomator2)**
* **CSV Handling (for test data)**

---

## Project Structure

* `page_match_test.py` → Main automation script
* `product_details.txt` → Input test data (contains URLs and XPaths)

---

## How It Works

### 1. Data Preparation

* Test data is stored in a `.txt` file in CSV format
* Includes:

  * Product ID
  * Website link
  * XPath for title, price, and color

### 2. Driver Initialization

* Appium driver is configured using:

  * Platform: Android
  * Automation: UiAutomator2
  * Browser: Chrome (mobile web testing, not native app)
* Executes on a real Android device

### 3. Data Extraction

* Opens each product URL in Chrome browser
* Switches to WebView context
* Extracts:

  * Product Title
  * Product Price
  * Product Color

### 4. Data Transformation

* Extracted data is structured into dictionary format
* Organized based on product ID

### 5. Data Comparison

* Compares product details between two sources
* Identifies mismatches in:

  * Title
  * Price
  * Color

---

## How to Run

### Prerequisites

* Install Python
* Install Appium
* Install required libraries:

```bash
pip install appium-python-client selenium
```

* Start Appium server
* Connect Android device with USB debugging enabled

### Execution

```bash
python page_match_test.py
```

---

##Sample Output

* **MATCH** → If product details are same across both websites
* **NOT MATCH** → Displays mismatched fields with values

Example:

```
Comparison Result: NOT MATCH: {'price': ('₹999', '₹1099')}
```

---

##Key Features

* Data-driven testing using external input file
* Dynamic XPath-based element identification
* Mobile web browser automation using Appium (Chrome on Android)
* Cross-platform product data validation
* Automated comparison logic for mismatch detection

---

## Limitations

* Uses static waits (`time.sleep`)
* Limited to two product comparisons
* Basic error handling

---

## Future Enhancements

* Implement explicit waits for better stability
* Integrate with Pytest framework
* Add reporting (HTML/Allure)
* Support multiple product comparisons
* Improve exception handling and logging

---

##Author

**Vallimayil**

---
