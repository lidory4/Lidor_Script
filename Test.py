import time
from selenium import webdriver
import pyautogui
import random

from selenium.webdriver import ActionChains

# set the path to the ChromeDriver executable file
chromedriver_path = r"C:\Users\lidor\PycharmProjects\Sdarot\chromedriver.exe"

# set the path to your user profile
user_data_dir = r"C:\Users\Lidor\AppData\Local\Google\Chrome\User Data"

# set the options for the Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument("--user-data-dir=" + user_data_dir)

# start the Chrome browser with the specified path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# open a URL of your choice
url = "https://cacms.state.gov/s/new-appointment"
driver.get(url)

# wait for the page to load
time.sleep(3)
# sleep_time = random.uniform(7, 16)
# time.sleep(sleep_time)

# specify the square region to click in
# x_min, x_max, y_min, y_max = 990, 1016, 619, 651

# click on Verify
x = random.randint(990, 1016)
y = random.randint(619, 651)
pyautogui.click(x, y)
time.sleep(10)

# click on a choose
x = random.randint(1480, 1953)
y = random.randint(432, 462)
pyautogui.click(x, y)
time.sleep(2)

# click on Israel
x = random.randint(1484, 1948)
y = 623
pyautogui.click(x, y)
time.sleep(2)

# click on the "next" button
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
next_button.click()

# click on a random West
x = random.randint(1490, 1935)
y = random.randint(495, 598)
pyautogui.click(x, 356)
time.sleep(2)

# click on the "next" button
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
next_button.click()

# click on a random x,y within the square region
x = random.randint(1478, 1912)
y = random.randint(757, 850)
pyautogui.click(x, y)
time.sleep(2)

# click on the "next" button
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
next_button.click()
time.sleep(2)

# click on the "next" button
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Today')]")
next_button.click()
time.sleep(2)

# search for a button containing either "am" or "pm"
buttons = driver.find_elements_by_xpath("//button[contains(text(), 'am') or contains(text(), 'pm')]")
if buttons:
    button = random.choice(buttons)
    button.click()
else:
    print('its not work')
# # click on a random x,y within the square region
# x = random.randint(2259, 2282)
# y = random.randint(527, 549)
# pyautogui.click(x, y)
# time.sleep(1)


# generate a random x and y coordinate within the specified range
# while True:
#     x = random.randint(990, 1016)
#     y = random.randint(563, 585)
#
# # perform a random click at the generated coordinates
#     action = ActionChains(driver)
#     action.move_by_offset(x, y).click().perform()
#     time.sleep(1)
#     x += 1
#     if x == 100:
#         break

# specify the x,y coordinates to click on
# x1, y1 = 1005, 632
# x2, y2 = 1926, 449
# x3, y3 = 1587, 622
# # click on the specified coordinates
# pyautogui.click(x1, y1)
# time.sleep(1)
# pyautogui.click(x2, y2)
# time.sleep(1)
# pyautogui.click(x3, y3)
# time.sleep(1)

# Clicked on x=1005, y=632
# Clicked on x=1926, y=449
# Clicked on x=1587, y=622
# click on the "next" button
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
next_button.click()