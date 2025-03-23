import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import time

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# save the content of the page
src = result.content

# parse the page
soup = BeautifulSoup(src, "lxml")
#print(soup)

# find the job titles & companies names & locations & skills
job_titels = soup.find_all("h2", {"class":"css-m604qf"})
campany_names = soup.find_all("a",{"class":"css-17s97q8"})
location_campanys = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})
#print(job_skills)

# loop to get the text of the job titles & companies names & locations & skills
job_titel = []
campany_name = []
location_campany = []
job_skill = []
salary = []

links = []

for i in range(len(job_titels)):
    job_titel.append(job_titels[i].text)
    campany_name.append(campany_names[i].text)
    location_campany.append(location_campanys[i].text)
    job_skill.append(job_skills[i].text)
    links.append(job_titels[i].find("a").attrs['href'])


#print(job_titel , campany_name , location_campany , job_titel)
with open("jobs.csv", "w" , newline="") as file:

    date = time.strftime(f"%Y-%m-%d -- {int(time.strftime('%H')) - 12 }:%M:%S")

    writer = csv.writer(file)
    writer.writerow(["Time" , "Job Titel", "Company Name", "Location", "Skills" , "Create : " + f"{[date]}"])
    writer.writerows(zip_longest([date] * len(job_titels) , job_titel, campany_name, location_campany, job_skill))

    print("Done")
