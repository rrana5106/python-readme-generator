# This class writes the README to a file
class FileWriter:
    
    # Store the filename
    def __init__(self,filename):
        self.filename = filename
    
    # Write the content into the file
    def write(self,content):
        with open(self.filename, "w") as file:
            file.write(content)
        