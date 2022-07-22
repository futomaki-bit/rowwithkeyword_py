fi = open('text.txt','r')
keywordfi = open('keywords.txt','r')
keyrows = keywordfi.readlines()
keywords = []
for row in keyrows:
    keywords.append(row)

rows = fi.readlines()
for row in rows:
    for keyword in keywords:
        if 'Note' not in row[:-1] and 'PS' not in row[:2]:
            if keyword[:-1] in row:
                print(row[:-1])
                break