"""
Get Data From API
"""

import requests as rq

respons=rq.get("https://fakestoreapi.com/products")

print(respons.json())

"""Get Data From API With Limit"""

query_params={
    "limit":4
}

response=rq.get("https://fakestoreapi.com/products",params=query_params)


# Status Code 200 define successful api hit
if(response.status_code == 200):
  print(response.json())
else:
  print(response.status_code)

"""Insert Data into Api"""

add_product={
    'id': 120,
    'title': 'Python Caps',
    'price': 20,
    'description': 'Perfect for the sunny day to wear and feel better',
    'category': "men's clothing",
    'image': 'Demo.png',
    'rating': {'rate': 4.2, 'count': 100}
}

post_data=rq.post("https://fakestoreapi.com/products",json=add_product)
print(post_data.json())

"""Update Data From Api"""

update_myprd={
    'title':'Mens Cap',
    'price': 40
}

update_data=rq.put("https://fakestoreapi.com/products/21",json=update_myprd)
print(update_data.json())

"""Delete Data From Api"""

del_data=rq.delete("https://fakestoreapi.com/products/1")
print(del_data.status_code)
print(del_data.json())

"""2nd Api with User Input"""

user_Input=input("Enter your City :")
rsp_weather=rq.get(f"https://goweather.herokuapp.com/weather/{user_Input}")

# Status Code 200 define successful api hit
if(response.status_code == 200):
  print(rsp_weather.json())
else:
  print(rsp_weather.status_code)

"""3rd API"""

rsp_currency=rq.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json")

# Status Code 200 define successful api hit
if(response.status_code == 200):
  print(rsp_currency.json())
else:
  print(rsp_currency.status_code)