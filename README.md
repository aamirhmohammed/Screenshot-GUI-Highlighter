# CS_435_Programming_Assignment_1
 A small tool that highlights and annotates the leaf level GUI-components in an Android application screenshot
 
 To run this code, create a folder containing rect.py and any screenshots that need annotations. 
 Each screenshot requires a png and xml file, pairs that are corrupted or missing a file are skipped.
 Highlighted images are saved in the format 'annotated'<filename.png> in the same folder

This solution depends on the os library for directory handling, Pillow for image manipulation, and xml dom for parsing.
The program checks each file in it's folder to see if it's an XML.
It then checks for a corresponding png file in the folder.
After parsing the xml file for leaf nodes, it adds the dimensions of each GUI component into a 2D list of tuples, which gets iterated through a rectangle drawer.
It opens each highlighted file to show it's been annotated, then saves it as a new image in the folder.

This project was straightforward in requirements, but a few design decisions were made. Noticing a corrupt xml file in the test cases, it was important to include some form of exception handling. A simple try except block worked to avoid parsing unreadable data, and the program prints an error message so the user is aware that the file was not processed. The width and color of the highlighted rectangles emulate the example in the project specifications, so no creative measures were considered there. Finally, the choice in parsing and image manipulation libraries were based on accessible documentation and convenience of use. I had no experience working in either library previously, and consulted the following resources:

OS RESOURCES

https://www.geeksforgeeks.org/python-os-direntry-name-attribute/

https://flexiple.com/python/python-get-current-directory/


PARSER RESOURCES

https://docs.python.org/3/library/xml.dom.minidom.html

https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes


PILLOW RESOURCES

https://www.geeksforgeeks.org/python-pil-image-save-method/

https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html


OTHER RESOURCES

https://www.geeksforgeeks.org/python-convert-string-to-tuple/
