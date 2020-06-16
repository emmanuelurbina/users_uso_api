import requests
url = "https://randomuser.me/api/?results=100"

results = requests.get(url)
i = 0
for res in results.json()['results']:
    i += 1
    title = res['name']['title']
    first = res['name']['first']
    last = res['name']['last']
    gender = res['gender']
    email = res['email']
    age = res['dob']['age']
    print("{i} {gender} {title} {first} {last} {email} {age}".format(
        i=i,
        gender=gender,
        title=title,
        first=first,
        last=last,
        email=email,
        age=age))
