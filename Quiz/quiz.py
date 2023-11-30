import json


with open("Questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for questions in data:
    print(questions["Question"])
    for index, choices in enumerate(questions["Choices"]):
        print(index+1, "-", choices)
    user_choice = int(input("Enter your choices: "))
    questions["user_choice"] = user_choice

score = 0
for index, questions in enumerate(data):
    if questions["user_choice"] == questions["Answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} - Your answer: {questions['user_choice']}, " \
              f"Correct answer: {questions['Answer']}"
    print(message)


print(score, "/", len(data))

