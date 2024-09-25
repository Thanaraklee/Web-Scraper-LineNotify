import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def extract_content(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    # -------------------------------- Title & Title link -------------------------------- #
    raw_data_title_all = [_.find_all('a', href=True) for _ in soup.select('td.title')]
    raw_data_title_all = [_[0] for _ in raw_data_title_all if _]
    raw_data_title = [_.text.strip() for _ in raw_data_title_all]
    raw_data_title_link = [_['href'].strip() for _ in raw_data_title_all]

    # --------------------------------- Subtitle --------------------------------- #
    raw_data_subtitle = [' '.join(_.text.replace('\n',' ').strip().split()) for _ in soup.select('td.subtext') if _.text]
    
    # ------------------------------- Comment link ------------------------------- #
    raw_data_comment_link = [_.find_all('a', href=True) for _ in soup.select('td.subtext')]
    raw_data_comment_link = [i['href'].strip() for _ in raw_data_comment_link for i in _ if 'comments' in i.text]
    
    # ----------------------------------- Top 5 ---------------------------------- #
    raw_data_title_top_5 = raw_data_title[:5]
    raw_data_title_link_top_5 = raw_data_title_link[:5]
    raw_data_subtitle_top_5 = raw_data_subtitle[:5]
    raw_data_comment_link_top_5 = raw_data_comment_link[:5]

    return raw_data_title_top_5, raw_data_title_link_top_5, raw_data_subtitle_top_5, raw_data_comment_link_top_5

def cleaning_content(raw_title: str, raw_title_link:str, raw_subtitle: str, raw_comment_link: str) -> str:
    all_data = []
    for i in range(5):
        all_data.append([i+1, raw_title[i], raw_title_link[i],raw_subtitle[i], raw_comment_link[i]])

    return all_data

if __name__ == '__main__':
    url = os.environ['URL']
    raw_title, raw_title_link, raw_subtitle, raw_comment_link = extract_content(url=url)
    data = extract_content(url=url)
    data = cleaning_content(raw_title=raw_title, raw_title_link=raw_title_link, raw_subtitle=raw_subtitle, raw_comment_link=raw_comment_link)
    print(data)