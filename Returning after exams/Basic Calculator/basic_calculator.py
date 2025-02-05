class Calculator:

    def add(self, i, j):
        return (i + j)

    def subtract(self, i, j):
        return (i - j)

    def multiply(self, i, j):
        return (i * j)

    def divide(self, i, j):
        if j == 0:
            return "Error: Division by zero is not allowed"
        return (i / j)

    def modulus(self, i, j):
        if j == 0:
            return "Error: Modulus by zero is not allowed"
        return (i % j)

def main():
    cal = Calculator()

    while True:
        try:
            choice = int(input("Enter the operation number: \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (/) \n 5. Modulus (%) \n 0. Exit \n"))
            if choice == 0:
                print("Exiting...Thank You!")
                break
            
            if not 1 <= choice <= 5:
                raise ValueError("Invalid choice, please enter a choice between 1 and 5!")
                
            a = float(input("Enter the first number \n"))
            b = float(input("Enter the second number \n"))

            if choice == 1:
                res = cal.add(a, b)
                

            elif choice == 2:
                res = cal.subtract(a, b)
                

            elif choice == 3:
                res = cal.multiply(a, b)
                

            elif choice == 4:
                res = cal.divide(a, b)
                

            elif choice == 5:
                res = cal.modulus(a, b)

            print(f"\n{'='*30}\nResult: {res}\n{'='*30}\n")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()