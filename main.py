import psycopg2


def string_to_number_or_none(value):
    if value == 'null':
        return None
    elif ',' in value or '.' in value:
        try:
            value = value.replace(',', '.')
            number = float(value)
            return number
        except:
            pass
    else:  # для scale i birth
        try:
            number = int(value)
            return number
        except:
            pass

    return value


# connect to db
connect = psycopg2.connect(user="postgres", password="password", dbname="DB")
cursor = connect.cursor()

# open file
file = open(r'Odata2020File.csv', 'r')
col_names = file.readline().lower()
col_names = col_names.replace('"', '')
col_names = col_names.split(';')

# create table
first_col_name = col_names[0]
other_col_names = col_names[1:]
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS data2020(
        %s text PRIMARY KEY
    );
    """ % first_col_name
)
for col in other_col_names:
    if 'birth' in col or 'scale' in col:
        cursor.execute('ALTER TABLE data2020 ADD COLUMN %s int' % col)
    elif 'ball' in col:
        cursor.execute('ALTER TABLE data2020 ADD COLUMN %s float' % col)
    else:
        cursor.execute('ALTER TABLE data2020 ADD COLUMN %s text' % col)
connect.commit()


# insert db
for i, values in enumerate(file):
    if i == 1000:
        break

    values = values.replace('"', '')
    values = values.split(';')
    values[-1] = values[-1][:-1]

    values = [string_to_number_or_none(value) for value in values]
    query = f"INSERT INTO data2020 ({', '.join(col_names)}) VALUES ({', '.join(['%s'] * len(values))})"

    cursor.execute(query, values)
    connect.commit()

print(f"Loaded {i} rows")
