del Void-Fragments-book.aux
del Void-Fragments-book.log
del Void-Fragments-book.pdf
del Void-Fragments-book.tex

pandoc Void-Fragments.md -o Void-Fragments-book.tex --metadata-file=Void-Fragments.yaml --template=Void-Fragments.tex --pdf-engine=pdflatex --dpi=300
pdflatex Void-Fragments-book.tex

pause