# cv.py
# Clasa CV: nume, email, experienta + afisare (fara 'typing', fara type hints)

class CV:
    def __init__(self, nume, email, experienta=None):
        self.nume = nume
        self.email = email
        self.experienta = experienta or []

    def afiseaza_cv(self):
        print(f"=== CV: {self.nume} ===")
        print(f"Email: {self.email}")
        print("Experienta:")
        if not self.experienta:
            print("- (fara experienta)")
        for job in self.experienta:
            print(f"- {job}")