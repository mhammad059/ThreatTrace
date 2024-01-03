import os
import glob
import xml.etree.ElementTree as ET
import cv2

def convert_xml_to_yolo(xml_path, image_width, image_height):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    objects = root.findall('object')
    annotations = []

    for obj in objects:
        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        # Convert bounding box coordinates to YOLO format
        x_center = (xmin + xmax) / (2.0 * image_width)
        y_center = (ymin + ymax) / (2.0 * image_height)
        bbox_width = (xmax - xmin) / image_width
        bbox_height = (ymax - ymin) / image_height

        annotation = f"0 {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}"
        annotations.append(annotation)

    return annotations

def convert_dataset_to_yolo(xml_folder, image_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    xml_files = glob.glob(os.path.join(xml_folder, '*.xml'))

    for xml_file in xml_files:
        file_name = os.path.basename(xml_file)
        image_name = file_name.replace('.xml', '.jpg')
        image_path = os.path.join(image_folder, image_name)

        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        yolo_annotations = convert_xml_to_yolo(xml_file, image_width, image_height)

        output_file = os.path.join(output_folder, file_name.replace('.xml', '.txt'))
        with open(output_file, 'w') as f:
            f.write('\n'.join(yolo_annotations))

        print(f"Converted {xml_file} to YOLO format.")

# Replace this function with your implementation to get image dimensions
def get_image_dimensions(image_path):
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape
    return image_width, image_height

# Example usage:
xml_folder = "./images/annotations_test/xmls"
image_folder = "./images/images_test"
output_folder = "./annotations_yolo"
convert_dataset_to_yolo(xml_folder, image_folder, output_folder)