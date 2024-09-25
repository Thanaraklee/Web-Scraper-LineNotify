from scrap import extract_content, cleaning_content
import os

if __name__ == '__main__':
    url = os.environ['URL']
    raw_title, raw_title_link, raw_subtitle, raw_comment_link = extract_content(url=url)
    data = extract_content(url=url)
    data = cleaning_content(raw_title=raw_title, raw_title_link=raw_title_link, raw_subtitle=raw_subtitle, raw_comment_link=raw_comment_link)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh:
        for i in data:
            print(f'TITLE_{i[0]}={i[1]}', file=gh)
            print(f'TITLE_LINK_{i[0]}={i[2]}', file=gh)
            print(f'SUBTITLE_{i[0]}={i[3]}', file=gh)
            print(f'COMMENT_LINK_{i[0]}={i[4]}', file=gh)
