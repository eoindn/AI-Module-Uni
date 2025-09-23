class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"

expert_system = WeatherExpertSystem()
expert_system.add_fact("high_temperature")  # Example: High temperature
expert_system.add_fact("low_humidity")  # Example: Low humidity
expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")

result = expert_system.infer()
print(result)  # Output: Comfortable