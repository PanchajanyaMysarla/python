import os
import json


path = '../../../../jbh/temp/app_masterdata_carrier'
os.chdir(path)
# print(os.listdir())

dir = '/Users/jcnt521/jbh/temp/app_masterdata_carrier/src'

carrier = '/Users/jcnt521/jbh/carrier.txt'
listOfFiles = []
for (p, d, f) in os.walk(dir):

    for file in f:
        if '.ts' in file:
            with open(carrier, 'a') as f:
                f.write('%s\n' % file)
            # listOfFiles.append(file)

# print(listOfFiles)


# with open(carrier, 'w') as f:
#     f.write(json.dumps(listOfFiles))
