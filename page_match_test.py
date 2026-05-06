from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
import time
import sys
import csv

def start_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "1c98c6ac"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.android.chrome"
    options.app_activity = "com.google.android.apps.chrome.Main"
    # options.browser_name = "Chrome"
    options.set_capability("chromedriver_autodownload", True)
    options.no_reset = True
    options.full_reset = False
    # options.set_capability("noReset", True)
    # options.set_capability("dontStopAppOnReset", True)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    print("driver started")
    return driver

def txt_to_dict_list(file_path):
    result = []

    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(
            f,
            delimiter=',',
            quotechar='"'
        )

        for row in reader:
            result.append(row)

        print("extracted data from input file")

    return result


def find_elements(driver, xpath):
    # --------- Product Name ----------
    try:
        xpath_content = driver.find_element(By.XPATH,xpath)
        xpath_value = xpath_content.text
        print(xpath + " Found")
    except:
        # handle for other methods here after raising the certain error
        xpath_value = "Not Found"
        print(xpath + " Not Found")
        print("Test Case failed ")
        sys.exit(0)

    return xpath_value

def extract_product_details(driver, dict_xpath):

    url = dict_xpath["link"]

    driver.get(url)
    time.sleep(3)
    driver.switch_to.context("WEBVIEW_chrome")
    time.sleep(3)
    output_dict = {}
    for key, value in dict_xpath.items():
        if 'xpath' in key:
            print(key)
            xpath_value = find_elements(driver, value)
            output_dict[dict_xpath['id'] + '_'+ key + '_' + value] = xpath_value

    return output_dict

def transform_data(data):
    result = {}

    for record in data:
        for key, value in record.items():
            parts = key.split('_')

            record_id = parts[0]      # 1 or 2
            field_name = parts[1]     # title, price, color

            if record_id not in result:
                result[record_id] = {}

            result[record_id][field_name] = value
    print("output transformed")
    return result


def compare_records(transformed):
    print("comparing results")
    ids = list(transformed.keys())

    if len(ids) < 2:
        return "Not enough records to compare"

    rec1 = transformed[ids[0]]
    rec2 = transformed[ids[1]]

    mismatches = {}

    for key in rec1:
        if rec1.get(key) != rec2.get(key):
            mismatches[key] = (rec1.get(key), rec2.get(key))

    if not mismatches:
        return "MATCH"
    else:
        return f"NOT MATCH: {mismatches}"


data = txt_to_dict_list('product_details.txt')

output = []
if len(data)>0:
    driver = start_driver()
    for i in data:
        print(i)
        dict = extract_product_details(driver, i)
        output.append(dict)

    driver.quit()
transformed_data = transform_data(output)


result = compare_records(transformed_data)
print("Comparison Result:", result)


