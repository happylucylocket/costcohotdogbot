import praw
import re
import math
import time

r = praw.Reddit('bot1')
subreddit = r.subreddit("vancouver")

gst = 0.05
hotdogPrice = 150 * gst + 150

def hotdogRes(signPrice):
    """
        Calculates the amount of hotdog combos purchasable from an amount of money
    """
    price = float(signPrice.replace("$", ""))*100
    amountOfHotdogs = math.floor(price/hotdogPrice)
    s = ("You can buy " + str(amountOfHotdogs) + " Costco hotdog + drink combos with " + str(signPrice) + " (including 5% GST)!")
    return s

for c in subreddit.stream.comments(skip_existing=True):
    # Read the already commented IDs
    f = open('idsResponded.txt', 'r+')
    ids = f.readlines()

    # Check for comments that contain a price value with $ and /u/CostcoHotdogBot
    match = re.search(r'\/?u\/CostcoHotdogBot', c.body) and re.search(r'\$\d+(\.\d{2})?', c.body)
    hasNotCommented = str(c.id) + '\n' not in ids
    if (hasNotCommented) and (match):
        print("MATCH FOUND\n")
        price = match.group()
        message = hotdogRes(price)
        c.reply(message)
        # Record the id of the comment the bot is leaving
        f.write(str(c.id) + '\n')
    elif (not hasNotCommented) and (match):
        print("ALREADY COMMENTED\n")
    else:
        print("NO MATCH\n")
    time.sleep(30)