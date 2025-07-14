import json

def load_database(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def find_answer(database, user_question):
    # Normalize the question text for better matching
    user_question = user_question.lower().strip().replace('"', '').replace("'", "")
    for qa in database:
        question = qa['question'].lower().strip().replace('"', '').replace("'", "")
        # Check if exact match or if one string contains the other (to cover variations)
        if question == user_question or user_question in question or question in user_question:
            return qa['answer']
    return "Sorry, I don't have the answer to that question."

def main():
    database = load_database("physics.json")
    print("Physics AI Tutor (type 'exit' to quit)\n")
    while True:
        user_question = input("Ask a question: ").strip()
        if user_question.lower() == "exit":
            print("Goodbye!")
            break
        answer = find_answer(database, user_question)
        print("Answer:", answer, "\n")

if __name__ == "__main__":
    main()
