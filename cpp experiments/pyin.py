from prompt_toolkit import prompt, HTML
from prompt_toolkit import print_formatted_text as print


if __name__ == '__main__':
    answer = prompt('Give me some input: ')
    print(HTML('<u>You said: %s </u>' % answer))
