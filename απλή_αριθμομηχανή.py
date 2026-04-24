# απλή_αριθμομηχανή.py

print("Απλή Αριθμομηχανή")
print("Επιλογές: +, -, *, /")

# 1. Παίρνουμε είσοδο από τον χρήστη
num1 = float(input("Δώσε τον πρώτο αριθμό: "))
op = input("Δώσε πράξη (+, -, *, /, %): ")
num2 = float(input("Δώσε τον δεύτερο αριθμό: "))

# 2. Υπολογισμός ανάλογα με την πράξη
if op not in ["+", "-", "*", "/", "%"]:
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Σφάλμα: δεν γίνεται διαίρεση με το 0.")
        continue
    result = num1 / num2
else:  # %
    if num2 == 0:
        print("Σφάλμα: δεν γίνεται modulo με το 0.")
        continue
    result = num1 % num2