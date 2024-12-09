from mapbook.map_functions import single_user_map, multi_user_map
from mapbook.users import users
from mapbook.crud import hello, read_users, add_user, remove_user, update_user


def main():
    hello(users[0]['name'])
    while True:
        print('======MENU======')
        print('0. Wyjście z programu')
        print('1. Dodaj znajomego')
        print('2. Wczytaj znajomych')
        print('3. Aktualizuj znajomego')
        print('4. Usuń znajomego')
        print('5. Generuj mapę z lokalizacją znajomego')
        print('6. Generuj mapę z lokalizacją wszystkich znajomych')

        menu_option: str = input('Użytkowniku wybierz opcję menu: ')
        print(f'Użytkownik wybrał {menu_option}')
        if menu_option == '0':
            break
        if menu_option == '1':
            add_user(users)
        if menu_option == '2':
            read_users(users)
        if menu_option == '3':
            update_user(users)
        if menu_option == '4':
            remove_user(users)
        if menu_option == '5':
            single_user_map(users)
        if menu_option == '6':
            multi_user_map(users)


if __name__ == '__main__':
    main()


