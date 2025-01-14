# steve_roggenbot

This repository describes a Python bot to automate shitposting on Twitter.

This Twitter bot posts tweets (with optional images) using data from CSV files, YAML configurations, or other sources. The bot leverages Python packages such as **pandas**, **yaml**, **tweepy**, and **datetime** to handle data processing, configuration, Twitter API communication, and time-based operations, respectively.

---

## Features

- **Tweet Posting:** Uses the Twitter API (via Tweepy) to post updates to Twitter.
- **CSV + pandas:** Reads input data (e.g., tweets, image paths) from CSV files using `pandas`.
- **YAML for Config:** Stores Twitter API credentials or other settings in YAML files.
- **Time Management:** Utilizes `datetime` for scheduling or timestamping posted tweets.

---

## Requirements

- Python 3.7 or higher
- Twitter Developer account and valid Twitter API credentials (API Key, API Secret, Access Token, Access Token Secret, Bearer Token if needed)
- You will need to install the following Python packages: `pandas`, `pyyaml`, `tweepy`
---

## Installation

You can install this bot in two main ways:  
1. **Using Python’s built-in `venv`**  
2. **Using `conda` (Anaconda/Miniconda)**

## Usage

1. Configure Your Credentials
* Store your Twitter API credentials (API Key, API Secret, Access Token, Access Token Secret, Bearer Token if using API v2) in a YAML file (e.g., config.yaml).
* Make sure to never commit your credentials to version control.

2. Prepare Your Data
* If posting from a CSV file, create a CSV (e.g., tweets.csv) containing tweet text, image paths, or any other fields you need.
* If needed, you can also store advanced configurations in YAML.

3. Run the Bot
* Within your environment (venv or conda), run:

```python
python3 steverogganbot.py

```

This project is distributed under the [MIT License](https://chatgpt.com/c/LICENSE.md). See LICENSE.md for more information.

Disclaimer
- Use this bot responsibly, in compliance with [Twitter’s Terms of Service](https://twitter.com/en/tos).
- Securely store your credentials and do not commit them to version control or share them publicly.

![](./images/rogganbot.jpg)
