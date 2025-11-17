import os
import json

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

def load_subjects():
    subjects = {}
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".json") and filename != "subjects.json":
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                subject_name = data.get("Subject", "Unknown")
                topics = data.get("topics", [])
                subjects[subject_name] = topics
    return subjects

def run_agent():
    print("📚 Welcome to the 12th Standard Study Helper AI!")
    print("-----------------------------------------------")
    
    subjects = load_subjects()
    if not subjects:
        print("No subjects found in the data folder!")
        return

    while True:
        print("\nAvailable subjects:")
        for sub in subjects:
            print(f" - {sub}")
        print("Type 'exit' to quit.")

        choice = input("\nEnter the subject you want to study: ").strip()
        if choice.lower() == "exit":
            print("Goodbye! Happy studying! 📖")
            break

        if choice not in subjects:
            print("Subject not found. Please type exactly as shown above.")
            continue

        print(f"\nTopics in {choice}:")
        for topic in subjects[choice]:
            title = topic.get("Title", "No Title")
            theory = topic.get("Theory", "No Theory")
            print(f" - {title}: {theory}")

if __name__ == "__main__":
    run_agent()
