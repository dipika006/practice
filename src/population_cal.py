n = 10000
for i in range(10, 1, -1):
    population = round(n - (0.1 * n))
    print(f"population in year#{i}", population)
    n = population
