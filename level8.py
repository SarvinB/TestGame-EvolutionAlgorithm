from evolution_algorithm import Evolution
import numpy as np
import matplotlib.pyplot as plt

level8 = '____G_G_MMM___L__L_G_____G___M_L__G__L_GM____L____'

evolutio1 = Evolution(200, level8, 100, 0.1, recombination_point=1, winner_point=True, parrent_choice="best")
evolutio2 = Evolution(500, level8, 200, 0.5, recombination_point=2, winner_point=False, parrent_choice="weigthed")

epoch = 30
best_competency1, worst_competency1, average_competency1, solvable1 = evolutio1.Run(epoch)
best_competency2, worst_competency2, average_competency2, solvable2 = evolutio2.Run(epoch)

print(solvable1)
print(solvable2)

x = np.arange(1,epoch+1)

fig, axis = plt.subplots(1, 2)
axis[0].plot(x, best_competency1)
axis[0].set_title("Best competency1")
axis[1].plot(x, best_competency2)
axis[1].set_title("Best competency2")
plt.savefig('Best competency.png')

fig, axis = plt.subplots(1, 2)
axis[0].plot(x, worst_competency1)
axis[0].set_title("Worst competency1")
axis[1].plot(x, worst_competency2)
axis[1].set_title("Worst competency2")
plt.savefig('Worst competency.png')

fig, axis = plt.subplots(1, 2)
axis[0].plot(x, average_competency1)
axis[0].set_title("Average competency1")
axis[1].plot(x, average_competency2)
axis[1].set_title("Average competency2")
plt.savefig('Average competency.png')