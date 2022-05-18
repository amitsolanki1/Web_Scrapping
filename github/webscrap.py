import requests as r
from bs4 import BeautifulSoup
import csv
import pandas as pd
github={
    'name':[],
    'link':[],
    'summary':[]
}
repo_dict={
    'name':[],
    'link':[],
    'stars':[]
}
for page in range(1,30):
        
    url=f"https://github.com/topics?page={page}"
    site_url="https://www.github.com"
    response =r.get(url)
    if response.status_code==200:
        data=BeautifulSoup(response.content,'html.parser')
        data_head=data.find_all('div',class_="py-4 border-bottom d-flex flex-justify-between")
        for i in data_head:

            name=i.find_all('p',class_='f3 lh-condensed mb-0 mt-1 Link--primary')[0].text
            link=site_url+i.find('a')['href']
            # print(name, link)
            summary=i.find_all('p',class_="f5 color-fg-muted mb-0 mt-1")[0].text.strip().replace(" ","")
            # name=link.child()
            # github['name'].append(name)
            # github['link'].append(link)
            # github['summary'].append(summary)
            repo_link=r.get(link)
            repo_link_data=BeautifulSoup(repo_link.content,'html.parser')
            repo_link_data=repo_link_data.find_all('article',class_='border rounded color-shadow-small color-bg-subtle my-4')
            
            for repo_details in repo_link_data:
                # print(repo_details)
                repo_=repo_details.find_all('h3',class_='f3 color-fg-muted text-normal lh-condensed')
                # print(repo_[0].find_all('a'))
                repo_username=repo_[0].find_all('a')[0].text.strip()
                repo_username_link=site_url+repo_[0].find_all('a')[0]['href']
                # print(repo_[0])
                # print(repo_[0].a)
            
                repo_name=repo_[0].find_all('a')[1].text.strip()
                repo_link=site_url+ repo_[0].find_all('a')[1]['href']
                # print(f"repo_username: {repo_username} and repo_username_link : {repo_username_link} \nrepo_name :{repo_name} and repo_link : {repo_link}")
                # break
                # a_tags=repo_.find('a')
                # repo_username=a_tags[0].text.strip()
                # repo_name=a_tags[1].text.strip()
                # repo_link=site_url+'/topics/3d'+ a_tags[1]['href']
                repo_star=repo_details.find('span',id="repo-stars-counter-star").text
                # print(repo_star)
                repo_dict['name'].append(repo_name)
                repo_dict['link'].append(repo_link)
                repo_dict['stars'].append(repo_star)

    print(repo_dict)
    r = pd.DataFrame(repo_dict)
    r.to_csv("sub_repo_data.csv")    
        
    # print(github)
    
    # dd = pd.DataFrame(repo_dict)
    # dd.to_csv("sub_repo_data.csv")

