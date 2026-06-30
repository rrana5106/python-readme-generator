# List of questions that will be shown to the user
questions = [

    # Ask for the project title
    {
        "type": "input",
        "message": "Enter the project title:",
        "name": "title"
    },

    # Ask for a short description
    {
        "type": "input",
        "message": "Enter a short project description:",
        "name": "description"
    },

    # Ask how to install the project
    {
        "type": "input",
        "message": "Enter the installation instructions:",
        "name": "installation"
    },

    # Ask how to use the project
    {
        "type": "input",
        "message": "Enter usage information:",
        "name": "usage"
    },

    # Let the user choose a license
    {
        "type": "list",
        "message": "Select a license:",
        "choices": ["MIT", "Apache 2.0", "BSD", "GPL", "AGPL"],
        "name": "license"
    },

    # Ask for the author's name
    {
        "type": "input",
        "message": "Enter the author's name:",
        "name": "author"
    },

    # Choose how the user wants to be contacted
    {
        "type": "list",
        "message": "Choose the contact type:",
        "choices": ["email", "phone"],
        "name": "contact_type"
    },

    # Ask for the contact details
    {
        "type": "input",
        "message": "Enter your contact information:",
        "name": "contact_info"
    },
]