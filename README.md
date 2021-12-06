# DirectoryScraper
Google Contacts directory scraper w/ Selenium, BS4, and pandas

## Usage
1. Fill in the script with the path to ChromeDriver on your computer and the path to an empty folder so ChromeDriver can create an empty profile.
2. Run the script once to launch ChromeDriver and create the profile, and then login to the Google account in question in the ChromeDriver profile. Stop execution of the script.
3. Rerun the script, and wait until finished.

## Notes on Execution
Google Contacts dynamically loads contacts 500 at a time, so if the scraper isn't managing to catch all of the contacts, lengthen the `scroll_pause_time` variable in the script.
