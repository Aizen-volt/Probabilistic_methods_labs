import math

from Permutations import Permutations
from Combinations import Combinations


def get_data(file_name: str) -> list:
    cities = []
    with open(file_name, "r") as file:
        next(file)
        for line in file:
            if line.strip():
                city_data = line.strip().split()
                city_id = int(city_data[0])
                city_name = city_data[1]
                population = int(city_data[2])
                latitude = float(city_data[3])
                longitude = float(city_data[4])
                cities.append((city_id, city_name, population, latitude, longitude))
    return cities


def calculate_distance(city1: list, city2: list) -> float:
    lat1, lon1 = city1[3], city1[4]
    lat2, lon2 = city2[3], city2[4]
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5


def main():
    cities = get_data("miasta.in")

    # zadanie 1
    min_distance = float('inf')
    best_order = None

    N = int(input("Enter N: "))
    cities = sorted(cities, key=lambda x: x[2], reverse=True)
    cities = cities[:N]

    for order in Permutations.generate(cities):
        distance = sum(calculate_distance(order[i], order[i + 1]) for i in range(len(order) - 1))
        if distance < min_distance:
            min_distance = distance
            best_order = order
    print("Najkrótsza trasa:", [city[1] for city in best_order], "Długość:", min_distance)

    # zadanie 2
    K = N // 2
    target_population = sum(city[2] for city in cities) / 2
    closest_subset = None
    min_population_difference = math.inf

    for comb in Combinations.generate(cities, K):
        subset_population = sum(city[2] for city in comb)
        population_difference = abs(subset_population - target_population)
        if population_difference < min_population_difference:
            min_population_difference = population_difference
            closest_subset = comb

    print("Podzbiór K=N/2 najbliższy 50% populacji:")
    for city in closest_subset:
        print(city[1], "-", city[2], "mieszkańców")


if __name__ == '__main__':
    main()
