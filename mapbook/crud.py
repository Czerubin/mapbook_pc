


def hello(user:str)->None:
    print(f'Witaj {user}!!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'twój znajomy {user['name']}, z {user['city']}, opublikował {user['posts']} postów')