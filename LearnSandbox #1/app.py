inputs = []

while True:
        user_input = input("Enter something: ")
        if user_input.lower() == "exit":
                break
        inputs.append(user_input)

print("Entered values:")
for index, value in enumerate(inputs, start=1):
        print(f"{index}. {value}")


