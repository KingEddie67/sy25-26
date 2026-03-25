F1 = ["F1", "W Off-Road-Rug", (185, 142), 6000, 9, 1880, 4]
A1 = ["A1", "Toyota-Corolla-WRC", (177, 140), 5500, 8, 1230, 4]
B1 = ["B1", "Seat-Cordoba-WRC", (176, 139), 5400, 8, 1240, 4]
C1 = ["C1", "Subaru-Impreza-WRC", (180, 143), 5800, 9, 1270, 4]
D1 = ["D1", "Mitsubishi-Lancer-WRC", (178, 141), 5700, 8, 1260, 4]
E1 = ["E1", "Ford-Focus-WRC", (179, 142), 5600, 8, 1250, 4]
G1 = ["G1", "Citroen-C4-WRC", (181, 144), 5900, 9, 1280, 4]
H1 = ["H1", "Peugeot-207-WRC", (175, 138), 5300, 8, 1220, 4]
I1 = ["I1", "Skoda-Fabia-WRC", (174, 137), 5200, 8, 1210, 4]
J1 = ["J1", "Mini-Cooper-WRC", (173, 136), 5100, 8, 1200, 4]

cars = [F1, A1, B1, C1, D1, E1, G1, H1, I1, J1]

def print_car(c):
    lines = [
        f" {c[0]}",
        f" Model: {c[1]}",
        f" Speed: {c[2][0]} / Acceleration: {c[2][1]}",
        f" Price: ${c[3]}",
        f" Handling: {c[4]}",
        f" Weight: {c[5]} kg"
    ]
    width = max(len(line) for line in lines) + 2
    print("+" + "-" * width + "+")
    for line in lines:
        print("|" + line.ljust(width) + "|")
    print("+" + "-" * width + "+")

i = 1
for car in cars:
    print(i, car[1])
    i += 1


carnum = int(input("Select your car (1-10: "))
print(f"You selected car number {carnum}: ")
print_car(cars[carnum - 1])