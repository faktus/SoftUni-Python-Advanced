def battle(*args):
    
    negatives = [int(el) for el in args if int(el) < 0]
    positives = [int(el) for el in args if int(el) > 0]

    return negatives, positives

numbers = input().split()
matrix = battle(*numbers)

print(sum(matrix[0]))
print(sum(matrix[1]))

if abs(sum(matrix[0])) > sum(matrix[1]):
    print("The negatives are stronger than the positives") 
else:
    print("The positives are stronger than the negatives")