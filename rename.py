#!/usr/bin/env python

from datetime import datetime
import os
import os.path
import sys


def main(target):
    dir_path = os.path.abspath(target)
    for i in os.listdir(target):

        try:   # Catch all files with the inappropriate file format
            old_name = os.path.join(dir_path, i)
            dateOnly, description = i.split(None,1) # Split String at the first Backspace and only extract the dateformat
            
            if ('.') in dateOnly:
                newDate = datetime.strptime(dateOnly, '%y_%m.%d').strftime('%Y-%m-%d')
            elif ('_') in dateOnly:
                newDate = datetime.strptime(dateOnly, '%y_%m').strftime('%Y-%m-XX')
            else:
                raise UnboundLocalError('My exit condition was met. Leaving try block')
            
            newFolderName = newDate + ' ' + description
            new_name = os.path.join(dir_path, newFolderName)
            os.rename(old_name, new_name)
        except ValueError: 
            print("Strange format detected: " + i )
            pass
        except UnboundLocalError:
            print ('Not the proper dateformat for: ' +i)
            pass
        
if __name__ == '__main__':
    main(sys.argv[1])