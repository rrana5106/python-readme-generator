questions = [
    {"type": "input",
     "message": "Enter the project title:",
    "name": "title"},
    {"type": "input",
     "message": "Enter a short project description:",
    "name": "description"},
    {"type": "input",
     "message": "Enter the installation instructions:",
    "name": "installation"},
    {"type": "input",
     "message": "Enter usage information:",
    "name": "usage"},
    {
    "type": "list",
    "message": "Select a license:",
    "choices": ["MIT", "Apache 2.0", "BSD", "GPL", "AGPL"],
    "name":"license"
    },
    {"type": "input",
     "message": "Enter the author's name: ",
     "name": "author"},
    {
    "type": "list",
    "message": "Choose the contact type:",
    "choices": ["email","phone"],
    "name": "contact_type"
    },
    {
    "type": "input",
    "message": "Enter your contact information:",
    "name": "contact_info"
    },
    # {"type": "confirm",
    #   "message": "Confirm?"},
]