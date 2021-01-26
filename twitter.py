import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests
import sys
import urllib.request
import os

# LINK FOR MATCH STATISTICS - FOOTBALLCRITIC
print("FootballCritic link to match: ")
input_url = input()
url = input_url

if not url:
    sys.exit()

response = requests.get(url, headers={'User-Agent': 'Custom5'})
print(response.status_code)

match_data = response.text
soup = BeautifulSoup(match_data, 'html.parser')

# WEB SCRAPING - FOOTBALLCRITIC
ht = soup.findAll("div", {"class": "league-information"})[0].find_next('span').text
ft = soup.findAll("div", {"class": "league-information"})[0].find_next('span').find_next('span').text[1:]

team1 = soup.findAll("div", {"class": "team-box"})[0].find_all('img')[0]['alt']
team1_poss = soup.findAll("div", {"class": "team-box"})[0].find_all('strong')[0].text
team1_shots = soup.findAll("div", {"class": "progress-row"})[0].find_next('span').text
team1_SoT = soup.findAll("div", {"class": "side-one"})[1].find_next('span').find_next('span').text
team1_pass = soup.findAll("div", {"class": "progress-row"})[6].find_next('span').text

team2 = soup.findAll("div", {"class": "team-box"})[1].find_all('img')[0]['alt']
team2_poss = soup.findAll("div", {"class": "team-box"})[1].find_all('strong')[0].text
team2_shots = soup.findAll("div", {"class": "progress-row"})[0].find_next('span').find_next('span').text
team2_SoT = soup.findAll("div", {"class": "side-two"})[1].find_next('span').find_next('span').text
team2_pass = soup.findAll("div", {"class": "progress-row"})[6].find_next('span').find_next('span').text

# WEB SCRAPING - UNDERSTAT
# LINK FOR XG
print("Understat link to match: ")

input_url = input()
url = input_url


if not url:
    sys.exit()

response = requests.get(url, headers={'User-Agent': 'Custom5'})
print(response.status_code)

match_data = response.text
soup = BeautifulSoup(match_data, 'html.parser')

team1_xG = soup.findAll("div", {"class": "progress-bar"})[3].findAll("div", {"class" : "progress-value"})[0].text
team2_xG = soup.findAll("div", {"class": "progress-bar"})[3].findAll("div", {"class" : "progress-value"})[1].text

# LINK FOR JPG IMAGE
print("Link to photo (jpg): ")
input_image = input()
if not input_image:
    sys.exit()

r = requests.get(input_image)
with open("saved_image.jpg", "wb") as f:
    f.write(r.content)

# TWEEPY
import tweepy as tp

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

# login
auth = tp.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

# tweet body
status = "#" + team1 + "-" + "#" + team2 + " " + ft + "(" + ht + ")" + "\n" + "Tiri (nello specchio) " + team1_shots + "-" + team2_shots + " (" +team1_SoT + "-" + team2_SoT + ")\n" + "xG " + team1_xG + "-" + team2_xG + "\n" + "Possesso " + team1_poss + "-" + team2_poss + "\n" + "Precisione "+ team1_pass + "%-" + team2_pass + "%"
print("Preview of the tweet : \n\n\n" + status + "\n\n")
input("Press Enter to tweet...")
imagePath = "saved_image.jpg"

# tweet
api.update_with_media(imagePath, status)