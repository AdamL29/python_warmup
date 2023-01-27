def print_this(cities : str): 
# def append?
# Below is steps 8-10
    if cities.startswith(("q","Q")):
        return "Q found: "+cities
    return "I was given this string: "+cities

cities = ["Calgary", "Edmonton", "Red Deer", "Medicine Hat", "Quebec City"]
# Below is step 4
for city in cities:
    result = print_this(city)
    print(result)

# Section 10 of warmup
def get_subs(users):
    """
    The function takes in a list of users, and returns a new list of users that is subscribed
    
    """
# Above is a description that has to be the first thing in a function.
    result = []
    for user in users:
        if user["is_sub"] == True:
            result.append(user)
    return result
#pass allows function without error when empty

def is_subs(user):
    return user['is_sub']
def filter_subs(users):
    return list(filter(is_subs, users))
    # filter goes through users and runs the function is_sub on all of them.

def lambda_subs(users):
    # lambda is the => function from JS
    return list(filter(lambda x: x['is_sub'], users))

users = [
    {
        "username" : "Adam",
        "is_sub" : True,
        "age" : 31
    },
        {
        "username" : "Timothy",
        "is_sub" : False,
        "age" : 25
    },
        {
        "username" : "Blake",
        "is_sub" : False,
        "age" : 40
    },  
]

print(get_subs(users))
print(filter_subs(users))
print(lambda_subs(users))