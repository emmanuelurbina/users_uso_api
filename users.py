import requests
import xlsxwriter

# generamos libro y hoja de excel
book = xlsxwriter.Workbook('usuarios.xlsx')
sheet = book.add_worksheet()
# columna y fila en 0
row = 0
col = 0
# variables
total_results = 100
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

sheet.write(row, col, "Genero")
sheet.write(row, col + 1, "Nombre")
sheet.write(row, col + 2, "Email")
sheet.write(row, col + 3, "Edad")
# se crea excel
for user in users:
    name = user['name']
    age = user['age']
    gender = user['gender']
    email = user['email']
    row += 1
    sheet.write(row, col, gender)
    sheet.write(row, col + 1, name)
    sheet.write(row, col + 2, email)
    sheet.write(row, col + 3, age)
    # Se imprimen los resultados igual como en el archivo
    print("{} {} {} {}".format(gender, name, email, age,))

book.close()
