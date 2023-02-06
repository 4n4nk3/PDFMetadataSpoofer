from pdfrw import PdfDict, PdfReader, PdfWriter

# Copy CreationDate and ModificationDate metadata from original file
original = PdfReader('original.pdf')
creation_date = original.Info['/CreationDate']
modification_date = original.Info['/ModDate']

# Open the fake file which metadata we want to match the original file's metadata
new = PdfReader('fake.pdf')
my_info = new.Info
dates_metadata = PdfDict(CreationDate=creation_date, ModDate=modification_date)
new.Info.update(dates_metadata)

# Write a new PDF with choosen metadata
PdfWriter().write('spoofed.pdf', new)

print(creation_date)
print(modification_date)
