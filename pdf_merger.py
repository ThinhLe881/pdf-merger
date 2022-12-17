import argparse
import PyPDF2
import os

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Downloader')
    parser.add_argument('src_path', metavar='src_path', type=str, help='The directory where the pdfs are placed')
    parser.add_argument('dest_path', metavar='dest_path', type=str, help='The directory where the merged pdf will be placed')

    args = parser.parse_args()

    src_path = args.src_path
    dest_path = args.dest_path

    merger = PyPDF2.PdfFileMerger()

    count = 0

    directory = os.fsencode(src_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.pdf'):
            merger.append(os.path.join(src_path, filename))
            count += 1

    if count == 0:
        print('No pdf file found')
        exit(1)

    filename = rf'{dest_path}/Merged.pdf'
    merger.write(filename)
    merger.close()

    print('Save as: ' + dest_path)
    print('Done')

if __name__ == '__main__':
    main()