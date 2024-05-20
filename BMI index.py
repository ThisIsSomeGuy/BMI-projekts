vārds = []
svars = []
augums = []
BMI = []

def formula_bmi(svars, augums):
    bmi = svars / ((augums/100) ** 2)
    return bmi

skull ='     ______\n  .-"      "-.\n /            \ \n|              |\n|,  .-.  .-.  ,|\n| )(__/  \__)( |\n|/     /\     \|\n(_     ^^     _)\n \__|IIIIII|__/\n  | \IIIIII/ |\n  \          /\n   `--------`'

def kategorijas_bmi(bmi):
    if bmi < 13.00:
        return skull
    elif 13.00 <= bmi < 17.00:
        return "Psihiskās anoreksijas oficiālais rādītājs"
    elif 17.00 <= bmi < 18.00:
        return "jums ir nepietiekams svars"
    elif 18.00 <= bmi < 20.00:
        return "Normālas ķermeņa masas oficiālās robežas"
    elif 20.00 <= bmi < 25.00:
        return "Normālas ķermeņa masas ieteicamās robežas"
    elif 25.00 <= bmi < 30.00:
        return "Liekais svars (netiek uzskatīta par slimību)"
    elif 30.00 <= bmi < 35.00:
        return "Pirmās pakāpes aptaukošanās"
    elif 35.00 <= bmi < 40.00:
        return "Otrās pakāpes aptaukošanās"
    elif bmi >= 40.00:
        return "Trešās pakāpes, galēja jeb ļoti smaga aptaukošanās"
    else: return skull

izvēle = int(input("\nJa vēlaties uzzināt, kas ir BMI spiediet 0.\nJa vēlaties uzzināt savu BMI rezultātu, spiediet 1. \nJa vēlaties izveidot sarakstu, kas sakārto indivīdus kategorijās pēc BMI, spiediet 2: ")) # 0 - lietotājs var uzzināt papildus par BMI

if izvēle == 0:
    print('\nBody Mass Index(BMI), jeb Ķermeņa Masas Indeks(ĶMI), jeb Kitēla indekss (indice de Quetelet)\nir beļģu statistiķa Ādolfa Kitēla izgudrots cilvēka ķermeņa aptaukošanās rādītājs,\nko izsaka kā svara un kvadrātā kāpināta auguma garuma attiecību. \n\nPapildus var aplūkot wikipēdijā:\n   https://en.wikipedia.org/wiki/Body_mass_index')

elif izvēle == 1:
    svars = float(input("\nKāds ir jūsu svars kilogramos? "))
    augums = float(input("Kāds ir jūsu augums centmetros? "))

    bmi = formula_bmi(svars, augums)
    print("\nJūsu BMI rezultāts ir:", '%.1f' % bmi)
    print(kategorijas_bmi(bmi))

    
elif izvēle == 2:
    cilv = int(input("\nJūs izvēlējāties izveidot sarakstu pēc BMI kategorijām. \nIevadiet cilvēku skaitu, kuriem jūs vēlaties izmērīt BMI: "))
    for i in range(cilv):
        vārds.append(input("\nIevadiet personas vārdu (vai '-' lai pārtrauktu): "))
        if vārds[i] == '-':
            break
        augums.append(float(input("Ievadiet augumu centimetros: ")))
        svars.append(float(input("Ievadiet svaru kilogramos: ")))
        BMI.append(formula_bmi(svars[i], augums[i]))
    avrg = sum(BMI)/len(BMI)
    max_index = BMI.index(max(BMI))
    min_index = BMI.index(min(BMI))
    print("\nVislielākais BMI( "'%.1f' % max(BMI), ") bija ",vārds[max_index],"\nvizmazākais BMI( ", '%.1f' % min(BMI),") bija",vārds[min_index],"\nVidējais BMI ir ", '%.1f' % avrg)
    
else:
    print("Nepareiza izvēle. Jāpiež 0 vai 1, vai 2 atkarībā no jūsu vēlēšanās.")

    



