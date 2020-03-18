import random
from  sqlalchemy import create_engine
import pandas as pd
import psycopg2
conn = psycopg2.connect(host='localhost', user='piotr', password='2050', database='fifawebsite')
cursor = conn.cursor()


engine = create_engine('postgresql://piotr:2050@localhost:5432/fifawebsite')

users = list(range(1, 301))
ratings = [1, 2, 3, 4, 5]
rated = []


'''
GENERATE DUMMY RATING DATA FOR CAM PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "cam"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(1, 10001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]



    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue

'''
GENERATE DUMMY RATING DATA FOR CB PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "cb"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(10001, 20001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR CDM PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "cdm"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(20001, 30001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR CF PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "cf"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(30001, 40001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR CM PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "cm"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(40001, 50001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR GK PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "gk"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(50001, 60001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR LB PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "lb"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(60001, 70001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR LM PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "lm"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(70001, 80001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR LW PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "lw"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(80001, 90001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR LWB PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "lwb"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(90001, 100001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR RB PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "rb"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(100001, 110001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR RM PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "rm"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(110001, 120001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR RW PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "rw"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(120001, 130001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR RWB PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "rwb"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(130001, 140001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue


'''
GENERATE DUMMY RATING DATA FOR ST PLAYERS
'''
df = pd.read_sql_query('select sofifa_id, player_positions from "st"', con=engine)
fifa_id = df['sofifa_id']
# print(len(fifa_id))

for i in range(140001, 150001):
    user = random.choice(users)
    rating = random.choice(ratings)
    player_id = int(random.choice(fifa_id))
    position = df['player_positions'][0]

    # users can't double rate a player
    if (user, player_id, position) not in rated:
        rated.append((user, player_id, position))
        print("rating_id {}: user_id {} rated playerid {} position {} a rating of {}".format(i, user, player_id, position, rating))
        cursor.execute(
            "INSERT INTO ratings (id, user_id, sofifa_id, player_position, user_rating) VALUES(%s, %s, %s, %s, %s)",
            (i, user, player_id, position, rating))
        conn.commit()
    else:
        print("Can't double rate")
        continue

cursor.close()
conn.close()