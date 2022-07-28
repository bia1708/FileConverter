import re

def convert(name):
    with open(f"{name}.tsv", 'r', encoding="utf8") as myfile:
        with open(f"{name}.csv", 'w', encoding="utf8") as csv_file:
            for line in myfile:
                fileContent = re.sub("\t", ",", line)

                csv_file.write(fileContent)

if __name__ == '__main__':
    filename = input("File name: ")

    convert(filename)

