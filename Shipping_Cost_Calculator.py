# Shipping Cost Calculator
## Input package weight and shipping rate
weight = float(input("Please, enter package weight in kilograms"))
rate = float(input("Please, enter a shipping rate per kilogram: "))
# Shipping cost
shipping_cost = weight * rate
## Display the result
print(f"Shipping cost:{shipping_cost} USD")
