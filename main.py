import pywikibot
import feedparser
import json
from pywikibot import pagegenerators as pg
import logging
import pprint

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
OPTIONS_FILTER_TEASER_EPISODES = False


def get_podcast_item(qid):
    logging.info("Starting wikidata rss bot with: " + podcast_item_id)

    podcast_item = pywikibot.ItemPage(repo, podcast_item_id)
    podcast_item.get()
    if 'en' in podcast_item.labels:
        logging.info("Download item page " + podcast_item.labels['en'])

    logging.info(podcast_item)

    if podcast_item.claims:
        if 'P31' in podcast_item.claims:  # instance of
            #print(podcast_item.claims['P31'][0].getTarget())
            # let's just assume it has sources.
            #print(podcast_item.claims['P31'][0].sources[0])
            pass

    return podcast_item


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    podcast_item_id = "Q63386294"
    podcast_item = get_podcast_item(podcast_item_id)
    logging.info("Get Feed")
    print(podcast_item.get_best_claim("P1019"))
    for claim in podcast_item["claims"]["P1019"]:
        pass
    logging.info(json.dumps(podcast_item["claims"]["P1019"]))
    #logging.info("Content of feed: " + podcast_item["claims"]["P1019"])
    #feed_url = podcast_item["claims"]["P1019"][0].get_target()

    #process_podcast_channel_item(feed_url=feed_url, item=podcast_channel_data)
#   get_all_existing_episodes(item_id=podcast_item_id)
