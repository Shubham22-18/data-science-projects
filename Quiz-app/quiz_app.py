def run_quiz():
    questions = [
        {
            "question": "Which language is primarily used for Data Science?",
            "options": ["A. Java", "B. Python", "C. C++", "D. PHP"],
            "answer": "B"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Processing Unit",
                "C. Central Program Unit",
                "D. Computer Program Unit"
            ],
            "answer": "A"
        },
        {
            "question": "Which company created GitHub?",
            "options": ["A. Google", "B. Microsoft", "C. Meta", "D. Amazon"],
            "answer": "B"
        }
    ]

    score = 0

    print("\n===== Quiz App =====")

    for q in questions:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n===== Quiz Completed =====")
    print(f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
