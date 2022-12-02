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
    """ % (item_id)

    generator = pg.WikidataSPARQLPageGenerator(QUERY, site=site)
    for item in generator:
        episode_item = item.get()
        print(episode_item["labels"]["en"])
        print("https://wikidata.org/wiki/" + item.title())
        #print(json.dumps(episode_item["claims"], indent=4))
