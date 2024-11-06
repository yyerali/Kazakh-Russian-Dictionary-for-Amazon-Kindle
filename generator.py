import os
def many(word:str):
    darder = ['л', 'м', 'н', 'ң', 'ж', 'з']
    larler = ['й', 'р', 'у', 'а', 'о', 'е', 'ы', 'і', 'ө', 'ұ', 'ү', 'э', 'ә', 'и', 'ю']
    tarter = ['б', 'в', 'г', 'д', 'п', 'ф', 'к', 'қ', 'т', 'с', 'ш', 'щ', 'х', 'ц', 'ч', 'Һ']
    softdausty = ['е', 'і', 'ө', 'ә', 'ү', 'и', 'ю']
    harddausty = ['а', 'о', 'ы', 'ұ', 'э', 'ю']
    alldausty = []
    for i in range(len(word)):
        if word[i] in softdausty or word[i] in harddausty:
            alldausty = word[i]
    try:    
        if word[-1] in darder:
            if alldausty[-1] in softdausty:
                return (word+'дер')
            else:
                return (word+'дар')
        elif word[-1] in larler:
            if alldausty[-1] in softdausty:
                return (word+'лер')
            else:
                return (word+'лар')
        elif word[-1] in tarter:
            if alldausty[-1] in softdausty:
                return (word+'тер')
            else:
                return (word+'тар')
        else:
            return word
    except:
        return word
def jatys(word:str):
    ndande = ['з']
    dade = ['а', 'о', 'е', 'ы', 'і', 'ө', 'ұ', 'ү', 'э', 'ә', 'и', 'ж', 'Һ', 'ю']
    tate = ['п', 'ф', 'к', 'қ', 'т', 'с', 'ш', 'щ', 'х', 'ц', 'ч', 'б', 'в', 'г', 'д']
    softdausty = ['е', 'і', 'ө', 'ә', 'ү', 'и', 'ю']
    harddausty = ['а', 'о', 'ы', 'ұ', 'э']
    alldausty = []
    for i in range(len(word)):
        if word[i] in softdausty or word[i] in harddausty:
            alldausty = word[i]
    try:    
        if word[-1] in ndande:
            if alldausty[-1] in softdausty:
                return (word+'нде')
            else:
                return (word+'нда')
        elif word[-1] in dade:
            if alldausty[-1] in softdausty:
                return (word+'де')
            else:
                return (word+'да')
        elif word[-1] in tate:
            if alldausty[-1] in softdausty:
                return (word+'те')
            else:
                return (word+'та')
        else:
            return word
    except:
        return word
def tabys(word:str):
    n = ['з']
    dudi = ['и', 'ж', 'ю']
    nuni = ['а', 'о', 'е', 'ы', 'і', 'ө', 'ұ', 'ү', 'э', 'ә']
    tuti = ['п', 'ф', 'к', 'қ', 'т', 'с', 'ш', 'щ', 'х', 'ц', 'ч', 'б', 'в', 'г', 'д']
    softdausty = ['е', 'і', 'ө', 'ә', 'ү', 'и', 'ю']
    harddausty = ['а', 'о', 'ы', 'ұ', 'э']
    alldausty = []
    for i in range(len(word)):
        if word[i] in softdausty or word[i] in harddausty:
            alldausty = word[i]
    try:    
        if word[-1] in dudi:
            if alldausty[-1] in softdausty:
                return (word+'ді')
            else:
                return (word+'ды')
        elif word[-1] in nuni:
            if alldausty[-1] in softdausty:
                return (word+'ні')
            else:
                return (word+'ны')
        elif word[-1] in tuti:
            if alldausty[-1] in softdausty:
                return (word+'ті')
            else:
                return (word+'ты')
        else:
            return word
    except:
        return word
with open('newfile.txt', encoding='utf-8') as new:
    neo = new.read().splitlines()
counter = 0
for i in range(0, 190):
    curfile = open(f"content/content{i}.html", 'w', encoding='utf-8')
    curfile.write('''<html xmlns:math="http://exslt.org/math" xmlns:svg="http://www.w3.org/2000/svg"
                xmlns:tl="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf"
                xmlns:saxon="http://saxon.sf.net/" xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:cx="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf"
                xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:mbp="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf"
                xmlns:mmc="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf"
                xmlns:idx="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            </head>
            <body>
                <mbp:frameset>''')    
    for y in range(i*300, (i+1)*300):
        theline = neo[y].split(' *** ')
        theline[0] = theline[0].lower()
        thelinemany = many(theline[0])
        thelinejatys = jatys(theline[0])
        thelinetabys = tabys(theline[0])
        print(thelinejatys, thelinetabys)
        if len(theline[0]) < 30 and len(theline[1]) < 60 and theline[0] != None: 
            curfile.write(f'''        <idx:entry name="default" scriptable="yes" spell="yes">
                <h5><dt><idx:orth>{theline[0].upper()}
                <idx:infl>
                <idx:iform value="{theline[0].lower()}" exact="yes"/>
                <idx:iform value="{theline[0].capitalize()}"/ exact="yes">
                </idx:infl>

                <idx:infl>
                <idx:iform value="{thelinemany.lower()}"/ exact="yes">
                <idx:iform value="{thelinemany.capitalize()}"/ exact="yes">
                </idx:infl>
                
                </idx:infl>
                <idx:iform value="{thelinejatys.capitalize()}"/ exact="yes">
                <idx:iform value="{thelinejatys.lower()}"/ exact="yes">
                </idx:infl>
                </idx:orth></dt></h5>
                <dd>&#9656; {theline[1].lower()}</dd>
                <br>
            </idx:entry>
            <hr/>\n''') 
            counter += 1      
    curfile.write("""    </mbp:frameset>
    </body>
</html>""")
