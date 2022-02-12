import sqlite3

lessons = {
				
				"https://habrastorage.org/webt/r3/fo/oy/r3fooydobsk4f-s-pu0iqjz7ytk.png": 'description image_1',
				"https://i-stack-imgur-com.translate.goog/gN9W5.png?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en-US&_x_tr_pto=sc": 'description image_2',
				'https://bit.ly/3uoauz6': 'description image 3',


				}

			

conn = sqlite3.connect('cards.db')
cursor = conn.cursor()

# for i in lessons:
# 	query = "INSERT INTO 'data'(source, description) VALUES ('{}', '{}')".format(i, lessons[i])
# 	cursor.execute(query)
# conn.commit()

def get_lessons():

	les = cursor.execute("SELECT * FROM 'data'").fetchall()

	lesson = {}

	for i in les:
		lesson[i[1]] = i[2]

	return lesson

