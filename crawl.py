import requests
import base64
# with open("./a.jpg",'rb') as f:
#     img = base64.b64encode(f.read())
# print(img)
request_url = 'https://web.baimiaoapp.com/api/perm/single'
headers = {'x-auth-token': 'VPQ1otywNIWYYjYCLhhyUKvYqdeORPeRIvukg5OzSj5xvgmrhkyJuQMygNJm2EER',
'x-auth-uuid': '69c9a64a-aeb9-48f8-8277-6d9843c4e833'}
response = requests.post(request_url)
if response:
    print (response.json())
