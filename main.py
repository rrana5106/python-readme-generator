from InquirerPy import prompt
from questions import questions
from projects import ReadmeProject
# from readmeGenerator import readmeGenerator


result = prompt(questions)

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

print(project.title)