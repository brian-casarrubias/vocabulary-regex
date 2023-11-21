
import re, os, sys

'''
project: vocabulary regex
description: enter a folder name, then enter vocabulary word you're looking for 
and any .txt files will be looked at using REGEX. if it finds it, the filename 
will be printed in the conosole.
'''

is_running = False
file_path = 'C:\\Users\\Brian\\Desktop'

def start():

    global is_running
    is_running = True


    print('Welcome to Brians Vocabulary Word Finder!!'.center(100,'-'))
    print()
    while is_running:
        word = input('Enter the word you\'re looking for:\t')

        vocabulary_regex = re.compile(f'{word}', re.IGNORECASE)

        print('We are currently in the desktop, so enter folder name'.center(100, '-'))
        print()
        folder_name = input('Enter folder name:\t')
        try:
            file_name = os.listdir(os.path.join(file_path, folder_name)) 
        except FileNotFoundError:
            print('Folder Not Found!')
            continue

        for file in file_name:
            
            
            if file.endswith('.txt'):
                
                with open(os.path.join(file_path, folder_name, file),  'r') as f:
                    contents = f.read()
                    find_it = vocabulary_regex.findall(contents)
                    
                    if find_it:
                        
                        print(f'The word "{word}" has been found  -->', file)
                        sys.exit()

                
                        
                        
            else:
                print('no file ends with .txt!')         

        print(f'{word} not found')    
                






if __name__ == '__main__':
    start()
    