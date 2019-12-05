from ebooklib import epub
import ebooklib
import os, sys
import prompt_toolkit as pt
import html2text
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.buffer import  Buffer

def OpenFile(file):
    book = epub.read_epub(file)
    chapters = list()
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text = item.get_body_content().decode("utf-8")
            text = html2text.html2text(text, '').split('\n')
            ntext = list()
            for line in text:
                if len(line) > 0:
                    ntext.append(line)
                else:
                    try:
                        ntext[len(ntext) - 1] = ntext[len(ntext) - 1] + '\n'
                    except:
                        pass
            chapters.append(ntext)
    return chapters

def main(text):
    kb = KeyBindings()
    doc = pt.document.Document(text = text, cursor_position = 0)
    Displayer = Buffer(read_only = True, multiline = True, document = doc)

    @kb.add('c-q')
    def exit_(event):
        event.app.exit()

    root_container = Window(content = BufferControl(buffer = Displayer))
    layout = Layout(root_container)
    app = Application(key_bindings = kb, layout = layout, full_screen = True)
    app.run()
    


if __name__ == '__main__':
    book = OpenFile('/home/hakiergrzonzo/Desktop/programy/syncing/epubRead/gemba.epub')
    text = str()
    for x in book[7]:
        text += ' ' + x + '\n'
    main(text)
    """
    for chapter in book:
        for line in chapter:
            print(line)
    """
