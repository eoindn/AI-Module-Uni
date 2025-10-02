

class FuzzySystem:
    def __init__(self):
        # Rules
        self.rules = {
            'heater_on': ['very_cold', 'cold'],
            'fan_on': ['hot', 'very_hot'],
            'off': ['warm']
        }

        # Membership functions
        self.memberships = {
            'very_cold': lambda x: self.triangle(x, -10, 0, 10),
            'cold':      lambda x: self.triangle(x, 0, 10, 20),
            'warm':      lambda x: self.triangle(x, 10, 20, 30),
            'hot':       lambda x: self.triangle(x, 20, 30, 40),
            'very_hot':  lambda x: self.triangle(x, 30, 40, 50)
        }

    def triangle(self, x, a, b, c):
        if x <= a or x >= c:
            return 0
        elif x == b:
            return 1
        elif a < x < b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)

    def __fuzzify(self, temp_value):
        return {term: func(temp_value) for term, func in self.memberships.items()}

    def __infer(self, memberships):
        results = {}
        for action, terms in self.rules.items():
            results[action] = max(memberships[term] for term in terms)
        return results

    def __defuzzify(self, inference_results):
        return max(inference_results, key=inference_results.get)

    def evaluate(self, temperature):
        memberships = self.__fuzzify(temperature)
        inference_results = self.__infer(memberships)
        decision = self.__defuzzify(inference_results)
        return decision


if __name__ == "__main__":
    system = FuzzySystem()
    for temp in [-5, 5, 15, 25, 35, 45,17]:
        decision = system.evaluate(temp)
        print(f"Temperature {temp}°C → Decision: {decision}")

