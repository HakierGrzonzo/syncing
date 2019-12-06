from ebooklib import epub
import fileinput, json
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

def OpenChapter(chapter):
    text = chapter.get_body_content().decode("utf-8")
    text = html2text.html2text(text).split('\n')
    res = str()
    for line in text:
        res += ' ' + line + '\n'
    return res

def OpenFile(file):
    book = epub.read_epub(file)
    chapters = list()
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item)
    return chapters, book.get_metadata('DC', 'title')

def SetState(state_):
    global state
    state = state_

def Display(text, cursorPos = 0, titlebar = str()):
    kb = KeyBindings()
    doc = pt.document.Document(text = text, cursor_position = cursorPos) 
    Displayer = Buffer(read_only = True, multiline = True, document = doc)
    SetState(None)
    @kb.add('c-q')
    def exit_(event):
        SetState('exit')
        event.app.exit()

    @kb.add('l')
    def next_(event):
        SetState('next')
        event.app.exit()

    @kb.add('h')
    def prev_(event):
        SetState('next')
        event.app.exit()
    Tooltip = pt.HTML('<ansigreen>Press crtl-q to exit ' + titlebar + ' </ansigreen>')
    root_container = HSplit([
        Window(content = BufferControl(buffer = Displayer)),
        Window(content = FormattedTextControl(text = Tooltip))
        ])
            
    layout = Layout(root_container)
    app = Application(key_bindings = kb, layout = layout, full_screen = True)
    app.run()
    return Displayer.cursor_position
    
def Settings():
    try:
        file = open(os.path.expanduser('~/.tinypub.json'), 'r')
    except: 
        file = open(os.path.expanduser('~/.tinypub.json'), 'w+')
        file.write(json.dumps({'name': 'tinypub'}))
        file.close()
        file = open(os.path.expanduser('~/.tinypub.json'), 'r')
    return json.loads(file.read())

def DumpSettings(settings):
    file = open(os.path.expanduser('~/.tinypub.json'), 'w')
    file.write(json.dumps(settings))

if __name__ == '__main__':
    state = None
    settings = Settings()
    if len(sys.argv) > 1:
        fname = str()
        for x in sys.argv[1:]:
            fname += x + ' '
        fname = fname[:len(fname) - 1]
        book, bookTitle = OpenFile(fname)

    else:
        raise Exception('File not specified')
    bookTitle, x = bookTitle[0]
    try:
        chapter = settings[bookTitle]['chapter']
        cursor = settings[bookTitle]['cursor']
    except:
        settings[bookTitle] = dict()
        chapter = 0
        cursor = 0
    while state != 'exit':
        try:
            status = ' ' + str(chapter + 1) + '/' + str(len(book))
            cursor = Display(OpenChapter(book[chapter]), cursorPos = cursor, titlebar = status)
            if state == 'next':
                cursor = 0
                chapter += 1
            elif state == 'prev':
                cursor = 0
                chapter -= 1
        except Exception as e:
            print(e)
            SetState('exit')
    settings[bookTitle]['chapter'] = chapter
    settings[bookTitle]['cursor'] = cursor
    DumpSettings(settings)
