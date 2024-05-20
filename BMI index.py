vārds = []
svars = []
augums = []
BMI = []

def formula_bmi(svars, augums):
    bmi = svars / ((augums / 100) ** 2)
    return bmi

skull = '''     ______
  .-"      "-.
 /            \ 
|              |
|,  .-.  .-.  ,|
| )(__/  \__)( |
|/     /\     \|
(_     ^^     _)
 \__|IIIIII|__/
  | \IIIIII/ |
  \          /
   `--------`'''

def kategorijas_bmi(bmi):
    if bmi < 13.00:
        return skull
    elif 13.00 <= bmi < 17.00:
        return "Psihiskās anoreksijas oficiālais rādītājs"
    elif 17.00 <= bmi < 18.00:
        return "Jums ir nepietiekams svars"
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
    elif 100 >= bmi >= 40.00:
        return "Trešās pakāpes, galēja jeb ļoti smaga aptaukošanās"
    else:
        return skull

izvēle = int(input("\nJa vēlaties uzzināt, kas ir BMI, spiediet 0.\nJa vēlaties uzzināt savu BMI rezultātu, spiediet 1.\nJa vēlaties izveidot sarakstu, kas sakārto indivīdus kategorijās pēc BMI, spiediet 2: "))

if izvēle == 0:
    print('\nBody Mass Index (BMI), jeb Ķermeņa Masas Indeks (ĶMI), jeb Kitēla indekss (indice de Quetelet)\n'
          'ir beļģu statistiķa Ādolfa Kitēla izgudrots cilvēka ķermeņa aptaukošanās rādītājs,\n'
          'ko izsaka kā svara un kvadrātā kāpināta auguma garuma attiecību.\n'
          '\nPapildus var aplūkot wikipēdijā:\n   https://en.wikipedia.org/wiki/Body_mass_index')

elif izvēle == 1:
    svars = float(input("\nKāds ir jūsu svars kilogramos? "))
    augums = float(input("Kāds ir jūsu augums centimetros? "))

    bmi = formula_bmi(svars, augums)
    print("\nJūsu BMI rezultāts ir:", '%.1f' % bmi)
    print(kategorijas_bmi(bmi))

elif izvēle == 2:
    cilv = int(input("\nJūs izvēlējāties izveidot sarakstu pēc BMI kategorijām.\nIevadiet cilvēku skaitu, kuriem jūs vēlaties izmērīt BMI: "))
    kategoriju_saraksts = {
        "Psihiskās anoreksijas oficiālais rādītājs": [],
        "Jums ir nepietiekams svars": [],
        "Normālas ķermeņa masas oficiālās robežas": [],
        "Normālas ķermeņa masas ieteicamās robežas": [],
        "Liekais svars (netiek uzskatīta par slimību)": [],
        "Pirmās pakāpes aptaukošanās": [],
        "Otrās pakāpes aptaukošanās": [],
        "Trešās pakāpes, galēja jeb ļoti smaga aptaukošanās": [],
        "Citi": []
    }
    for i in range(cilv):
        vārds_input = input("\nIevadiet personas vārdu (vai '-' lai pārtrauktu): ")
        if vārds_input == '-':
            break
        vārds.append(vārds_input)
        augums_input = float(input("Ievadiet augumu centimetros: "))
        svars_input = float(input("Ievadiet svaru kilogramos: "))
        augums.append(augums_input)
        svars.append(svars_input)
        bmi = formula_bmi(svars_input, augums_input)
        BMI.append(bmi)
        kategorija = kategorijas_bmi(bmi)
        if kategorija in kategoriju_saraksts:
            kategoriju_saraksts[kategorija].append(vārds_input)
        else:
            kategoriju_saraksts["Citi"].append(vārds_input)
    
    for kategorija, cilveki in kategoriju_saraksts.items():
        if cilveki:
            print(f"\n{kategorija}:")
            for cilveks in cilveki:
                print(f" - {cilveks}")
    
    avrg = sum(BMI) / len(BMI)
    max_index = BMI.index(max(BMI))
    min_index = BMI.index(min(BMI))
    print("\nVislielākais BMI (", '%.1f' % max(BMI), ") bija", vārds[max_index],
          "\nVismazākais BMI (", '%.1f' % min(BMI), ") bija", vārds[min_index],
          "\nVidējais BMI ir", '%.1f' % avrg)

else:
    print("Nepareiza izvēle. Jāpiež 0 vai 1, vai 2 atkarībā no jūsu vēlēšanās.")
