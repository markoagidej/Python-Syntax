# Task 1: Validating Calculations

answer_normal = 1 + 2 * 3 ** 4 / 5
answer_parens = 1 + (2 * 3) ** (4 / 5)

print(answer_normal == answer_parens)
print("Normal = " + str(answer_normal))
print("Parens = " + str(answer_parens))

# Task 2: Mix and Match

result = 1 + 9 == 5 + 5 and 10 - 4 == 6
print("Result of 1 + 9 == 5 + 5 and 10 - 4 == 6 should be True")
print(result)