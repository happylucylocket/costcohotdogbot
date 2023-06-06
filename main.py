import praw
import re
import math

r = praw.Reddit('bot1')

subreddit = r.subreddit("testingground4bots")

gst = 0.05
hotdogPrice = 150 * gst + 150


def hotdogRes(signPrice):
    price = float(signPrice.replace("$", ""))*100
    amountOfHotdogs = math.floor(price/hotdogPrice)
    s = ("You can buy " + str(amountOfHotdogs) + " Costco hotdog + drink combos with " + str(signPrice) + " (including 5% GST)!")
    return s

for c in subreddit.stream.comments():
    match = re.search(r'/u/CostcoHotdogBot', c.body) and re.search(r'\$\d+(\.\d{2})?', c.body)
    if (match):
        price = match.group()
        message = hotdogRes(price)
        c.reply(message)
    else:
        print("NO MATCH\n")