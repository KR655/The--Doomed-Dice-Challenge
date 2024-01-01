numbers = [1, 2, 3, 4, 5, 6]
total = len(numbers) ** 2
print("Total Combinations:", total)
combos = [(i, j) for i in numbers for j in numbers]
print("\nCombinations Distribution:")
for i in range(0, total, len(numbers)):
    print(combos[i:i + len(numbers)])

print("\nProbability for every Sum :")
for i in range(2, 13):
    count = sum(1 for j in combos if sum(j) == i)
    probability = count / total
    print(f"P(Sum = {i})  :   {count}/{total} = {probability:.2f}")



    
