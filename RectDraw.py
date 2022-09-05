# Aamir Mohammed
# Assignment 1
# CS 435
# 9/6/2022

from xml.dom.minidom import parse, parseString
import os
from PIL import Image, ImageDraw

def string_to_tuple_set(list_str):
    # a helper method to convert parsed strings of bound lists
    # into tuples that are proper inputs for the rectangle drawer
    # '[0,0][0,0]'   -->    [(0,0),(0,0)]
    string = ''
    list = []
    # iterate through the string for tuple values
    for i in range(len(list_str)):
        if list_str[i] != '[' and list_str[i] != ']':
            string += list_str[i]
        # at the end of a string list
        # add it as a tuple to the final list
        if list_str[i] == ']':
            tup = tuple(map(int,string.split(',')))
            string = ''
            list.append(tup)
    return list

# get all xml and pngs from current directory
directory = os.getcwd()
for xmlfile in os.scandir(directory):
    if xmlfile.is_file():
        if xmlfile.path[-3:] == 'xml':
            current_xml = xmlfile.path

            for pngfile in os.scandir(directory):
                if pngfile.path[-3:] == 'png':
                    if xmlfile.path[:-3] == pngfile.path[:-3]:
                        current_png = pngfile.path
                        png_name = pngfile.name

            # try to parse xml files for nodes and their bounds
            try:
                parser = parse(current_xml)
                nodes = parser.getElementsByTagName("node")

                unique = []
                for node in nodes:
                    # get bounds for each leaf node
                    if node.hasChildNodes() == False:
                        bounds = node.getAttribute("bounds")

                        # reduces the rectangles drawn later
                        # possibly a performance cost
                        if bounds not in unique:
                            unique.append(string_to_tuple_set(bounds))

                # draw rectangles at each bound
                im = Image.open(current_png)
                rect = ImageDraw.Draw(im)
                for bound in unique:
                    rect.rectangle(bound, width = 7, outline = "yellow")
                im.show()
                im.save("annotated"+png_name)

            # simple exception handling for corrupted xml data
            except:
                print("Cannot process current file")
