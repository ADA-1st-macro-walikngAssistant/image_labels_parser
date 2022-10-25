import os
import re

path = '/home/raymond/Downloads/development/image_labels_parser/labels_1465-1830'
files = sorted(os.listdir(path))
file_names_list = []
files_dictionary = {}

# Declare a variable to store the file name
fileName = ''


def filterFileName(path):
    # If each item in the list named file meets the form of 'train_' + 7 digits + '.txt', store it in the list named file_names_list
    for file in files:
        if re.match(r'train_\d{7}.txt', file):
            file_names_list.append(file)

    # print(file_names_list)
    return file_names_list


def parseLabel(file_names_list):
    # Read the content of each file in the list named file_names_list
    for file in file_names_list:

        # Open the file
        f = open(path + '/' + file, 'r')

        # Read the content of the file
        content = f.read()

        # Split the content by the line break
        content = content.split('\n')

        print('content:', content)

        # # Replace the partial string '16 0.' with '17 0.'
        for i in range(len(content)):
            content[i] = content[i].replace('16 0.', '17 0.')
            print(f'Replaced content[{i}]:', content[i])

            # Write the content to the original text file
            f = open(path + '/' + file, 'w')
            f.write('\n'.join(content))
            f.close()

        print('\n')
    values = str(files_dictionary.values())
    print(values)


if __name__ == '__main__':
    filterFileName(files_dictionary)
    parseLabel(file_names_list)