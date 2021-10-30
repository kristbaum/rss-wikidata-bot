import pywikibot
import feedparser, json
from pywikibot import pagegenerators as pg


site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()



def process_podcast_channel_item(itemID):
    podcast_item = pywikibot.ItemPage(repo, itemID)
    podcast_channel_data = podcast_item.get()
    # check if there are more than one
    feed_url = get_feed_url(podcast_channel_data)
    
    d = feedparser.parse(feed_url)
    channel_data = {
        "title": d.feed.title,
        "link": d.feed.link,
        "description": d.feed.description,
        "published": d.feed.published,
        "published_parsed": d.feed.published_parsed
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
    #print(json.dumps(channel_data, indent=4))

def get_feed_url(item):
    return "https://www.ndr.de/nachrichten/info/podcast4684.xml"
    feed_json = item["claims"]["P1019"][0].toJSON()
    feed_url = feed_json["mainsnak"]["datavalue"]["value"]
    print(feed_url)
    return feed_url


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



if __name__ == "__main__":
    podcast_item_id = "Q88072607"
    #process_podcast_channel_item(podcast_item_id)
    get_all_existing_episodes(podcast_item_id)
    
