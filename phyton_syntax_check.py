x = 1
y = 1

while True:
    print("x:", x, "y:", y)
    if x == y:
        print("x and y are equal")
    else:
        print("x and y are not equal")
        if x < y:
            pass
        break
    y += x
    x += 1

for i in range(0, y, 1):
    for j in range(0, x, 1):
        print(str(i) + " " + str(j) + "   ", end="")
    print()

try:
    result = x / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("An unexpected error occurred:", str(e))
else:
    print("No error")
finally:
    print("Execution completed.")
