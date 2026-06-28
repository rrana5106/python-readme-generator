from InquirerPy import prompt
from questions import questions

result = prompt(questions)
title_name = result["name"]
description = result["description"]
print(result)
# fav_lang = result[1]
# confirm = result[2]

