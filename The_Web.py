# opens my favorite browsers I use on the daily

import webbrowser
import time
import re


daily_url = ["http://www.google.com"]


def open_tabs(url):
    for url in daily_url:
        for seconds in daily_url:
            time.sleep(2)
    webbrowser.open_new_tab(url)


def main():
    webbrowser.open(open_tabs("run"), new=0, autoraise=False)


main()
