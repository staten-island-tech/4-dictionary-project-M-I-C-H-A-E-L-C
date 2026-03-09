x = []
y = 0
item = [item1, item2, item3, item4, item5:]
item1 = {
    "name": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps",
    "price": 130.99000000000000000000013,
    "department": "Televisions",
    "mass": "1 solar mass, maybe like 55 pounds?",
    "description": "Bundle of 17 eggs"
},
item2 = {
    "name": "costo hot chicken dog",
    "price": 1.99,
    "department": "Laundry Aisle",
    "mass": "10 KG",
    "description": "Chimken fud"
},
item3 = {
    "name": "Cat fud",
    "price": 3.99,
    "department": "Laundry Aisle",
    "mass": "10 Grams",
    "description": "Very health for dogi"
},
item4 = {    
    "name": "Empire state building",
    "price": 11.99,
    "department": "Laundry Aisle",
    "mass": "365,000,000,000.12389821398128490 Grams",
    "description": "Big buildin"
},
item5 = {    
    "name": "Linkedin",
    "price": 13.99,
    "department": "Construction tols",
    "mass": "??? ",
    "description": "Big moneh"
} 
print("Hi, dis me store. Good stuff. Very Chep")
print(item1[0]["name"])
print(item2[0]["name"])
print(item3[0]["name"])
print(item4[0]["name"])
print(item5["name"])
z = input("What would you like to purchase? Or exit to purchase items in cart.:")

while z != "exit": 
    if z == "Cat fud":
        print("Cat fud, Added to Cart")
        x.append(item1[0]["name"]) 
    elif z == "55-inch Ultra HD Smart TV with HDR and built-in streaming apps":
        print("55-inch Ultra HD Smart TV with HDR and built-in streaming apps, Added to Cart")
        x.append(item2[0]["name"]) 
    elif z == "costo hot chicken dog":
        print("costo hot chicken dog, Added to Cart")
        x.append(item3[0]["name"]) 
    elif z == "Empire state building":
        print("Empire state building, Added to Cart")
        x.append(item4[0]["name"]) 
    elif z == "Linkedin":
        print("Linkedin, Added to Cart")
        x.append(item5["name"]) 
    z = input("What would you like to purchase? Or exit to purchase items in cart.:")
