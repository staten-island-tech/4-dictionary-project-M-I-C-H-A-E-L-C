x = []
price = 0
item = [
{
    "name": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps",
    "price": 130.99000000000000000000013,
    "department": "Televisions",
    "mass": "1 solar mass, maybe like 55 pounds?",
    "description": "Bundle of 17 eggs"
},
{
    "name": "costo hot chicken dog",
    "price": 1.99,
    "department": "Laundry Aisle",
    "mass": "10 KG",
    "description": "Chimken fud"
},
{
    "name": "Cat fud",
    "price": 3.99,
    "department": "Laundry Aisle",
    "mass": "10 Grams",
    "description": "Very health for dogi"
},
{    
    "name": "Empire state building",
    "price": 11.99,
    "department": "Laundry Aisle",
    "mass": "365,000,000,000.12389821398128490 Grams",
    "description": "Big buildin"
},
{    
    "name": "Linkedin",
    "price": 13.99,
    "department": "Construction tols",
    "mass": "??? ",
    "description": "Big moneh"
}]
print("Hi, dis me store. Good stuff. Very Chep")
print(item[0]["name"])
print(item[1]["name"])
print(item[2]["name"])
print(item[3]["name"])
print(item[4]["name"])
z = input("What would you like to purchase? Or exit to purchase items in cart.:")

while z != "exit": 
    if z == "55-inch Ultra HD Smart TV with HDR and built-in streaming apps":
        print("55-inch Ultra HD Smart TV with HDR and built-in streaming apps, Added to Cart")
        x.append(item[0]["name"]) 
        price += item[0]["price"]
    elif z == "costo hot chicken dog":
        print("costo hot chicken dog, Added to Cart")
        x.append(item[1]["name"]) 
        price += item[1]["price"]
    elif z == "Cat fud":
        print("Cat fud, Added to Cart")
        x.append(item[2]["name"]) 
        price += item[2]["price"]
    elif z == "Empire state building":
        print("Empire state building, Added to Cart")
        x.append(item[3]["name"]) 
        price += item[3]["price"]
    elif z == "Linkedin":
        print("Linkedin, Added to Cart")
        x.append(item[4]["name"]) 
        price += item[4]["price"]
    z = input("What would you like to purchase? Or exit to purchase items in cart.:")

print("Cart:" ,x)
print("Total:",price)