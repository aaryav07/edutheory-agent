import json
import os

def load_subject_data(subject):
    """Loads the JSON file for the selected subject."""
    file_path = f"data/{subject.lower()}.json"

    if not os.path.exists(file_path):
        return {"error": "Subject not found."}

    with open(file_path, "r") as f:
        return json.load(f)


def get_chapter_theory(subject, chapter_number):
    """Returns the theory for the selected subject & chapter."""
    data = load_subject_data(subject)

    if "error" in data:
        return data["error"]

    chapters = data.get("chapters", {})

    if str(chapter_number) not in chapters:
        return "Chapter not found."

    chapter = chapters[str(chapter_number)]
    
    return f"📘 {chapter['title']}\n\n{chapter['theory']}"


# Example usage (for future testing)
if __name__ == "__main__":
    print(get_chapter_theory("physics", 1))
