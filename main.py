# from mapbook.map_functions import single_user_map, multi_user_map
# from mapbook.users import users
# from mapbook.crud import hello, read_users, add_user, remove_user, update_user

from tkinter import *

import tkintermapview






class User:
    def __init__(self,imie, nazwisko, postow, lokalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.postow = postow
        self.lokalizacja = lokalizacja

users = [
    User('aaa', 'aaa', '1','aaa'),
    User('bbb', 'bbb', '2','bbb'),
    User('ccc', 'ccc', '3','ccc'),
]
def show_users():

    for idx, user in enumerate (users):
        listbox_lista_obiektow.insert(idx, user.imie)




root=Tk()
root.geometry("800x600")
root.title('mapbook')


#ramki
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)


ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, padx=50, pady=20, columnspan=2)

ramka_mapa = Frame(root)
ramka_mapa.grid(row=2, column=0, padx=50, pady=20)

# ramka lista obiektów
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=50)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text="Pokaz szczegoly", command=lambda:print('aaa'))
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usun obiekt")
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj obiekt")
button_edytuj_obiekt.grid(row=2, column=2)

#  obiekty wewnątrz formularza
label_formularz = Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=3)
label_imie = Label(ramka_formularz, text="Imie: ")
label_imie.grid(row=1, column=0,sticky=W)
entry_imie = Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_nazwisko.grid(row=2, column=0,sticky=W)
entry_nazwisko = Entry(ramka_formularz)
entry_nazwisko.grid(row=2, column=1)
label_liczba_postow = Label(ramka_formularz, text="Liczba postow: ")
label_liczba_postow.grid(row=3, column=0,sticky=W)
entry_liczba_postow = Entry(ramka_formularz)
entry_liczba_postow.grid(row=3, column=1)
label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")
label_lokalizacja.grid(row=4, column=0,sticky=W)
entry_lokalizacja = Entry(ramka_formularz)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text="Dodaj obiekt")
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)



# ramka szczegoly obiektow - zawartosc
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegoly obiektu: ")
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_szczegoly_imie = Label(ramka_szczegoly_obiektu, text="Imie: ")
label_szczegoly_imie.grid(row=1, column=0, sticky=W)
label_szczegoly_imie_wartosc = Label(ramka_szczegoly_obiektu, text="... ", width=10)
label_szczegoly_imie_wartosc.grid(row=1, column=1)
label_szczegoly_nazwisko = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
label_szczegoly_nazwisko.grid(row=1, column=2)
label_szczegoly_nazwisko_wartosc = Label(ramka_szczegoly_obiektu, text="... ", width=10)
label_szczegoly_nazwisko_wartosc.grid(row=1, column=3)
label_szczegoly_posty = Label(ramka_szczegoly_obiektu, text="Posty: ")
label_szczegoly_posty.grid(row=1, column=4)
label_szczegoly_posty_wartosc = Label(ramka_szczegoly_obiektu, text="... ", width=10)
label_szczegoly_posty_wartosc.grid(row=1, column=5)
label_szczegoly_lokalizacja = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")
label_szczegoly_lokalizacja.grid(row=1, column=6)
label_szczegoly_lokalizacja_wartosc = Label(ramka_szczegoly_obiektu, text="... ", width=10)
label_szczegoly_lokalizacja_wartosc.grid(row=1, column=7)

map_widget=tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=600, height=400)
map_widget.set_position(deg_x=52.0,deg_y=21)
map_widget.set_zoom(6)
map_widget.grid(row=3, column=0, columnspan=8)

show_users ()


root.mainloop()




# if __name__ == '__main__':
#     main()


