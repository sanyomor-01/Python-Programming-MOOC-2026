# Write your solution here
c_editor = 'Visual Studio Code'

c_editor = c_editor.lower()

while True:
    editor = input('Editor: ')
    editor = editor.lower()
    if editor == 'word' or editor == 'notepad':
        print('awful')
    elif editor != c_editor:
        print('not good')
    else:
        print('an excellent choice!')
        break
