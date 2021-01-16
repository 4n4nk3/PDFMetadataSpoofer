from pdfrw import PdfDict, PdfReader, PdfWriter

original = PdfReader('10527002-parte3.pdf')
creation_date = original.Info['/CreationDate']
modification_date = original.Info['/ModDate']

new = PdfReader('eccolo.pdf')
my_info = new.Info
dates_metadata = PdfDict(CreationDate=creation_date, ModDate=modification_date)
new.Info.update(dates_metadata)

PdfWriter().write('si/10527002-parte3.pdf', new)

print(creation_date)
print(modification_date)