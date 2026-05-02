def add(a,b):
    return a+b
    
def multiply(a,b):
    return a*b
    
def substract(a,b):
    return abs(a-b)
    
def run_command(user_input):
    os.system(user_input)

def slow_function(data):
    for i in data:
        for j in data:
            print(i, j)  


if __name__=='__main__':
    user = input("Enter command: ")

    run_command(user)       # triggers security agent
    slow_function([1,2,3,4])  # triggers performance agent

    print(add(3, 2))
    print(substract(2, 3))
    print(multiply(2, 3))
