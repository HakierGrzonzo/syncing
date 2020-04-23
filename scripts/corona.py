import matplotlib.pyplot as plt
import datetime
przyrost = [1, 0, 4, 1, 5, 6, 5, 9, 20, 17, 36, 21, 52, 61, 49, 68, 70, 111, 98, 115, 152, 150, 170, 168, 249, 224, 193, 256, 243, 392, 437, 244, 475, 311, 435, 357, 370, 380, 401, 318, 260, 270, 380, 336, 461, 363, 545, 306, 263, 313]

i = 0
przyrost_3dni = list()
dni = list()
while True:
    try:
        przyrost_3dni.append(przyrost[i] + przyrost[i+1] + przyrost[i+2])
        dni.append(str(i) + '-' + str(i+2))
        i += 3
    except:
        break
przypadki = 0
y_axis = list()

days = list()
print('dzień\tprzypadki\tprzyrost w 3 dni')
for i in range(len(przyrost_3dni)):
    przypadki += przyrost_3dni[i]
    if przypadki > 400:
        try:
            days.append(przypadki)
            y_axis.append(round(przypadki / ( przypadki - przyrost_3dni[i]), 2))
            print(dni[i] + '.',  przypadki, '', y_axis[-1], sep = '\t')
        except:
            pass
plt.plot([3*(x - len(days) + 1) for x in range(len(days))], days, label = 'dane')
dane_range = len(days) - 1
x = float(input('Spada o mniej-więcej: '))
y = y_axis[-1]
while y > 0.9:
    y -= x
    days.append(days[-1] * y)
plt.plot([3*(x - dane_range) for x in range(dane_range, len(days))], days[dane_range:], label = 'przewidywane')
plt.ylabel('Potwierdzone przypadki')
plt.xlabel('dni, gdzie 0 to ' + datetime.date.today().isoformat() + ' plus-minus 3 dni')
plt.title('Przypadki Koronawirusa w Polsce jeśli zmiana przyrostu na 3 dni to ' + str(-x))
plt.legend()
plt.show()
