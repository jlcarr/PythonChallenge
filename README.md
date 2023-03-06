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

### Level 4
- **Title**: follow the chain
- **Url**: http://www.pythonchallenge.com/pc/def/linkedlist.html
- **Solution**: The html page directs to a php page, where we have an image which links to the same page with a url query parameter, `nothing=12345` and there's a comment which alludes to following the "nothings" at most 400 times. Following the link with the query parameter we are are told what the "next nothing is", which we can use to update the query parameter. Repeating this in an automated loop until we finall reach a page saying `peak.html` which is our answer.
- **Answer**: http://www.pythonchallenge.com/pc/def/peak.html

### Level 5
- **Title**: peak hell
- **Url**: http://www.pythonchallenge.com/pc/def/peak.html
- **Solution**: In the html there is a tag called "peakhell" with a `src` attributes pointing to banner.p which is a file we can download. The hint text says "pronounce it" and "peakhell" sounds like "pickle" a popular python serialization library, whose output files usually use the .p exentsion. If we unpickle the file we get a list of lists and in each inner list we have tuples of characters and numbers. if we repeat each character the number of times and concatenate them all together we get an ascii art saying "channel" which is our answer.
- **Answer**: http://www.pythonchallenge.com/pc/def/channel.html

### Level 6
- **Title**: now there are pairs
- **Url**: http://www.pythonchallenge.com/pc/def/channel.html
- **Solution**: The image is of a zipper, so try changing the url to end in .zip instead of .html. Download this .zip, then extract the contents, which is a folder with a lot of numbered .txt files and a readme.txt giving a starting "nothing" to follow. Follow the sequence of .txt files in the same "next nothing" style, until we get to a .txt saying "Collect the comments." so taking the zip format's comment for each internal file gives a sequence of bytes, which decoded to ascii makes a large ascii art saying "hockey" but using the letters "oxygen" which is our answer.
- **Answer**: http://www.pythonchallenge.com/pc/def/oxygen.html

### Level 7
- **Title**: smarty
- **Url**: http://www.pythonchallenge.com/pc/def/oxygen.html
- **Solution**: The image shown has a sequence of grey squares along the middle of various shades. Taking the byte values of the shades, and converting ascii we get a message "smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]". Converting the last array into ascii again gives the answer "integrity".
- **Answer**: http://www.pythonchallenge.com/pc/def/integrity.html

