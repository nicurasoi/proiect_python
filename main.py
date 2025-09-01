# main.py

from cv import CV
from proiecte import Proiect
from contact import trimite_mesaj

# [1] CV (exact ca în exemplul tău)
# Cream o variabila 'cv' de tipul clasei CV
cv = CV(
    "Rasoi Nicușor Alexandru",
    "rasoi.nicusor.alexandru@email.com",
    ["IT Support - 2 ani", "Junior Python Dev - 1 an"]
)

cv.afiseaza_cv()

# [2] Tipuri de date primitive (str, int, float, bool)
# str -> nume/email (deja folosite mai sus)
varsta = 30               # int
rating_portofoliu = 4.8   # float
disponibil = True         # bool

print(f"\n[2] Profil: varsta={varsta} (int), rating={rating_portofoliu} (float), disponibil={disponibil} (bool)")

# [3] Structuri de date

# list (indexata, ordonata, modificabila, permite duplicate)
experiente = ["IT Support - 2 ani", "Junior Python Dev - 1 an"]

# tuple (indexata, ordonata, nemodificabila, permite duplicate)
coordonate = (45.76, 21.23)

# set (neindexat, neordonat, modificabil, fara duplicate)
tehnologii = {"Python", "Flask", "SQLite"}

# dict (indexat prin cheie, ordonat, modificabil, cheile unice)
proiect_info = {
    "titlu": "Site Portofoliu",
    "limbaj": "Python",
    "an": 2025
}

print("\n[3] Structuri de date din proiect:")
print("Lista experiente:", experiente)
print("Tuplu coordonate:", coordonate)
print("Set tehnologii:", tehnologii)
print("Dictionar proiect:", proiect_info)

# [4] if / elif / else — disponibilitate + rating
if disponibil and rating_portofoliu >= 4.5:
    print("[4] Esti disponibil si ai un rating foarte bun.")
elif disponibil:
    print("[4] Esti disponibil pentru proiecte.")
else:
    print("[4] Momentan esti indisponibil.")

# [5] if / else — major/minor
if varsta >= 18:
    print("[5] Esti major, poti incheia colaborari.")
else:
    print("[5] Esti minor.")

# [6] if / elif / else — pe numarul de experiente DIN CV (nu din lista separata)
if len(cv.experienta) == 0:
    print("[6] Nu ai inca experienta profesionala.")
elif len(cv.experienta) == 1:
    print("[6] Ai un job anterior.")
else:
    print("[6] Ai experienta profesionala solida.")

# [7] for + continue
print("\n[7] Experienta avansata (excludem pozitiile 'Junior'):")
for job in cv.experienta:
    if "Junior" in job:
        continue
    print(f"- {job}")

# [8] while + break
print("\n[8] Cautare primul job 'Junior' (while + break):")
i = 0
gasit = False
while i < len(cv.experienta):
    if "Junior" in cv.experienta[i]:
        print(f"Gasit: {cv.experienta[i]}")
        gasit = True
        break
    i += 1
if not gasit:
    print("Nu exista job 'Junior' in lista.")

print("\n---\n")

# [9] Proiecte
proiect1 = Proiect(
    "Site Portofoliu",
    "Aplicatie Python pentru prezentare CV si proiecte",
    ""  # fara link GitHub, cum ai cerut
)
proiect1.afiseaza_proiect()

print("\n---\n")

# [10] Contact — functie cu parametri numiti
trimite_mesaj(
    nume="Andrei",
    email="andrei@email.com",
    mesaj="Salut! Interesant proiectul tau!"
)