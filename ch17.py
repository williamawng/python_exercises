import sqlite3
con = sqlite3.connect('population.db')
cur = con.cursor()
# cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
# cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
# cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
# cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
# con.commit()
cur.execute('SELECT Region, Population, Size FROM PopByRegion')
# print(cur.fetchone())
# fetchmany() you can control the number of rows to retrieve from a db.
regions = cur.fetchall()
for region in regions:
    # print(region)
    output_text = f'The Region {region[0]} has a population of {region[1]}'
    if region[2]:
        output_text +=  f' and its size is {region[2]} million square kilometers.'
    else:
        output_text += '.'
    print(output_text)
con.close()