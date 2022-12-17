@echo off
set src_dir=" -the directory where the pdfs are placed- "
set dest_dir=" -the directory where the merged pdf will be placed- "
cd /d " -the directory of the python file- "
python pdf_merger.py %src_dir% %dest_dir%