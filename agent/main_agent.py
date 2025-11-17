import json
import os

DATA_FOLDER = "data"

def load_subjects():
    subjects = {}
    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".json"):
            with open(os.path.join(DATA_FOLDER, file), "r") as f:
                data = json.load(f)
                subjects[data["class"]] = data["topics"]
    return subjects


def run_agent():
    print("📚 Welcome to the 12th Standard Study Helper AI!")
    print("-----------------------------------------------")

    subjects = load_subjects()
    print("\nAvailable Subjects:")
    for idx, subj in enumerate(subjects.keys(), start=1):
        print(f"{idx}. {subj}")

    choice = int(input("\nEnter subject number: "))
    selected_subject = list(subjects.keys())[choice - 1]

    print(f"\n📘 Topics in {selected_subject}:")
    for topic in subjects[selected_subject]:
        print(f"- {topic}")

    print("\n✨ Thanks for using the Study Helper!")


if __name__ == "__main__":
    run_agent()
