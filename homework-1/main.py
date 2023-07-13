"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv

import psycopg2

#  Открываем файл и достаем информацию
with open('./north_data/employees_data.csv') as f:
    list_from_employees_data = []
    data = csv.reader(f, delimiter=",")  # записываем данные в переменную
    for line in data:  # перебираем файл
        change_list_to_tuple = tuple(line)  # переводим список в кортеж
        list_from_employees_data.append(change_list_to_tuple)  # добавляем кортежи в пустой список
# Открываем файл и достаем информацию
with open('./north_data/customers_data.csv') as f:
    list_from_customers_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_customers_data.append(change_list_to_tuple)
    # Открываем файл и достаем информацию
with open('./north_data/orders_data.csv') as f:
    list_from_orders_data = []
    data = csv.reader(f, delimiter=",")
    for line in data:
        change_list_to_tuple = tuple(line)
        list_from_orders_data.append(change_list_to_tuple)

    # подключение к БД
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1234')
cur = conn.cursor()  # включить курсор
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                list_from_employees_data[1:])  # добавление данных в таблицу
cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', list_from_customers_data[1:])
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', list_from_orders_data[1:])
conn.commit()  # закоммитить

cur.close()  # закрыть курсор
conn.close()  # закрыть подключение к БД
