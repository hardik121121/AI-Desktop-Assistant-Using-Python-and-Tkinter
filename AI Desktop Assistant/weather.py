# pip install requests-html==0.10.0
# pip install lxml==4.9.1
# pip install lxml[html_clean]
# agra weather url : https://www.google.com/search?q=weather+agra
# user agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
# span id = wob_tm

from requests_html import HTMLSession

def weather():
    # Initialize an HTML session
    s = HTMLSession()

    # URL for weather query
    url = 'https://www.google.com/search?q=weather+agra'

    # Make a request to the URL with appropriate headers
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    })

    # Extract weather information using appropriate selectors
    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = r.html.find('span#wob_dc', first=True).text
    return temp + " "+ unit + " "+ desc


   