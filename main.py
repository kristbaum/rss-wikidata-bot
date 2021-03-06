import pywikibot
import feedparser, json
from pywikibot import pagegenerators as pg

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
OPTIONS_FILTER_TEASER_EPISODES = False



def get_all_existing_episodes(item_id):
    QUERY = """SELECT DISTINCT ?item ?itemLabel WHERE {
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
        {
            SELECT DISTINCT ?item WHERE {
            ?item p:P179 ?statement0.
            ?statement0 (ps:P179/(wdt:P279*)) wd:%s.
            }
        }
    }
    """%(item_id)

    generator = pg.WikidataSPARQLPageGenerator(QUERY, site=site)
    for item in generator:
        episode_item = item.get()
        print(episode_item["labels"]["en"])
        print("https://wikidata.org/wiki/" + item.title())
        #print(json.dumps(episode_item["claims"], indent=4))

def process_podcast_channel_item(feed_url, item):
    d = feedparser.parse(feed_url)
    print(json.dumps(d.feed, indent=4))
    print(d.feed.keys())

    instance_of = item["claims"]["P31"][0]["main"]
    print(instance_of)

    for key in d.feed.keys():
        if key == "title":
            title = d.feed["title"]
            item["claims"]["P1476"][0].get_target()
            # https://www.wikidata.org/wiki/Q24634210


    #print(d.feed.keys)
    #print(d.feed.entries[0].keys)
    exit(0)

    channel_data = {
        "title": d.feed.title,
        "link": d.feed.link,
        "description": d.feed.description,
        "published": d.feed.published,
        "published_parsed": d.feed.published_parsed
#        "language": feed.language
    }



    entry = {
        "title": d.entries[0].title,
        "link": d.entries[0].link,
        "description": d.entries[0].description,
        "published": d.entries[0].published,
        "published_parsed": d.entries[0].published_parsed,
        "id": d.entries[0].id
    }

    print(json.dumps(entry, indent=4))




def get_feed_url(item):
    #return "https://www.ndr.de/nachrichten/info/podcast4684.xml"
    return "https://neuezwanziger.de/feed/mp3/"
    feed_url = item["claims"]["P1019"][0].get_target()
    
    print("Feed url" + feed_url)
    return feed_url

if __name__ == "__main__":
    podcast_item_id = "Q88072607"
    podcast_item = pywikibot.ItemPage(repo, podcast_item_id)
    podcast_channel_data = podcast_item.get()
    # check if there are more than one
    feed_url = get_feed_url(podcast_item_id)

    process_podcast_channel_item(feed_url=feed_url, item=podcast_channel_data)
#   get_all_existing_episodes(item_id=podcast_item_id)
    
