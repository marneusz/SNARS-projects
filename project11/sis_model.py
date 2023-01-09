import networkx as nx
import numpy as np
import random


class SISModel:
    def __init__(self, G: nx.Graph, beta: float = 0.1, gamma: float = 0.1) -> None:
        """_summary_

        Args:
            G (nx.Graph): NetworkX Graph
            beta (float, optional): The probability of being infected. Defaults to 0.1.
            gamma (float, optional): The probability of being recovered. Defaults to 0.1.
        """

        self.beta = beta
        self.gamma = gamma
        self.G = G

        self.reset()

    def reset(self):
        self.is_infected = {k: False for k in self.G.nodes}
        unlucky_person = random.choice(list(self.is_infected.keys()))
        self.is_infected[unlucky_person] = True
        self.timestep = 0
        self.num_of_infected = 1
        return unlucky_person

    def next_step(self):
        if all(self.is_infected.values()) or not any(self.is_infected.values()):
            self.reset()
            return

        to_be_infected = {}
        for person in self.G.nodes:
            if not self.is_infected[person]:
                infected_neighbors = [
                    neighbor
                    for neighbor in self.G.neighbors(person)
                    if self.is_infected[neighbor]
                ]
                to_be_infected[person] = (
                    np.random.binomial(n=len(infected_neighbors), p=self.beta) > 0
                )
                self.num_of_infected += to_be_infected[person]

            else:
                to_be_infected[person] = np.random.binomial(n=1, p=(1 - self.gamma))
                self.num_of_infected -= 1 - to_be_infected[person]

        self.is_infected = to_be_infected
        self.timestep += 1

        return self.timestep
