# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final score when quiz is completed
name = input("Enter your name:")
print("welcome to quiz game", name, '!')
quiz = {
    "Question 1": {
        "Question": "What is the capital of France?",
        "ans": "paris"
    },
    "Question 2": {
        "Question": "What is the capital of Germany?",
        "ans": "Berlin"
    },
    "Question 3": {
        "Question": "What is the capital of Italy?",
        "ans": "Rome"
    },
    "Question 4": {
        "Question": "What is the capital of Spain?",
        "ans": "Madrid"
    },
    "Question 5": {
        "Question": "What is the capital of Portugal?",
        "ans": "Lisbon"
    },
    "Question 6": {
        "Question": "What is the capital of Switzerland?",
        "ans": "Bern"
    },
    "Question 7": {
        "Question": "What is the capital of Austria?",
        "ans": "Vienna"
    },
    "Question 8": {
        "Question": "What is the capital of India?",
        "ans": "Delhi"
    },

}

score = 0

for key, value in quiz.items():
    print(value["Question"])
    ans = input("Answer?")

    if ans.lower() == value["ans"].lower():
        print("Correct")
        score += 1
        print("your score is :", str(score))

    else:
        print("Wrong")
        print("The answer is:", value["ans"])
