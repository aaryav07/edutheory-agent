📘 HSC Theory Assistant – AI Retrieval Agent

This project is an AI-powered theory assistant designed for 12th Standard (HSC) students.
It helps students get clear and accurate theory for any subject and chapter using a simple retrieval system.

🚀 Project Goal

To create an easy, fast, and helpful tool for HSC students where they can pick a subject → pick a chapter → and instantly get the full theory.

📂 Project Structure
your-repo/
 ├── data/
 │    ├── physics.json
 │    ├── chemistry.json
 │    ├── maths.json
 │    └── biology.json
 ├── agent/
 │    └── main_agent.py
 ├── requirements.txt
 └── README.md

 📚 How It Works
1. Data Folder

The data folder contains JSON files for each subject.
Each file includes:

chapter number

chapter name

chapter theory

Example inside a JSON file:

{
  "subject": "Physics",
  "chapters": {
    "1": {
      "title": "Rotational Motion",
      "theory": "Rotational motion is the motion of a body around a fixed axis."
    }
  }
}

2. Agent Folder

The agent folder contains main_agent.py, which:

Loads the correct JSON file

Finds the chapter

Returns the theory

Displays it in a clean format

Example function:

get_chapter_theory("physics", 1)

🧠 Example Usage
from agent.main_agent import get_chapter_theory
print(get_chapter_theory("physics", 1))


Output:

📘 Rotational Motion

Rotational motion is the motion of a body around a fixed axis...

🔥 Future Enhancements

Add full HSC syllabus theory

Add a simple website UI

Add MCQ generator

Add answer writing helper

Add concept explainers

Add video links

✨ Created as a Capstone Project for AI Agent Intensive 2025

By: Aarya Vhatkar 🤍
