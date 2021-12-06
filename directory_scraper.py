import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=<INSERT PATH TO AN EMPTY DIRECTORY HERE>")
driver = webdriver.Chrome(executable_path=r"<INSERT PATH TO CHROMEDRIVER HERE>", options=options)
driver.get("https://contacts.google.com/u/0/directory")

print("Sleeping to load page...")
time.sleep(2)

scroll_pause_time = 0.25
viewport_height = driver.execute_script("return document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].offsetHeight;")
list_height = driver.execute_script("return document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].scrollHeight;")
current_scroll_position = driver.execute_script("return document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].scrollTop;")
i = 0

def scroll_to_next(height = 0):
    global i
    global current_scroll_position
    if height == 0:
        driver.execute_script("document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].scrollTo(0, {screen_height} * {i});".format(screen_height = viewport_height, i = i))
        i += 1
    else:
        driver.execute_script("document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].scrollBy(0, {height});".format(height = height))
    time.sleep(scroll_pause_time)
    current_scroll_position = driver.execute_script("return document.getElementsByClassName(\"zQTmif SSPGKf eejsDc\")[0].scrollTop;")

rows_list = []

while current_scroll_position != (list_height - viewport_height):
    redo = False
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for parent in soup.find_all(class_="XXcuqd"):
        try:
            name = str(parent.find(class_="PDfZbf").string)
            email = str(parent.find(class_="hUL4le").string)
            phone = str(parent.find(class_="E6Tb7b b62A4e").string)
            position = str(parent.find(class_="E6Tb7b ZAFZMe").string)
            rows_list.append([name, email, phone, position])
        except:
            time.sleep(2)
            print(parent.prettify())
            redo = True
            break
    if redo == False:
        scroll_to_next()
    else:
        scroll_to_next(height=50)
        print("Redoing...")

df = pd.DataFrame(rows_list, columns=["Name", "Email", "Phone", "Job title & Company"])
df = df.drop_duplicates()
df.to_csv("directory.csv", index = False)