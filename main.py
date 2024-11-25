users:list=[
    {'name':'Patrycja','posts':1,'city':'Warszawa'},
    {'name':'Dominik','posts':3,'city':'Poznań'},
    {'name':'Szymon z wąsem','posts':5,'city':'Toruń'},
    {'name':'Szymon','posts':7,'city':'Łódź'},
    {'name':'Patryk','posts':9,'city':'Kielce'},
    {'name':'Żerom','posts':10,'city':'Katowice'},
    {'name':'Michał','posts':11,'city':'Zielona Góra'},
    {'name':'Dominik','posts':12,'city':'Szczecin'},
    {'name':'Kinga','posts':13,'city':'Bydgoszcz'},
    {'name':'Aleksandra','posts':14,'city':'Gdańsk'},


]

print (f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'twój znajomy {user['name']}, z {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {posow[idx]} postów')
