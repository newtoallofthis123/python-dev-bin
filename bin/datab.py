import sqlite3

# Connecting to the database
conn = sqlite3.connect('database.db')

# Creating a cursor for operating in the database. This is will act as a literal cursor
c = conn.cursor()

# Creating a table
# c.execute("""CREATE TABLE starWars(
    # name text,
    # type text,
    # role text
# )""")

# Types of datatypes: NULL, INTEGER, REAL, TEXT, BLOB

# Insert data in the datasbase
# c.execute("INSERT INTO starWars VALUES ('Luke SkyWalker', 'Human', 'Jedi')")

# To Insert with dict:
# characters = [
    # ('Anakin SkyWalker', 'Human', 'DarthVader'),
    # ('Yoda', 'Maldorian', 'Jedi'),
# ]
# c.executemany("INSERT INTO starWars VALUES (?,?,?)", characters)

# To update Records
c.execute(""" UPDATE starWars SET type = "Human"
    WHERE rowid = 1


""")

# Commit the command
conn.commit()

# To Query the database:
c.execute('SELECT * FROM starWars')

# To get rowid also:
# c.execute('SELECT rowid, * FROM starWars')

# To get specific stuff:
# c.execute("SELECT * FROM starWars WHERE type = 'Human'")

# Fetch the values:
# c.fetchone()
# c.fetchmany()
print(c.fetchall())

# To delete:
# c.execute("DELETE from starWars WHERE rowid=5")

# To query with ORDER-BY by decending
# c.execute('SELECT rowid, * FROM starWars ORDER BY rowid DESC')

# To query with ORDER-BY by ascending
# c.execute('SELECT rowid, * FROM starWars ORDER BY rowid')

# To select Specific
# c.execute('SELECT rowid, * FROM starWars WHERE type LIKE 'DR%' AND rowid = 3)

# Commit the command
conn.commit()

# Close the connection, just to be safe
conn.close()
