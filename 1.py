import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# set the path to the ChromeDriver executable file
chromedriver_path = r"C:\Users\lidor\PycharmProjects\Sdarot\chromedriver.exe"

# set the path to your user profile
user_data_dir = r"C:\Users\Lidor\AppData\Local\Google\Chrome\User Data"

# set the options for the Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument("--user-data-dir=" + user_data_dir)

# set the path to the download directory
download_folder = r"G:\MI BOX 4\TV Shows\Avatar The Last Airbender"

# start the Chrome browser with the specified pa
# th to the ChromeDriver executable
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# set the starting episode and season numbers
episode_number = 1
start_season_number = 1
# temp_start_episode_number = start_episode_number

# loop through the episodes and navigate to each one
# for episode_number in range(start_episode_number, end_episode_number+1):
while True:
    # navigate to the URL for the current episode
    # episode_number = start_episode_number
    url = f'https://sdarot.tw/watch/3604-%D7%A7%D7%95%D7%A4%D7%94-%D7%A8%D7%90%D7%A9%D7%99%D7%AA-kupa-rashit-cash-register/season/{start_season_number}/episode/{episode_number}'
    driver.get(url)

    # press the "End" key on the keyboard after 5 seconds to activate the "end" button
    time.sleep(0.5)
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.END)
    time.sleep(5)

    # check if the episode does not exist, move to next episode
    if 'אין פרקים בעונה זו' in driver.page_source:
        driver.quit()
        print("finish")
        sys.exit()
        break

    # check if the season does not exist, move to next season
    if 'מצטערים, הפרק לא קיים במערכת.' in driver.page_source:
        # driver.quit()
        start_season_number += 1
        episode_number = 1
        start_episode_number = 1
        continue
    #
    # # if '' in driver.page_source:
    # #     driver.quit()
    # #     print("finish")
    #
        # break



    # find the download button with the highest quality available
    download_button = None
    for quality in ['720p', '1080p', '480p']:
        try:
            download_button = driver.find_element_by_xpath(f"//*[text()='הורדת הפרק באיכות {quality}']")
            break
        except:
            pass

    if download_button is not None:
        download_button.click()
        episode_number +=1
    else:
        print("No download button found")

        # keep track of the files in the download directory before starting the download
    initial_files = os.listdir(download_folder)

    # wait for a new file to appear in the download directory
    while True:
        current_files = os.listdir(download_folder)
        new_files = set(current_files) - set(initial_files)
        if new_files:
            # Get the first new file in the folder
            new_file = os.path.join(download_folder, new_files.pop())

            # Check if the file is a video file
            if new_file.endswith('.mp4') or new_file.endswith('.mkv') or new_file.endswith('.avi'):
                break

        time.sleep(1)

    # if we have downloaded 5 episodes, close the browser and start again
    if episode_number % 5 == 0:
        driver.quit()
        time.sleep(10)  # wait for 10 seconds before starting again
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# close the browser after all episodes are downloaded
driver.quit()
