class Alternative:
    def __init__(self, name, cost, performance, battery, quality):
        self.name = name
        self.cost = cost
        self.performance = performance
        self.battery = battery
        self.quality = quality

    def calculate_score(self, weights):
        score = (
            (100 - self.cost) * weights["cost"] +
            self.performance * weights["performance"] +
            self.battery * weights["battery"] +
            self.quality * weights["quality"]
        )
        return score


class MCDSS:
    def __init__(self):
        self.alternatives = []

    def add_alternative(self, alt):
        self.alternatives.append(alt)

    def recommend(self, weights, max_budget):
        valid_options = []

        for alt in self.alternatives:

            # Constraint Checking (CSP)
            if alt.cost <= max_budget:

                score = alt.calculate_score(weights)

                valid_options.append((alt.name, score))

        if not valid_options:
            return None

        # Greedy Search
        valid_options.sort(key=lambda x: x[1], reverse=True)

        return valid_options


def main():

    print("========== MCDSS ==========")
    print("Laptop Recommendation System")
    print()

    system = MCDSS()

    system.add_alternative(
        Alternative("Laptop A", 50, 90, 80, 85)
    )

    system.add_alternative(
        Alternative("Laptop B", 40, 85, 75, 80)
    )

    system.add_alternative(
        Alternative("Laptop C", 70, 95, 90, 92)
    )

    print("Enter Importance Weights (0-1)")

    cost_weight = float(input("Cost Weight: "))
    performance_weight = float(input("Performance Weight: "))
    battery_weight = float(input("Battery Weight: "))
    quality_weight = float(input("Quality Weight: "))

    max_budget = int(input("Maximum Budget Score (0-100): "))

    weights = {
        "cost": cost_weight,
        "performance": performance_weight,
        "battery": battery_weight,
        "quality": quality_weight
    }

    results = system.recommend(weights, max_budget)

    if results:

        print("\nRecommended Options:")

        for i, (name, score) in enumerate(results, start=1):
            print(f"{i}. {name} --> Score = {score:.2f}")

        print("\nBest Choice:", results[0][0])

    else:
        print("No alternatives satisfy constraints.")


if __name__ == "__main__":
    main()