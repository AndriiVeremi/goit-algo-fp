import random
import matplotlib.pyplot as plt

# Функція для симуляції кидання двох кубиків
def simulate_dice_rolls(num_simulations):
    # Створюємо словник для підрахунку кількості кожної суми
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll_sum = dice_1 + dice_2
        sum_counts[roll_sum] += 1
    
    # Обчислюємо ймовірність кожної суми
    probabilities = {key: value / num_simulations * 100 for key, value in sum_counts.items()}
    
    return sum_counts, probabilities

# Кількість симуляцій
num_simulations = 100000

# Запускаємо симуляцію
sum_counts, probabilities = simulate_dice_rolls(num_simulations)

# Аналітичні ймовірності
analytic_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Виводимо результати
print("Simulation Results (Monte Carlo):")
for roll_sum in range(2, 13):
    print(f"Sum {roll_sum}: {probabilities[roll_sum]:.2f}%")

print("\nAnalytical Results:")
for roll_sum in range(2, 13):
    print(f"Sum {roll_sum}: {analytic_probabilities[roll_sum]:.2f}%")

# Побудова графіка
sums = list(range(2, 13))
simulated_probabilities = [probabilities[roll_sum] for roll_sum in sums]
analytical_probabilities = [analytic_probabilities[roll_sum] for roll_sum in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, simulated_probabilities, alpha=0.6, label="Simulated (Monte Carlo)", color='blue')
plt.plot(sums, analytical_probabilities, 'r-', label="Analytical", marker='o')
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability (%)")
plt.title("Probability of Each Sum with Two Dice Rolls")
plt.legend()
plt.grid(True)
plt.show()
 