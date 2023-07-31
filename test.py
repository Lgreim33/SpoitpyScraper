
#POTENTIAL IMPLEMENTATION OF FETCHING<


from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.youtube.com/results?search_query=aint+it+fun+by+paramore+"
response = session.get(url)
response.html.render(sleep=1, keep_page = True, scrolldown = 2)

for links in response.html.find('a#[OFFICIAL]'):
    link = next(iter(links.absolute_links))
    print(link)