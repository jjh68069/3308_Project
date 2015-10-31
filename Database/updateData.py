#this file can be run to update the information in the database
#it will get the most recent from quandl.
#refer to this article for how to access data in the database: https://docs.python.org/2/library/sqlite3.html

import sqlite3
conn = sqlite3.connect('stocks.db')
