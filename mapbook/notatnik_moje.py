from tkinter import *

import requests
from bs4 import BeautifulSoup
import tkintermapview


root=Tk()
root.geometry("800x600")
root.title('mapbook')


class User:
    def __init__(self, imie, nazwsiko, postow, lokalizacja):
        self.imie = imie
        self.nazwsiko = nazwsiko
        self.postow = postow
        self.lokalizacja = lokalizacja
        self.coords:list=User.get_coordinates(self)
        self.marker=map_widget.set_marker(
            self.coords[0],
            self.coords[1],
            text=f'{self.imie}{self.nazwsiko}',
        )




    def get_coordinates(self)->list:#ta funckja zwraca liste
        url: str = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return[
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.'))
        ]


users=[
    # User('Kasia','Kowalska','7','Warszawa'),
    # User('Adam','Nowak','2','Wrocław'),
]
def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user.imie} {user.nazwsiko}{user.postow}{user.lokalizacja}')

def add_user()->None:
    name=entry_imie.get()
    surname=entry_nazwisko.get()
    posts=entry_liczba_postow.get()
    location=entry_lokalizacja.get()

    new_user=User(name,surname,posts,location)

    users.append(new_user)
    show_users()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()

def delete_user()->None:
    i=listbox_lista_obiektow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()

def edit_user()->None:
    i=listbox_lista_obiektow.index(ACTIVE)
    entry_imie.insert(0,users[i].imie)
    entry_nazwisko.insert(0,users[i].nazwsiko)
    entry_liczba_postow.insert(0,users[i].postow)
    entry_lokalizacja.insert(0,users[i].lokalizacja)

    button_dodaj_obiekt.config(text='zapisz zmiany',command=lambda:update_user(i))

def update_user(i)->None:

    users[i].imie=entry_imie.get()
    users[i].nazwsiko=entry_nazwisko.get()
    users[i].postow=entry_liczba_postow.get()
    users[i].lokalizacja=entry_lokalizacja.get()
    users[i].coords=User.get_coordinates(users[i])
    users[i].marker.delete()
    users[i].marker=map_widget.set_marker(users[i].coords[0],users[i].coords[1])

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()
    button_dodaj_obiekt.config(text='dodaj obiekt', command=add_user)
    show_users()

def show_user_details()->None:
    i = listbox_lista_obiektow.index(ACTIVE)
    label_szczegoly_imie_wartosc.config(text=users[i].imie)
    label_szczegoly_nazwisko_wartosc.config(text=users[i].nazwsiko)
    label_szczegoly_posty_wartosc.config(text=users[i].postow)
    label_szczegoly_lokalizacja_wartosc.config(text=users[i].lokalizacja)
    map_widget.set_position(users[i].coords[0],users[i].coords[1])
    map_widget.set_zoom(12)



# ramki
ramka_lista_obiektow=Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0,padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
ramka_mapa.grid(row=2, column=0,padx=50, pady=20)


#  ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektow: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=50)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly=Button(ramka_lista_obiektow,text='pokaz szczegoly', command=show_user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow,text='usun obiekt',command=delete_user)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow,text='edytuj obiekt', command=edit_user)
button_edytuj_obiekt.grid(row=2, column=2)

#obiekty wewnatrz formularza
label_formularz=Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=3)
label_imie=Label(ramka_formularz, text="Imie: ")
label_imie.grid(row=1, column=0, sticky=W)
entry_imie=Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)
label_nazwwisko=Label(ramka_formularz, text="Nazwisko: ")
label_nazwwisko.grid(row=2, column=0, sticky=W)
entry_nazwisko=Entry(ramka_formularz)
entry_nazwisko.grid(row=2, column=1)
label_liczba_postow=Label(ramka_formularz, text="Liczba postow: ")
label_liczba_postow.grid(row=3, column=0, sticky=W)
entry_liczba_postow=Entry(ramka_formularz)
entry_liczba_postow.grid(row=3, column=1)
label_lokalizacja=Label(ramka_formularz, text="Lokalizacja: ")
label_lokalizacja.grid(row=4, column=0, sticky=W)
entry_lokalizacja=Entry(ramka_formularz)
entry_lokalizacja.grid(row=4, column=1)



button_dodaj_obiekt=Button(ramka_formularz, text='dodaj obiekt', command=add_user) #dodanie funkcji guzika
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)




# ramka szczegóły obiektu - zawartość
label_szczegoly_obiektu=Label(ramka_szczegoly_obiektu, text="Szczegoly obiektu: ")
label_szczegoly_obiektu.grid(row=0, column=0,sticky=W)
label_szczegoly_imie=Label(ramka_szczegoly_obiektu, text="Imie: ")
label_szczegoly_imie.grid(row=1, column=0,sticky=W)
label_szczegoly_imie_wartosc=Label(ramka_szczegoly_obiektu, text="... ",width=10)
label_szczegoly_imie_wartosc.grid(row=1, column=1)
label_szczegoly_nazwisko=Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
label_szczegoly_nazwisko.grid(row=1, column=2)
label_szczegoly_nazwisko_wartosc=Label(ramka_szczegoly_obiektu, text="... ",width=10)
label_szczegoly_nazwisko_wartosc.grid(row=1, column=3)
label_szczegoly_posty=Label(ramka_szczegoly_obiektu, text="posty: ")
label_szczegoly_posty.grid(row=1, column=4)
label_szczegoly_posty_wartosc=Label(ramka_szczegoly_obiektu, text="... ",width=10)
label_szczegoly_posty_wartosc.grid(row=1, column=5)
label_szczegoly_lokalizacja=Label(ramka_szczegoly_obiektu, text="lokalizacja: ")
label_szczegoly_lokalizacja.grid(row=1, column=6)
label_szczegoly_lokalizacja_wartosc=Label(ramka_szczegoly_obiektu, text="... ",width=10)
label_szczegoly_lokalizacja_wartosc.grid(row=1, column=7)

map_widget=tkintermapview.TkinterMapView(ramka_szczegoly_obiektu,width=600, height=400)
map_widget.set_position(deg_x=52.0, deg_y=21)
map_widget.set_zoom(6)
map_widget.grid(row=3, column=0,columnspan=8)





root.mainloop()



# if __name__ == '__main__':
#     main()


#sdfgyui