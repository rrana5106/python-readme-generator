# Used to ask the user questions in the terminal
from InquirerPy import prompt

# Import the questions for the user
from questions import questions

# Import the class that stores the project information
from projects import ReadmeProject

# Import the class that generates the README content
from readmeGenerator import ReadmeGenerator

# Import the class that writes the README to a file
from fileWriter import FileWriter

# Ask the user the questions and store the answers in a dictionary
result = prompt(questions)

# Store the user's answers in a project object
project = ReadmeProject(
    result["title"],
    result["description"],
    result["installation"],
    result["usage"],
    result["license"],
    result["author"],
    result["contact_type"],
    result["contact_info"]
)

# Generate the README content
generator = ReadmeGenerator(project)
markdown = generator.generate()

# Save the README to a file
writer = FileWriter("README.md")
writer.write(markdown)

print("README.md created successfully")