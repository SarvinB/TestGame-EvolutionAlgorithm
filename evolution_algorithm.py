import numpy as np
import random

class Evolution:
    
    def __init__(self, chromosome_number, level, parrent_number, m, recombination_point=1, winner_point=True, parrent_choice="random"):
        
        self.chromosome_number = chromosome_number
        self.gen_number = len(level)
        self.level = level
        self.parrent_number = parrent_number
        self.m = m
        self.solvable = False
        self.winner_point = winner_point
        self.parrent_choice = parrent_choice
        self.recombination_point = recombination_point
        self.population = self.population_production()

    
    def population_production(self):
        
        population = np.random.randint(0,3, (self.chromosome_number, self.gen_number))
        return population
    
    def competency(self, chromosome):
        point = 0
        lenth = self.gen_number
        
        if chromosome[lenth-1] == 1:
            point += 1
            
            
        win = True
        step = 0
        loose_step = -1
        
        if self.level[0] == 'G' or self.level[0] == 'L':
            win = False
            loose_step = 0
        
        for i in range(lenth-1):
            
            if chromosome[step] == 0:
                if self.level[step+1] == 'G' or self.level[step+1] == 'L':
                    win = False   
                    if loose_step == -1:
                        loose_step = step
                elif self.level[step+1] == 'M':
                    point += 2
                    
            elif chromosome[step] == 1:
                if self.level[step+1] == 'L':
                    win = False
                    if loose_step == -1:
                        loose_step = step
                    
                if step <= lenth-3 and self.level[step+2] == 'M':
                    point += 2
                    
                if step <= lenth-3 and self.level[step+2] == 'L':
                    win = False
                    if loose_step == -1:
                        loose_step = step
                    
                if step <= lenth-3 and self.level[step+2] == 'G':
                    point += 2
                    
                elif self.level[step+1] == '_' or self.level[step+1] == 'M':
                    point -= 1
                    
                step += 1
            
            else:
                if self.level[step+1] == 'G':
                    win = False
                    if loose_step == -1:
                        loose_step = step
                    
                # if step <= lenth-3 and (self.level[step+2] == 'G' or self.level[step+2] == 'L'):
                #     win = False
                #     if loose_step == -1:
                #         loose_step = step
                    
                if self.level[step+1] == '_':
                    point -= 1
                    
                if step <= lenth-3 and self.level[step+2] == 'M':
                    point += 2   
                step += 1
            step += 1
            if step >= lenth-1:
                break
            
        point += loose_step
                    
        if win and self.winner_point:
            point += (self.gen_number-3)/2 + 1
            return True, point
            
        return False, point
    
    def competency_chromosomes (self, population):
        
        result = []
        
        i = 0
        for c in population:
            c_competency = self.competency(c)
            if c_competency[0]:
                self.solvable = True
            t = (c_competency[1], i)
            result.append(t)
            i += 1
        return sorted(result)


    def choose_parrent(self):
        competencies = self.competency_chromosomes(self.population)
        if (self.parrent_choice == "best"):
            return competencies[len(competencies) - self.parrent_number:]
            
        if (self.parrent_choice == "weigthed"):
            p = []
            sum = 0
            mini = competencies[0][0]
            for c in competencies:
                sum += c[0]
            sum += len(competencies)*(abs(mini)+1)
            for c in competencies:
                p.append((c[0]-mini+1)/sum)
            uniforms = np.random.uniform(0,1,self.parrent_number)
            parrent_choosen = []
            for u in uniforms:
                s = p[0]
                i = 0
                while s < u:
                    s += p[i]
                    i += 1
                    if i >= len(competencies):
                        break
                parrent_choosen.append(competencies[max(i-1, 0)])
            return parrent_choosen
                
            
    
    def recombination_and_mutation(self, p1, p2):
        cut = np.random.randint(low=0, high=self.gen_number, size=self.recombination_point)
        
        c1 = p1[:cut[0]]
        c2 = p2[:cut[0]]
        
        for i in range(1, self.recombination_point):
            if i%2 == 1:
                c1 = np.concatenate((c1, p2[cut[i-1]:cut[i]]))
                c2 = np.concatenate((c2, p1[cut[i-1]:cut[i]]))
            else:
                c1 = np.concatenate((c1, p1[cut[i-1]:cut[i]]))
                c2 = np.concatenate((c2, p2[cut[i-1]:cut[i]]))
        
        if self.recombination_point%2 == 1:
            c1 = np.concatenate((c1, p2[cut[self.recombination_point-1]:]))
            c2 = np.concatenate((c2, p1[cut[self.recombination_point-1]:]))
        else:
            c1 = np.concatenate((c1, p1[cut[self.recombination_point-1]:]))
            c2 = np.concatenate((c2, p2[cut[self.recombination_point-1]:]))
            
        u = np.random.uniform(0,1,2)
        if (u[0] <= self.m):
            gen_choosen = np.random.randint(low=0, high=self.gen_number, size=1)[0]
            if c1[gen_choosen] == 2:
                c1[gen_choosen] = 0
            else:
                c1[gen_choosen] += 1
        if (u[1] <= self.m):
            gen_choosen = np.random.randint(low=0, high=self.gen_number, size=1)[0]
            if c2[gen_choosen] == 2:
                c2[gen_choosen] = 0
            else:
                c2[gen_choosen] += 1
        
        return c1, c2
    
    def recombination_and_mutation_population(self):
        parrent_population = self.choose_parrent()
        childeren = []
        
        for i in range(0, self.parrent_number, 2):
            t1, t2 = random.choices(parrent_population, k=2)
            p1 = self.population[t1[1]]
            p2 = self.population[t2[1]]
            c1, c2 = self.recombination_and_mutation(p1, p2)
            childeren.append(c1)
            childeren.append(c2)
        
        return childeren
    
    def choose_population(self, main_population, childeren_population):
        childeren_competencies = self.competency_chromosomes(childeren_population)
        main_competencies = self.competency_chromosomes(main_population)
        population_competencies = []
        for c in childeren_competencies:
            population_competencies.append(c)
        for c in main_competencies:
            population_competencies.append(c)
        population_competencies = sorted(population_competencies)
        
        return population_competencies[len(population_competencies)-self.chromosome_number:]
        
            
    def make_population_table(self, population_tuple):
        p = []
        for t in population_tuple:
            p.append(self.population[t[1]])
        np.asarray(p)
        p1 = self.population
        self.population = p
        p2 = self.population
        x = 10
        
    def competency_population(self, population_competency, competency_type="best"):
        
        if competency_type == "best":
            return max(population_competency, key=lambda tup: tup[0])[0], self.population[max(population_competency, key=lambda tup: tup[0])[1]]
        if competency_type == "worst":
            return min(population_competency, key=lambda tup: tup[0])[0]
        if competency_type == "average":
            sum = 0
            for c in population_competency:
                sum += c[0]
            return (sum/len(population_competency))            
        
    
    def Run(self, k=10):
        
        best_competency = []
        worst_competency = []
        average_competency = []
        
        for i in range(k):
            parrent_population = self.choose_parrent()
            childeren_population = self.recombination_and_mutation_population()
            self.make_population_table(self.choose_population(self.population, childeren_population))
            competency_chromosomes = self.competency_chromosomes(self.population)
            best_competency.append(self.competency_population(competency_chromosomes, competency_type="best"))
            worst_competency.append(self.competency_population(competency_chromosomes, competency_type="worst"))
            average_competency.append(self.competency_population(competency_chromosomes, competency_type="average"))
        
        return best_competency, worst_competency, average_competency, self.solvable
            
    
    
        
        