#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 29/12/2022
The aim of this program is to give a solvable problem of the 38 magique
"""

import sys
sys.path.append("../")
from GeneticAlgorithm import *
from numpy import prod, random
import pandas as pd



### Recovering Useful Data

stats = ["HP", "ATK", "DEF", "SP.ATK", "SP.DEF", "SPEED"]

df = pd.read_csv("pokedex.csv")
pokedex_df = df.loc[:, ["NAME", "FORM", "TYPE 1", "TYPE 2", *stats]]
pokedex_df

# All possible types a pokemon can have, duets or not
duets = []
for d in pokedex_df.loc[:, ["TYPE 1", "TYPE 2"]].values:
    ld = list(d)
    ld.sort()
    if "-----" in ld:
        ld = ld[1:]
    if ld not in duets:
        duets.append(ld)
duets.sort()
duets

types_table = pd.read_csv("types_table.csv")
types_table

# Exemple of Venusaur
pokemon = pokedex_df.loc[10]
pokemon
pokemon["NAME"], pokemon["TYPE 1"], pokemon["TYPE 2"]





### Declaring Specific Agent


class Team(Agent):
    """
    Team of 6 Pokemons, each of 1 or two different types
    """
    def __init__(self, genes=6*[0]):
        # the numbers of the pokemons [0, 0, 0, 0, 0, 0]
        self.genes = genes  

    def get_score(self):
        s = 0
        s += self.type_coverage()
        s += self.statistic_balance()
        return s

    def statistic_balance(self):
        """
        Return the sum of the max stats in the team for each stat
        """
        s = 0
        for stat in stats:
            m = 0
            for p in self.genes:
                m = max(m, pokedex_df.loc[p][stat])
            s += m
        return s

    def type_coverage(self):
        # for each possible duet type, return the best sum of coefficients
        # in attack and defense of one of the pokemons in the team
        teams_types = self.get_types()
        s1 = evaluate_offensive_team(teams_types, duets)
        s2 = evaluate_offensive_team(duets, teams_types)
        return s1-s2

    def get_types(self):
        types = []
        for p in self.genes:
            types.append(get_pokemon_types(p))
        return(types)

    def get_offspring(self):
        l = len(self.genes)
        offsprings_genes = [p for p in self.genes]
        new_pokemon_num = random.randint(len(pokedex_df))
        offsprings_genes[random.randint(l)] = new_pokemon_num
        offspring = Team(offsprings_genes)
        return offspring

    def get_df(self):
        return pokedex_df.loc[self.genes]

    def save(self, file):
        self.get_df().to_csv(file)

    def __repr__(self):
        s = str(pokedex_df.loc[self.genes])
        return s


def get_pokemon_types(pokemon_number):
    pokemon = pokedex_df.loc[pokemon_number]
    pokemon_types = [pokemon["TYPE 1"]]
    if pokemon["TYPE 2"] != "-----":
        pokemon_types.append(pokemon["TYPE 2"])
    return pokemon_types

get_pokemon_types(2)


def get_pokemon_stats(pokemon_number):
    pokemon = pokedex_df.loc[pokemon_number]
    pokemon_stats = pokedex_df.loc[pokemon_number][stats].to_dict()
    return pokemon_stats

get_pokemon_stats(0)


def get_pokemon_name(pokemon_number):
    pokemon = pokedex_df.loc[pokemon_number]
    pokemon_name = pokedex_df.loc[pokemon_number]["NAME"]
    return pokemon_name

get_pokemon_name(0)


def evaluate_offense_duet_on_duet(d1, d2):
    # d1 attacks d2
    max_offense = 0
    for type1 in d1:
        offense = prod([types_table[type1][type2] for type2 in d2])
        if offense > max_offense:
            max_offense = offense
    return max_offense

def find_best_offense(team, duet):
    # Find the best pokemon on the team against one pokemon duet
    offense_values = [evaluate_offense_duet_on_duet(p, duet) for p in team]
    max_offensive = max(offense_values)
    return max_offensive

def evaluate_offensive_team(team1, team2):
    # find the best pokemon in team 1 to strike each pokemon in team 2
    # then adds the summed coeeficient to the final result
    l = len(team2)
    total = 0
    for d in team2:
        total += find_best_offense(team1, d)
    return total/l


def main(parameters):
    return(0)


if __name__ == "__main__":
    main(sys.argv)
