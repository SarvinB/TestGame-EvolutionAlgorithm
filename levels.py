from evolution_algorithm import Evolution
import numpy as np
import matplotlib.pyplot as plt

levels = ['__M_____', '____G_____', '__G___L_', '__G__G_L___', '____G_ML__G_', '____G_MLGL_G_', '_M_M_GM___LL__G__L__G_M__', '____G_G_MMM___L__L_G_____G___M_L__G__L_GM____L____', '___M____MGM________M_M______M____L___G____M____L__G__GM__L____ML__G___G___L___G__G___M__L___G____M__', '_G___M_____LL_____G__G______L_____G____MM___G_G____LML____G___L____LMG___G___GML______G____L___MG___']
epoch = 40

i = 1
# for level in levels[:8]:
#     evolution = Evolution(300, level, 150, 0.1, recombination_point=1, winner_point=True, parrent_choice="best")
#     best_competency, worst_competency, average_competency, solvable = evolution.Run(epoch)
#     s = "level " + str(i) + " :"
#     print(s)
#     print("Solvable: ", solvable)
#     print("Best competency: ", best_competency[epoch-1][0])
#     print("Worst competency", worst_competency[epoch-1])
#     print("Average competency", average_competency[epoch-1])
#     print(best_competency[epoch-1][1])
#     print()
#     i += 1
    

# epoch = 100
# for level in levels[8:]:
#     evolution = Evolution(1500, level, 750, 0.5, recombination_point=10, winner_point=True, parrent_choice="weigthed")
#     best_competency, worst_competency, average_competency, solvable = evolution.Run(epoch)
#     s = "level " + str(i) + " :"
#     print(s)
#     print("Solvable: ", solvable)
#     print("Best competency: ", best_competency[epoch-1][0])
#     print("Worst competency", worst_competency[epoch-1])
#     print("Average competency", average_competency[epoch-1])
#     print(best_competency[epoch-1][1])
#     print()
#     i += 1
    
for level in levels[:8]:
    evolution = Evolution(300, level, 150, 0.1, recombination_point=1, winner_point=True, parrent_choice="best")
    best_competency, worst_competency, average_competency, solvable = evolution.Run(epoch)
    s = "level " + str(i) + " :"
    print(s)
    print(best_competency[epoch-1][1])
    i += 1
    

epoch = 100
for level in levels[8:]:
    evolution = Evolution(1500, level, 750, 0.5, recombination_point=10, winner_point=True, parrent_choice="weigthed")
    best_competency, worst_competency, average_competency, solvable = evolution.Run(epoch)
    s = "level " + str(i) + " :"
    print(s)
    print(best_competency[epoch-1][1])
    i += 1