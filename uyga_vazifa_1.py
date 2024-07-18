import psycopg2

connect=psycopg2.connect(
    database="fn22",
    user="postgres",
    password="96970204",
    host="localhost",
    port=5432
)
connect.autocommit=True
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS group_(
               id serial primary key,
               title varchar(255) not null,
               status boolean not null,
               reg_date date not null
);""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS staff(
               id serial primary key,
               first_name varchar(55) not null,
               last_name varchar(55) not null,
               age int not null,
               rating numeric(4,2) not null
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id serial primary key,
               first_name varchar(55) not null,
               last_name varchar(55) not null,
               age int not null,
               rating numeric(5,2)
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS position(
               id serial primary key,
               name_ varchar(255) not null,
               status boolean not null
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS category_(
               id serial primary key,
               title varchar(255) not null,
               images varchar(555)
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_(
               id serial primary key,
               first_name varchar(55) not null,
               last_name varchar(55) not null,
               age int not null,
               rating numeric(4,2) not null

);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS product_(
               id serial primary key,
               title varchar(255) not null,
               price int not null,
               color varchar(255) not null,
               count int not null,
               category_id int not null,
               FOREIGN KEY (category_id) REFERENCES product_(id)
);""")


cursor.execute("""CREATE TABLE IF NOT EXISTS cart_(
               id serial primary key,
               user_id int not null,
               unique(user_id),
               FOREIGN KEY (user_id) REFERENCES user_(id),
               total_summa int not null,
               total_qty int not null
);""")


cursor.execute("""CREATE TABLE IF NOT EXISTS group_student(
               id serial primary key,
               group_id int not null,
               FOREIGN KEY (group_id) REFERENCES group_(id),
               student_id int not null,
               FOREIGN KEY (student_id) REFERENCES student_(id) 
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS staf_position(
               id serial primary key,
               staff_id int not null,
               FOREIGN KEY (staff_id) REFERENCES staff(id),
               position_id int not null,
               FOREIGN KEY (position_id) REFERENCES position(id)
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS c(
               id serial primary key,
               product_id int not null,
               FOREIGN KEY (product_id) REFERENCES product_(id),
               cart_id int not null,
               FOREIGN KEY (cart_id) REFERENCES cart_(id)
);""")