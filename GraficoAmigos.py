import matplotlib.pyplot as plt  # plotting



def printGrrafico():

    names = []
    friends = []

    f = open('grafico.txt', 'r')

    for row in f:
        row = row.split(' ')
        names.append(row[0])
        friends.append(int(row[1]))

    plt.bar(names, friends, color='g', label='File Data')

    plt.xlabel('Student Names', fontsize=12)
    plt.ylabel('Friends', fontsize=12)

    plt.title('Students Marks', fontsize=20)
    plt.legend()

    plt.show()






