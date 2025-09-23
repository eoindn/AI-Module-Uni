class TaxRuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, income, result):
        self.rules.append((income,result))

    def apply_bracket(self,income_input):
        for income, result in self.rules:
            if income(income_input):
                return result
        return "must be a tax evader"
    

engine = TaxRuleEngine()
engine.add_rule(lambda x: x <= 12570, "0 tax broke boi" )
engine.add_rule(lambda x: x > 12571 and x < 50271, "20% tax" )
engine.add_rule(lambda x: x > 50270 and x < 124141 ,"40% tax" )
engine.add_rule(lambda x: x >= 125140, "45 tax")

print(engine.apply_bracket(1000000))