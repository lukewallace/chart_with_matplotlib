import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('test.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))

plt.plot(x, y, color='g', linestyle='dashed',
         marker='o', label="Values")

plt.xticks(rotation=25)
plt.xlabel('date')
plt.ylabel('value')
plt.title('Data Report', fontsize=20)
plt.grid()
plt.legend()
plt.show()
