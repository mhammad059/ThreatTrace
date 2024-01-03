import os

image_folder = './dataset/images/train'
txt_folder = './dataset/labels/train'

image_files = [file for file in os.listdir(image_folder) if file.endswith('.jpeg')]

for image_file in image_files:
    txt_file = image_file[:-5] + '.txt'

    image_path = os.path.join(image_folder, image_file)
    txt_path = os.path.join(txt_folder, txt_file)

    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted image file: {image_path}")

    if os.path.exists(txt_path):
        os.remove(txt_path)
        print(f"Deleted text file: {txt_path}")
