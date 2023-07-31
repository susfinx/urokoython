names = ['Alice', 'Bob', 'Charlie']
rates = [100, 200, 300]
bonuses = ['10.25%', '5%', '15%']

result_dict = dict((name, rate * float(bonus.rstrip('%')) / 100) for name, rate, bonus in zip(names, rates, bonuses))
print(result_dict)
