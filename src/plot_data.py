import matplotlib.pyplot as plt


def plot_data_on_chart(avg_fitness, best_fitness, worst_fitness):
    x = list(range(0, len(avg_fitness)))
    plt.plot(x, best_fitness)
    plt.plot(x, worst_fitness)
    plt.plot(x, avg_fitness)
    plt.xlabel('Liczba pokoleń')
    plt.ylabel('Przystosowanie')
    plt.legend(['best', 'worst', 'average'])
    plt.show()
