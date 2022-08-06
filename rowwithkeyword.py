def rowwithkeyword(text:str,keytext:str):

    fi = open(text,'r')
    keywordfi = open(keytext,'r')
    keyrows = keywordfi.readlines()
    keywords = []
    for row in keyrows:
        keywords.append(row)

    result = ""
    rows = fi.readlines()
    for row in rows:
        for keyword in keywords:
            if 'Note' not in row[:-1] and 'PS' not in row[:2]:
                if keyword[:-1] in row:
                    result += row[:-1] + "\n"
                    break
    return result