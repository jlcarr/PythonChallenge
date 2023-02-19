# PythonChallenge
Solutions to Python Challenge problems in Python3.

## Results
### Level 0
- **Title**: warming up
- **Url**: http://www.pythonchallenge.com/pc/def/0.html
- **Solution**: Simply evaluate the expression in the picture (`2**38` which is `274877906944`) and go the html page of the same name.
- **Answer**: http://www.pythonchallenge.com/pc/def/274877906944.html

### Level 1
- **Title**: What about making trans?
- **Url**: http://www.pythonchallenge.com/pc/def/map.html
- **Solution**: The image shows a mapping of a few letters in a rot2 ciper, and the text hint says "think twice". Applying a rot2 to the cipher text we get clear text saying "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url." Applying rot2 to `"map"` gives `"ocr"` again we go to that html page.
- **Answer**: http://www.pythonchallenge.com/pc/def/ocr.html

### Level 2
- **Title**: ocr
- **Url**: http://www.pythonchallenge.com/pc/def/ocr.html
- **Solution**: Like the hint says, look at the page source, and inside we see comments with ciphertext and another hint suggesting to look for rare characters. Using Python's `collections.Counter` class we can filer out characters at least as common as the newlines, to get the final result of `"equality"`.
- **Answer**: http://www.pythonchallenge.com/pc/def/equality.html

### Level 3
- **Title**: re
- **Url**: http://www.pythonchallenge.com/pc/def/equality.html
- **Solution**: As the hint says, we're looking for examples of lowercase letters surrounded by exactly 3 upper-case letters in the ciphertext in the comments. As the title hints at, we can use Python's `re` library to do this. A working regex is `r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'`. Watch out for the cases of more than 3 upper-case letters present. 
- **Answer**: http://www.pythonchallenge.com/pc/def/linkedlist.html

