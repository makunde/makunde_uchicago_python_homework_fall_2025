"""
We could not finish off our last assignment with
revisiting temperature conversion. It is back!

Write a statement using map that takes a list of
temperatures in Celsius and converts then to Fahrenheit.

map(something, something)
Write another statement using list comprehension to
make the same conversion.

converted_temps = [something something in something]
Use the following list of temperature on each of your approaches:

temperatures = [-32.0, 0.0, 1.0, 10.0, 32.0, 50.3, 88.8, 101.0]
What is the time complexity of each approach? Devise and conduct
a benchmarking experiment to determine if one is faster than the
other in practice.
"""

import time

temperatures = [-32.0, 0.0, 1.0, 10.0, 32.0, 50.3, 88.8, 101.0]


# Conversion formula: C to F is (temp * 9/5) + 32
# Reference: https://www.calculatorsoup.com/calculators/conversions/celsius-to-fahrenheit.php
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)


converted_temps_map = list(map(celsius_to_fahrenheit, temperatures))
print("Approach 1 - Using map:")
print(converted_temps_map)

converted_temps_list_comp = [celsius_to_fahrenheit(temp) for temp in temperatures]
print("\nApproach 2 - Using list comprehension:")
print(converted_temps_list_comp)

time_complexity_analysis = """
+++ TIME COMPLEXITY ANALYSIS +++
Map approach: O(n)
  - Must iterate through all n elements once
  - Each conversion is a constant-time operation

List comprehension approach: O(n)
  - Must iterate through all n elements once
  - Each conversion is a constant-time operation

Conclusion: Both approaches have identical time complexity O(n)
"""
print(time_complexity_analysis)

# Benchmarking experiment
print("\n+++ BENCHMARKING EXPERIMENT +++")

large_temps = temperatures * 1000


start = time.time()
for _ in range(100):
    list(map(celsius_to_fahrenheit, large_temps))
map_time = time.time() - start


start = time.time()
for _ in range(100):
    [celsius_to_fahrenheit(temp) for temp in large_temps]
list_comp_time = time.time() - start

print(f"Map approach: {map_time:.6f} seconds (100 runs on {len(large_temps)} elements)")
print(
    f"List comprehension approach: {list_comp_time:.6f} seconds (100 runs on {len(large_temps)} elements)"
)
print(f"Difference: {abs(map_time - list_comp_time):.6f} seconds")

if map_time < list_comp_time:
    ratio = list_comp_time / map_time
    print(f"\nMap is {ratio:.2f}x faster")
elif list_comp_time < map_time:
    ratio = map_time / list_comp_time
    print(f"\nList comprehension is {ratio:.2f}x faster")
else:
    print("\nPerformance is essentially equivalent")

conclusion = """
+++ CONCLUSION +++
While both approaches are O(n) theoretically, in practice,
list comprehension is typically faster due to Python optimizations.
List comprehension creates the list more efficiently than map + list().
"""
print(conclusion)
