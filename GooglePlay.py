# IMPORTS:

# These 2 imports are necessary to use selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# Package "time" is using to sleep scraper
import time

# I am using "tqdm" package to see progress of loop "for i in range" execution in which selenium scrapes
from tqdm import tqdm

# to be able to save scraped data to csv file
import csv


# CODE:

# To be able to launch and operate on firefox
opts = Options()
browser = Firefox(options=opts)

# Launch a google play page with information about app
browser.set_page_load_timeout(100)

# Page has few sec to load, then window will be closed
try:
    browser.get("here you have to paste a app details page url")

except Exception as e:
    print(getattr(e, 'message', str(e)))
    browser.close()
    quit()

# Close window with cookies information
browser.find_element_by_xpath('/html/body/div[1]/c-wiz[1]/div/div[1]/div[1]/div/a[2]').click()

# Maximize window
browser.maximize_window()

# Scroll down
browser.execute_script("window.scrollBy(0, 800)")

# Sleep for a while (0.5 sec)
time.sleep(0.5)

# Scrape some general information about app
rating = browser.find_element_by_css_selector(
               '.BHMmbe'
               ).text

ratings_count = browser.find_element_by_css_selector(
              '.EymY4b > span:nth-child(2)'
              ).text

latest_update = browser.find_element_by_css_selector(
              '.IxB2fe > div:nth-child(1) > span:nth-child(2) > div:nth-child(1) > span:nth-child(1)'
              ).text

current_version = browser.find_element_by_css_selector(
              'div.hAyfc:nth-child(4) > span:nth-child(2) > div:nth-child(1) > span:nth-child(1)'
              ).text

download_count = browser.find_element_by_css_selector(
              'div.hAyfc:nth-child(3) > span:nth-child(2) > div:nth-child(1) > span:nth-child(1)'
              ).text

print("\n",
      'Rating: ', rating,"\n",
      'Ratings Count: ', ratings_count,"\n",
      'Latest update: ', latest_update,"\n",
      'Current version: ', current_version,"\n",
      'Download count: ', download_count,"\n")

# Scroll again just to have a view
browser.execute_script("window.scrollBy(0, 800)")

time.sleep(0.5)

# Click to show more review
browser.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div').click()

time.sleep(0.5)

# Click to sort by the latest reviews
browser.find_element_by_css_selector('div.MocG8c:nth-child(3)').click()
browser.find_element_by_css_selector('.OA0qNb > div:nth-child(1)').click()

time.sleep(0.5)

# Create a csv file
with open('YourCSVname.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Date', 'Rating (1-5)', 'Content', 'Usefulness'])

# Change value of rating_count to int
x = ratings_count.replace(' ','')
z = int(x)

# I use a for i in range loop to can use a 'tqdm' package to measure our progress directly
for z in tqdm(range(z), ncols=80):

    # Try scrape
    try:

        z+=1

        # Date of review
        single_date = browser.find_element_by_css_selector(
            'c-wiz.zQTmif:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child('
            + str(z) +
            ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)').text

        # Rating
        single_rating = browser.find_element_by_css_selector(
            '.W4P4ne > div:nth-child(2) > div:nth-child(3) > div:nth-child('
            + str(z) +
            ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
            ).get_attribute("aria-label")

        # We need only a numeric rating so we have to delete other not needed strings
        single_rating = single_rating[:-5]
        single_rating = single_rating[20:]

        # Content of review
        # Try and except is here because sometimes when review is too long you have to click a button to see full review
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div['
                + str(z) +
                ']/div/div[2]/div[2]/span[1]/div/button').click()

            time.sleep(0.25)

            single_content = browser.find_element_by_css_selector('.W4P4ne > div:nth-child(2) > div:nth-child(3) > div:nth-child('
                + str(z) +
                ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)').text

        except:
            single_content = browser.find_element_by_css_selector(
                'c-wiz.zQTmif:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child('
                + str(z) +
                ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').text

        # Count of likes this review get
        single_usefulness = browser.find_element_by_css_selector(
            'c-wiz.zQTmif:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child('
            + str(z) +
            ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)').text

        z-=1

        # I don't know why selenium scrape "" instead of 0, so:
        if single_usefulness == '':
            single_usefulness = 0

        # Add scraped values to csv
        with open('YourCSVname.csv', 'a') as fd:
            filewriter = csv.writer(fd, delimiter=',')
            filewriter.writerow([single_date, single_rating, single_content, single_usefulness])

        # Google Play load next reviews only if you scroll down
        browser.execute_script("window.scrollBy(0, 90)")

        # Try click button if it is on page, if not go forward
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span').click()

        except:
            pass

        time.sleep(0.5)

    # Except when something is wrong with scraping
    except Exception as e:
        print(getattr(e, 'message', str(e)))
        browser.close()
        quit()


# TODO:



