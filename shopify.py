import requests

revenue = 0
pageNum = 1

def getJSON(num):
    url = 'https://shopicruit.myshopify.com/admin/orders.json'
    url_params = {'page': num, 'access_token': 'c32313df0d0ef512ca64d5b336a0d7c6'}
    response = requests.get(url, params=url_params).json()
    return response

while (len(getJSON(pageNum)['orders']) != 0):
     response = getJSON(pageNum)

     for order in response['orders']:
         revenue += float(order['total_price'])

     pageNum += 1

print("The total order revenue is $" + str(revenue))
