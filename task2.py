# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

print("Утверждение ¬(X or Y or Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
for X in 0, 1:
    for Y in 0, 1:
        for Z in 0, 1:
            if not (X or Y or Z) != (not X and not Y and not Z):
                print("ложно при", f'X = {X}, Y = {Y}, Z = {Z}')
            else:
                print("истинно при", f'X = {X}, Y = {Y}, Z = {Z}')