import requests
from bs4 import BeautifulSoup
import time
import re

regexp = re.compile("a href=\"\/\d*\"")

# Base URL for the repost pages
base_url = 'https://weibo.cn/repost/Ni2Axx2fy?uid=3266647631&page={}'
cookies = {
    "SUB":" ",
    "SUBP":" ",
    "SSOLoginState":" ",
    "SCF":" ",
    "_T_WM":" "
}
# Create a list to store usernames
usernames = []

# Iterate through pages from 1 to 16
for page in range(1, 17):
    time.sleep(0.5)
    # Make a request to the URL
    url = base_url.format(page)
    response = requests.get(url, cookies=cookies)
    
    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        
        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')
        
        page_usernames = []
        
        # Find all 'a' tags with href attributes containing usernames
        for a in soup.find_all('a', href=True):
            if (regexp.search(str(a)) != None):
                page_usernames.append(a.get_text())
        
        # Add the usernames from this page to the list
        usernames.extend(page_usernames)
        print(usernames)
    else:
        print(f"Failed to fetch page {page}, status code: {response.status_code}")


# Convert the list to a set to remove duplicates
unique_list = list(set(usernames))

# Print the extracted usernames
with open("usernames.txt", "w", encoding="utf-8") as file:
    # Use a for loop to iterate through the list and write each item followed by a newline character
    for item in unique_list:
        file.write(item + "\n")
