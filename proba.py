from tkinter import *
import tkintermapview




def main():
    def show_main_window():
        login_window.destroy()  # Zamknij okno logowania

        # Dane
        records = []  # Lista do zarządzania wydarzeniami sportowymi i uczestnikami

        class Record:
            def __init__(self, event, employee, guest, location):
                self.event = event
                self.employee = employee
                self.guest = guest
                self.location = location
                self.coordinates = self.get_coordinates()
                self.marker = map_widget.set_marker(
                    self.coordinates[0],
                    self.coordinates[1],
                    text=f'{self.event}\n'
                )


            def get_coordinates(self):
                try:
                    # Zwraca współrzędne lokalizacji, domyślnie (52.0, 21.0)
                    city_coords = {
                        "Warszawa": (52.2297, 21.0122),
                        "Kraków": (50.0647, 19.9450),
                        "Łódź": (51.7592, 19.4560),
                        "Wrocław": (51.1079, 17.0385),
                        "Poznań": (52.4064, 16.9252),
                        "Gdańsk": (54.3520, 18.6466),
                        "Szczecin": (53.4285, 14.5528),
                        "Bydgoszcz": (53.1235, 18.0084),
                        "Lublin": (51.2465, 22.5684),
                        "Białystok": (53.1325, 23.1688),
                        "Katowice": (50.2649, 19.0238),
                        "Gdynia": (54.5189, 18.5305),
                        "Częstochowa": (50.8118, 19.1203),
                        "Radom": (51.4027, 21.1471),
                        "Sosnowiec": (50.2864, 19.1046),
                        "Toruń": (53.0138, 18.5984),
                        "Kielce": (50.8661, 20.6286),
                        "Gliwice": (50.2945, 18.6658),
                        "Zabrze": (50.3244, 18.7851),
                        "Bielsko-Biała": (49.8224, 19.0464)
                    }
                    return city_coords.get(self.location, (52.0, 21.0))
                except:
                    return [52.0, 21.0]



        def clear_inputs(entries):
            for entry in entries:
                entry.delete(0, END)

        def update_listbox():
            # Aktualizuje listę wyświetlaną w listboxie.
            listbox_records.delete(0, END)
            for idx, record in enumerate(records):
                listbox_records.insert(
                    idx,
                    f"Wydarzenie: {record.event} | Pracownik: {record.employee} | Gość: {record.guest} | Lokalizacja: {record.location}"
                )

        def add_record():
            # Dodaje nowe wydarzenie, pracownika i gościa jednocześnie.
            event = entry_event.get().strip()
            employee = entry_employee.get().strip()
            guest = entry_guest.get().strip()
            location = entry_location.get().strip()

            if event and employee and guest and location:
                new_record = Record(event, employee, guest, location)
                records.append(new_record)
                update_listbox()
                clear_inputs([entry_event, entry_employee, entry_guest, entry_location])

        def delete_record():
            # Usuwa wybrany rekord z listy i mapy.
            selected_index = listbox_records.curselection()
            if selected_index:
                idx = selected_index[0]
                records[idx].marker.delete()  # Usuwanie znacznika z mapy
                records.pop(idx)  # Usuwanie z listy
                update_listbox()

        def edit_record():
            # Edytuje wybrany rekord.
            selected_index = listbox_records.curselection()
            if selected_index:
                idx = selected_index[0]
                record = records[idx]

                # Wypełnij pola edytowalnymi wartościami
                entry_event.insert(0, record.event)
                entry_employee.insert(0, record.employee)
                entry_guest.insert(0, record.guest)
                entry_location.insert(0, record.location)

                # Zmień działanie przycisku "Dodaj"
                button_add.config(text="Zapisz zmiany", command=lambda: save_changes(idx))

        def save_changes(idx):
            # Zapisuje zmiany w rekordzie.
            if entry_event.get().strip() and entry_employee.get().strip() and entry_guest.get().strip() and entry_location.get().strip():
                record = records[idx]
                record.event = entry_event.get()
                record.employee = entry_employee.get()
                record.guest = entry_guest.get()
                record.location = entry_location.get()
                record.coordinates = record.get_coordinates()

                # Aktualizacja znacznika na mapie
                record.marker.delete()
                record.marker = map_widget.set_marker(
                    record.coordinates[0],
                    record.coordinates[1],
                    text=f'{record.event}'
                )

                clear_inputs([entry_event, entry_employee, entry_guest, entry_location])
                button_add.config(text="Dodaj", command=add_record)
                update_listbox()

        # Tworzenie głównego okna
        root = Tk()
        root.geometry("1000x800")
        root.title("Zarządzanie wydarzeniemi sportowymi, pracownikami oraz gośćmi")
        root.configure(bg="#E0B0FF")

        # Mapa
        map_frame = Frame(root, bg="#4682B4")
        map_frame.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=5, pady=5)
        map_widget = tkintermapview.TkinterMapView(map_frame, width=600, height=500)
        map_widget.set_position(52.0, 21.0)
        map_widget.set_zoom(6)
        map_widget.pack(fill=BOTH, expand=True)


        # Formularz
        Label(root, text="Wydarzenie:", bg="#4B0082", fg="white").grid(row=0, column=3, sticky=W, padx=5)
        entry_event = Entry(root, width=30)
        entry_event.grid(row=0, column=4, sticky=W, padx=5)

        Label(root, text="Pracownik:", bg="#4B0082", fg="white").grid(row=1, column=3, sticky=W, padx=5)
        entry_employee = Entry(root, width=30)
        entry_employee.grid(row=1, column=4, sticky=W, padx=5)

        Label(root, text="Gość:", bg="#4B0082", fg="white").grid(row=2, column=3, sticky=W, padx=5)
        entry_guest = Entry(root, width=30)
        entry_guest.grid(row=2, column=4, sticky=W, padx=5)

        Label(root, text="Lokalizacja:", bg="#4B0082", fg="white").grid(row=3, column=3, sticky=W, padx=5)
        entry_location = Entry(root, width=30)
        entry_location.grid(row=3, column=4, sticky=W, padx=5)

        button_add = Button(root, text="Dodaj", command=add_record, bg="#4B0082", fg="white", width=15)
        button_add.grid(row=4, column=4, columnspan=2, pady=5)

        Button(root, text="Usuń", command=delete_record, bg="#4B0082", fg="white", width=15).grid(row=5, column=4, columnspan=2, pady=5)
        Button(root, text="Edytuj", command=edit_record, bg="#4B0082", fg="white", width=15).grid(row=6, column=4, columnspan=2, pady=5)

        # Lista rekordów
        Label(root, text="Lista rekordów:", bg="#4B0082", fg="white").grid(row=7, column=0, sticky=W, padx=5)
        listbox_records = Listbox(root, width=100, height=10, bg="#E0FFFF", fg="black")
        listbox_records.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

        root.mainloop()

    # Okno logowania`
    login_window = Tk()
    login_window.geometry("400x200")
    login_window.title("Logowanie")
    login_window.configure(bg="#4B0082")

    Label(login_window, text="Login:", bg="#4B0082", fg="white").pack(pady=5)
    login_entry = Entry(login_window)
    login_entry.pack()

    Label(login_window, text="Hasło:", bg="#4B0082", fg="white").pack(pady=5)
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    Button(login_window, text="Zaloguj", command=show_main_window, bg="#4B0082", fg="white").pack(pady=10)
    login_window.mainloop()


if __name__ == '__main__':
    main()