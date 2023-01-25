import mouse
import time
import datetime
from pymongo import MongoClient

class MouseMove:

    cluster = "" #insert your connection string here
    client = MongoClient(cluster)

    db = client.MouseTracker #name of your database
    global timeStamps #name of your collection

    clicks = 0 #the amount of clicks will be stored here
    start = 0 #start counting the time
    DELTATIME = 5 #determines the seconds between two insertions
    UPPERBOUND = 10 #upper limit for clicks within delta time

    def postClicks(clicks):
        timeStamps.insert_one({"date" : datetime.datetime.now(), "number" : clicks})  

    if __name__ == "__main__":

        timeStamps = db.timeStamps
        start = time.time()  #store current time

        while(True):
            if (time.time() - start) >= DELTATIME:  #once deltatime is over, insert into database
                postClicks(clicks)
                clicks = 0
                start = time.time()
            if mouse.is_pressed(button='left') and clicks <= UPPERBOUND: #increase counter for every click if it hasn't reached the upper bound
                clicks += 1 
                time.sleep(0.1)
            time.sleep(0.01)
