
"""## SQL light"""

import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER
);"""

con = sqlite3.connect('mydata.sqlite3')

con.execute(query)

con.commit()

data = [('Atlanta','Georgia', 1.25,6),
       ('Tallahassee','Florida', 2.6,3),
       ('Scramento','California', 1.7,5)]

stmt = "Insert into test Values(?, ?, ?, ?)"

con.executemany(stmt, data)

con.commit()

import sqlalchemy as sqla

db = sqla.create_engine('sqlite:///mydata.sqlite')
