# proiecte.py
# Clasa Proiect: titlu, descriere, link + afisare (fara 'typing')

class Proiect:
    def __init__(self, titlu, descriere, link=""):
        self.titlu = titlu
        self.descriere = descriere
        self.link = link  # poate fi gol ("") daca nu vrem link

    def afiseaza_proiect(self):
        print(f"Proiect: {self.titlu}")
        print(f"Descriere: {self.descriere}")
        if self.link:
            print(f"Link: {self.link}")