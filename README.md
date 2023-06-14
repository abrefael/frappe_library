## Frappe Library

This is a library type appliction for the frappe framework (intended to be used mainly in R&D labs and such).
The Idea is that by having a DOI\ISBN or a PDF file of a specific article\text book one can add it to the list of sources that are availible to the group. By attaching a PDF file (**needs to be attached as "Public"**) and\or inserting the DOI\ISBN of the document and then clicking the "Guess" button, the system gusses information about the document (such as if it is an article or a book, year and\or month of issue, authors etc.) thus decreasing the chance to have doubles or triples of the same document.


#### Requirements
Requires Frappe Framework 14 installed.

In addition the installation also adds to your system:

```
google>=3.0.0
requests>=2.25.1
pypdf2==2.1.0
pdftitle>=0.3
feedparser>=6.0.2
pyperclip
pdfminer.six==20221105
pymupdf==1.21.0
isbnlib
pdf2doi4frappe_library #(based on https://pypi.org/project/pdf2doi/ specialy trimmed to tailor the Frappe Library application)
```

#### Installation
```
bench get-app https://github.com/abrefael/frappe_library.git --resolve-deps
bench --site [Your site] install-app frappe_library
```
#### License

MIT
