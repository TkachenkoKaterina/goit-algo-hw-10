from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

limonad = LpVariable(name="limonad", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += limonad + fruit_juice, "Total products"

model += (2 * limonad + 1 * fruit_juice <= 100), "Water constraint"
model += (1 * limonad <= 50), "Sugar constraint"
model += (1 * limonad <= 30), "Lemon juice constraint"
model += (2 * fruit_juice <= 40), "Fruit puree constraint"

status = model.solve()

print(f"Статус вирішення: {status}")
print(f"Максимальна кількість Лимонаду: {value(limonad)}")
print(f"Максимальна кількість Фруктового соку: {value(fruit_juice)}")
print(f"Загальна кількість продуктів: {value(limonad + fruit_juice)}")
