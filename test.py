import os
import sqlite3

def add(a,b):
    return a+b
    
def multiply(a,b):
    return a*b
    
def substract(a,b):
    return abs(a-b)
    
def run_command(user_input):
    os.system(user_input)

def get_user_data(user_id):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id=" + user_id  
    cursor.execute(query)
    return cursor.fetchall()
    
def slow_function(data):
    for i in data:
        for j in data:
            print(i, j)  

def inefficient_sum(data):
    result = 0
    for i in range(len(data)):
        result += sum(data)   
    return result


if __name__=='__main__':
    user = input("Enter command: ")
    run_command(user)

    user_id = input("Enter user id: ")
    get_user_data(user_id)

    slow_function([1,2,3,4])
    inefficient_sum([1,2,3,4])

    print(add(3, 2))
    print(substract(2, 3))
    print(multiply(2, 3))
