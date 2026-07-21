import random

def quiz():
    score = 0
    num_questions = 5  # number of questions in the quiz

    for i in range(num_questions):
        # Generate random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        # Randomly choose an operation
        operation = random.choice(["+", "-", "*"])

        # Form the question
        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        else:  # multiplication
            correct_answer = num1 * num2

        # Ask the user
        print(f"Q{i+1}: What is {num1} {operation} {num2}?")
        user_answer = int(input("Your answer: "))

        # Check answer
        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}.")

    # Final score
    print("\n--- Quiz Finished ---")
    print(f"Your final score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz()