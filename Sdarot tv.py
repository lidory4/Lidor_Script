import tkinter as tk
from tkinter import filedialog
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# create the GUI window
root = tk.Tk()

# function to handle selecting the download folder
def choose_download_folder():
    download_folder = filedialog.askdirectory()
    download_folder_label.config(text=download_folder)

# create a label and button to select the download folder
download_folder_label = tk.Label(root, text="Download folder location:")
download_folder_label.pack()

download_folder_button = tk.Button(root, text="Select folder", command=choose_download_folder)
download_folder_button.pack()

# function to handle getting the URL input and starting the download
def start_download():
    # get the download folder location
    download_folder = download_folder_label.cget("text")

    # get the URL input
    url = url_entry.get()

    # set the path to the ChromeDriver executable file
    chromedriver_path = r"C:\Users\lidor\PycharmProjects\Sdarot\chromedriver.exe"

    # set the path to your user profile
    user_data_dir = r"C:\Users\Lidor\AppData\Local\Google\Chrome\User Data"

    # set the options for the Chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument("--user-data-dir=" + user_data_dir)

    # set the download folder
    prefs = {"download.default_directory": download_folder}
    chrome_options.add_experimental_option("prefs", prefs)

    # start the Chrome browser with the specified path to the ChromeDriver executable
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    # set the starting episode and season numbers
    episode_number = 1
    start_season_number = 1

    # loop through the episodes and navigate to each one
    while True:
        # navigate to the URL for the current episode
        url = url.format(start_season_number, episode_number)
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

        # find the download button with the highest quality available
        download_button = None
        for quality in ['720p', '1080p', '480p']:
            try:
                download_button = driver.find_element_by_xpath(f"//*[text()='הורדת הפרק באיכות {quality
        if download_button is not None:
            download_button.click()
            episode_number += 1
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

# create a label and entry for the URL input
url_label = tk.Label(root, text="Enter the URL for the TV show (use {} as placeholders for season and episode numbers):")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

# create a button to start the download
download_button = tk.Button(root, text="Download", command=start_download)
download_button.pack()

# start the GUI window
root.mainloop()
