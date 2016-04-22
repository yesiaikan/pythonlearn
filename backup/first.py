__author__ = 'muli'

import os;
import time;

source = ["D:\\test"]
target_dir = "D:\\backup";
target = target_dir + time.strftime('%Y%m%d%H%M%S') + ".zip"
# zip_command = 'zip -qr %s %s' %(target, ' '.join(source))
zip_command = 'ls -l'
if os.system(zip_command) == 0:
    print('Successfull backup to', target)
else:
    print("failed")