KazRus = open('KazRus.opf', 'w', encoding='utf-8-sig')
KazRus.write('''<?xml version="1.0"?>
<package version="2.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId">
  <metadata>
    <dc:title>Большой казахско-русский словарь</dc:title>
    <dc:creator opf:role="aut">Қалдыбай Бектайұлы Адаптировано: Есенбаев Е.</dc:creator>
    <dc:language>kk</dc:language>
    <meta name="cover" content="my-cover-image" />
    <x-metadata>
      <DictionaryInLanguage>kk</DictionaryInLanguage>
      <DictionaryOutLanguage>ru</DictionaryOutLanguage>
      <DefaultLookupIndex>default</DefaultLookupIndex>
    </x-metadata>
  </metadata>
  <manifest>
    <item href="cover.png" id="my-cover-image" media-type="image/png" />
    <item id="cover"
          href="cover.html"
          media-type="application/xhtml+xml" />
    <item id="usage"
          href="usage.html"
          media-type="application/xhtml+xml" />
    <item id="copyright"
          href="copyright.html"
          media-type="application/xhtml+xml" />''')
for i in range(0, 190):
    KazRus.write(f'''    <item id="content{i}"
          href="content/content{i}.html"
          media-type="application/xhtml+xml" />\n''')
KazRus.write('''  </manifest>
  <spine>
    <itemref idref="cover" />
    <itemref idref="usage" />
    <itemref idref="copyright"/>\n''')
for i in range(0, 190):
    KazRus.write(f'''    <itemref idref="content{i}" />\n''')
KazRus.write('''  </spine>
  <guide>''')
KazRus.write(f'''    <reference type="index" title="IndexName" href="content/content{0}.html"/>''')
KazRus.write('''  </guide>
</package>''')