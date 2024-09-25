# Lista med tal vars gångertabeller vi vill skriva ut
talen = [2, 7, 4]

# Loopar genom varje tal i listan
for tal in talen:
    print(f"Gånger-tabellen för {tal}:")
    for i in range(1, 11):
        produkt = tal * i
        print(f"{tal} x {i} = {produkt}")
    print()  # Tom rad mellan gångertabellerna