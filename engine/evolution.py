import random
from typing import List

from strategies.generator import generate_random_strategy
from .evaluation import evaluate_strategy


def crossover(parent1: dict, parent2: dict) -> dict:
    """Create a child strategy from two parents."""
    return {
        "short_window": random.choice(
            [parent1["short_window"], parent2["short_window"]]
        ),
        "long_window": random.choice(
            [parent1["long_window"], parent2["long_window"]]
        ),
    }


def evolve_strategies(strategies: List[dict], fitness_scores: List[float]) -> List[dict]:
    """Evolve a population of strategies based on fitness scores."""
    paired = list(zip(strategies, fitness_scores))
    paired.sort(key=lambda x: x[1], reverse=True)

    retain_length = max(1, len(strategies) // 2)
    survivors = [p[0] for p in paired[:retain_length]]

    # mutate survivors
    for i, strat in enumerate(survivors):
        if random.random() < 0.2:
            survivors[i] = generate_random_strategy()

    # produce children
    while len(survivors) < len(strategies):
        parents = random.sample(survivors, 2)
        child = crossover(parents[0], parents[1])
        survivors.append(child)

    return survivors


def main():
    import numpy as np
    import pandas as pd

    population_size = 6
    generations = 3

    price_series = pd.Series(
        np.cumprod(1 + np.random.normal(0, 0.01, 300)), name="price"
    )

    strategies = [generate_random_strategy() for _ in range(population_size)]

    for gen in range(generations):
        fitness = [evaluate_strategy(s, price_series) for s in strategies]
        print(f"Generation {gen} fitness: {fitness}")
        strategies = evolve_strategies(strategies, fitness)

    print("Final strategies:")
    for strat in strategies:
        print(strat)


if __name__ == "__main__":
    main()
