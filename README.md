# RSS-Wikidata-Bot

Regularly updates Wikidata from a set of RSS/Atom feeds.

Possible Usage:
* Podcasts
* YouTube-Channels
* Blogs
* Publications
* Other RSS-driven content

Not every episode of every podcast needs to be in WD, so use it carefully.

For example take the feed for the podcast: "Geschichten aus der Geschichte"
Its item is [Q63386294](https://www.wikidata.org/wiki/Q63386294)
Using the web feed URL [P1019](https://www.wikidata.org/wiki/Property:P1019) property it retrieves https://www.geschichte.fm/feed/mp3/

From this it can derive

# Development

`python3 -m venv venv`
`source venv/bin/activate`
`pip install poetry`
`poetry update`