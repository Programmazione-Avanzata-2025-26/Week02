class Car:
    # COSTRUTTORE: COSTRUISCE L'OGGETTO
    # DEFINENDO I SUOI ATTRIBUTI ED INIIZIALIZZANDOLI
    def __init__(self):
        self.licensePlate = 0
        self.bodyColor = ''
        self.turnedOn = False

    # POSSO DEFINIRE NELLA CLASSE ALTRE FUNZIONI CHE
    # OPERANO SUI DATI
    def paint(self, color):
        self.bodyColor = color # Cambio colore

    def turnOn(self):
        self.turnedOn = True

c = Car()

# POSSO ACCEDERE AGLI ATTRIBUTI DELL'OGGETTO c
# CON LA NOTAZIONE PUNTATA, IN SCRITTURA E LETTURA

c.licensePlate = "AB123CD"
print(c.licensePlate)

c.paint("red")
print(c.bodyColor)


