# opens my favorite sites I use daily

import webbrowser
import time
import re


daily_url = ["http://www.google.com", "http://www.gmail.com", "http://www.youtube.com"]


def open_tabs(url):
    for url in daily_url:
        for seconds in daily_url:
            time.sleep(2)
    webbrowser.open_new_tab(url)


def main():
    webbrowser.open(open_tabs("run"), new=1, autoraise=False)
    


main()
