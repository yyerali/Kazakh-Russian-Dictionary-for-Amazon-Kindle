# Kazakh-Russian-Dictionary-for-Amazon-Kindle

Неофициальная адаптация Казахско-русский словаря под Amazon Kindle.

Сгенерировать .mobi файл самостоятельно можно через kindlegen (сохранён только через Internet Archive) и промпт:
`kindlegen "____свой путь____\KazRus.opf" -c1 -gen_ff_mobi7 -dont_append_source`, а скачать через Releases.

Данный проект зародился с простого вопроса "что если?" и занял около недели работы. Был использан инструмент казахского OCR с базой в Tesseract (ocr.py) и результаты с папки dictionarytxt были адаптированны в содержимое папки content через использование API Gemini AI (для удобного автоматического форматирования), а также свой generator.py. Пока generator.py генерирует .html файлы, generator2.py сгенерировал KazRus.

ПРОЕКТ БЫЛ СОЗДАН ДЛЯ ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЕЙ И НЕ СОЗДАН С ЦЕЛЬЮ ЗАМЕНЫ БУМАЖНОЙ ВЕРСИИ

Если обнаружены ошибки, пишите на esenbaeverali@gmail.com
