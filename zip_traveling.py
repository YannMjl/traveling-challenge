#------------------------------------------------------------------------------------------------------#
# At a Zipline operations center, we want to deliver many different types of products to many
# different hospitals using our fleet of autonomous planes (we call them "Zips"). In order to
# provide the best overall experience to our customers, we always want to minimize the
# time-to-deliver. That said, some of our orders are "Emergency" deliveries, which have the
# potential to be life-saving, whereas other orders are "Resupply" deliveries, leaving us some
# flexibility in delivery time.

# The reality is that Zips are a finite resource, and so we need to be more clever than immediately
# sending out a Zip as each order comes in. To help manage these logistics, the purpose of this
# exercise will be to write a ZipScheduler utility (preferably in python), to determine when and to
# which hospitals we should send out Zips for delivery.

# To make things more interesting, we will also allow each Zip to carry multiple packages at a
# time. This means that a Zip can fly a route, delivering to several hospitals along the way,
# although Zips are still limited by the cumulative distance they can fly on a given trip.
#------------------------------------------------------------------------------------------------------#

# solution concept:
# tradeoff: oder priority over distance since there is a potential life saving
# scenario for emergency orders

# 1. we going to start by reading orders and separate them by level of priority
# 2. from there we going to schedule the next flight for each order (considering that
# each flight can supply 3 orders within a maximum cummulative range of 164km)

# we are going to use a queue to store order after reading them (meaning first order in,
# will be the first order out)

# import the csv module that will help read and get data from the input files
import csv
from queue import PriorityQueue

class ZipScheduler:

    order_queue = PriorityQueue()

    def hospitals_location(file):
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # expect values to be separated by a coma by default
            # next(reader)                    # skip the first line if we had title on the csv file
            for line in reader:
                return line

ZipScheduler.hospitals_location('hospitals.csv')

                