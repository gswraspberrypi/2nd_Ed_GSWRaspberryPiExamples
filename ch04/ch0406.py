import feedparser

feed_url = "http://w1.weather.gov/xml/current_obs/KPVD.rss"
feed = feedparser.parse(feed_url)
RSSitems = feed["items"]
for item in RSSitems:
    weather = item["title"]
    print weather