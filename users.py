import requests

total_results = 5
fields = "name,gender,dob,email"

# peticion get
url = "https://randomuser.me/api/?results={results}&inc={fields}".format(
    results=total_results,
    fields=fields)
results = requests.get(url).json()

# se extraen los datos
users = []
for res in results['results']:

    """
        Almacenamos cada valor necesario del diccionario
        en una variable.
    """
    title = res['name']['title']
    first = res['name']['first']
    last = res['name']['last']
    full_name = "{} {} {}".format(title, first, last)
    age = res['dob']['age']
    gender = res['gender']
    email = res['email']
    """
        Para un mejor tratamiento generamos un nuevo
        diccionario con los datos
    """
    users.append({"name": full_name,
                  "age": age,
                  "gender": gender,
                  "email": email})
    """
        Ordena por edad descendente
    """
    users.sort(key=lambda x: x['age'], reverse=True)

# se crea excel
for user in users:
    print("{} {} {}".format(user['gender'], user['name'], user['age']))
