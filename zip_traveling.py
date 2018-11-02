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

import csv                                      # csv module that will help read files
import sched, time                              # sched module implements a general purpose event scheduler.
from queue import PriorityQueue                 # implements priority queue


class ZipScheduler:

    # order_queue = PriorityQueue()
    list_of_order = []

    def read_order(file):
        order_list = ZipScheduler.list_of_order                         # init an empty that store order read from the csv file 
        with open(file, 'r') as csvfile:
            reader_order = csv.reader(csvfile)  # expect values to be separated by a coma by default
            # next(reader)                      # skip the first line if we had title on the csv file
            for line in reader_order:           
                # add extra operation for 'Resupply' and 'Emergency' priority
                order_list.append(line)
        return order_list

    ## we are going to check for each order in the file. add order on top of the list if it has Emergency 
    ## priority and the largest number of second(meaning an order was made earlier than an other)
    
    def store_order(file):
        orders = ZipScheduler.read_order(file)
        for i in range(len(orders)):
            return (orders[i])
            #for j in range(len(orders[i])):
                #print(orders[i][j])    

    #def queue_order(received_time, hospital, priority):
    def queue_order():
        orders = ZipScheduler.list_of_order
        for item in orders:
            print(item[2])

    def schedule_next_flight(current_time):
        print('add operation for next schedule')
        pass
        
    def schedule_flight(): 
        print("call schedule next flight function every 60 sec")
        # call function here
        #ZipScheduler.schedule_next_flight()
        time.sleep(60)

while True:
    ZipScheduler.schedule_flight()

#ZipScheduler.store_order('orders.csv')
#ZipScheduler.queue_order()
# print(ZipScheduler.read_order('hospitals.csv'))


                
