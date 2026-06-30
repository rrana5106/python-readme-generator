# This class creates the README content
class ReadmeGenerator:
    
    # Store the project object
    def __init__(self, project):
        self.project = project

    # Generate the README in Markdown format
    def generate(self):
        return f"""# {self.project.title}

## Description
{self.project.description}

## Installation
{self.project.installation}

## Usage
{self.project.usage}

## License
{self.project.license}

## Author
{self.project.author}

## Contact
{self.project.contact_type}: {self.project.contact_info}
"""