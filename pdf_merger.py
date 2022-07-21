import PyPDF2
import os
from sys import argv

src_path = argv[1]
dest_path = argv[2]

print(src_path)
print(dest_path)

merger = PyPDF2.PdfFileMerger()

directory = os.fsencode(src_path)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.pdf'):
        merger.append(os.path.join(src_path, filename))

filename = dest_path + './' + 'merged.pdf'
merger.write(filename)
merger.close()
print('Merge complete')
