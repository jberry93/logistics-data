import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_countries_table_query = """
CREATE TABLE Countries(CountryName VARCHAR(20), ISO2 CHAR(2), ISO3 CHAR(3), PhoneCode VARCHAR(20), Continent VARCHAR(20), Capital VARCHAR(20), TimeZone VARCHAR(20), Currency VARCHAR(20))
"""

drop_countries_table_query = """
DROP TABLE IF EXISTS Countries
"""

create_currencies_table_query = """
CREATE TABLE Currencies(Code VARCHAR(20), Description VARCHAR(255))
"""

drop_currencies_table_query = """
DROP TABLE IF EXISTS Currencies
"""

cursor.execute(create_currencies_table_query)
print('Currencies table created')

connection.commit()
connection.close()
