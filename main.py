import os
import cv2
import xml.dom.minidom

### YOU EDIT HERE
images_path = "sample_data/images/" # include slash at the end
annotations_path = "sample_data/annotations_pascal_voc/" # include slash at the end
output_path = "sample_data/image_bounding_boxes/" + "{}.png" # include slash at the end; choose png/jpg or other
###

files = os.listdir(images_path)
for file in files:
    # read image
    filename, extension = os.path.splitext(file)
    img_path = images_path + filename + extension
    img = cv2.imread(img_path)
    if img is None: # pass when no img
        pass

    # read xml
    xml_path = annotations_path + filename + ".xml"

    # iterate through objects
    dom = xml.dom.minidom.parse(xml_path)
    objects = dom.getElementsByTagName("object")
    for xmlobject in objects:
        # detect bounding boxes
        boundingbox = xmlobject.getElementsByTagName("bndbox")[0]
        xmin = boundingbox.getElementsByTagName("xmin")[0]
        ymin = boundingbox.getElementsByTagName("ymin")[0]
        xmax = boundingbox.getElementsByTagName("xmax")[0]
        ymax = boundingbox.getElementsByTagName("ymax")[0]
        xmin_data = xmin.childNodes[0].data
        ymin_data = ymin.childNodes[0].data
        xmax_data = xmax.childNodes[0].data
        ymax_data = ymax.childNodes[0].data
        cv2.rectangle(img, (int(xmin_data), int(ymin_data)), (int(xmax_data), int(ymax_data)), (0, 255, 0), 1)
        ### TESTING
        # cv2.imshow("bounding", img)
        # cv2.waitKey(0) # click through to verify bounding box placement
        ###

    # write image
    flag = cv2.imwrite(output_path.format(filename), img)
    # if flag:
    #     print(filename, "processed")

print("Finished processing all " + str(len(files)) + " images.")
