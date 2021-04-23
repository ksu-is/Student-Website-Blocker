import time 
from datetime import datetime as dt
# we use 'datetime' so we can set a combination of date AND time in the website restrictions
# we use the import idiom "dt" to make the code more unambigious 

hosts_path = "/etc/hosts"

redict = "127.0.0.1"
#we are working on the host file. we will be mapping hostnames of websites to our local address.

website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
# here is where you enter what websites to block.