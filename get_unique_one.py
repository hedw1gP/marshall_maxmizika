import requests

# Read the contents of usernames.txt and split it into a list of entries
with open('usernames.txt', 'r', encoding="utf-8") as file:
    entries = file.read().split('\n')

# Retrieve the newest BTC hash
btc_api_url = 'http://blockchain.info/q/latesthash'
response = requests.get(btc_api_url)

# Convert hex to dec
newest_hash = response.text
print("Newest hash: {}".format(newest_hash))
index = int(newest_hash, 16) % len(entries)

# Here it goes, the chosen one!
print(entries[index])

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(entries[index])
