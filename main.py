from mapbook.users import users
from mapbook.crud import hello, read_users, add_user, remove_user, update_user


def main():
    hello(users[0]['name'])
    read_users(users)
    # add_user(users)
    # remove_user(users)
    update_user(users)
    read_users(users)
#help

if __name__ == '__main__':
    main()


#asdfg
