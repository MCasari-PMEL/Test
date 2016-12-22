#version number update script

'''
---------version number format---------

    major.minor.version.build

major number
    0 - Alpha
    1 - Beta
    2 - Release candidate
    3 - Release version

minor number
    0 - Initial
    
version
    Github version number increment

build
    build/make increment number
    
'''

'''
Imports
'''
import sys
import os

'''
Globals
'''
DEF_VAL = '#define VERSION    '
BASE_VER = DEF_VAL + '("v0.0.0.0")'

print('Input Argument')
filename = []
path = []
try:
    print(sys.argv[1])
    #filename = os.path.join(sys.argv[1],sys.argv[2])
    path = sys.argv[1]
except:
    print('No argument passed')
    path = os.getcwd()

filename = os.path.join(path,'version.h')
print(filename)
results = []
with open(filename) as inputfile:
    for line in inputfile:
        results.append(line.strip())

#search for the version definition
idx = [results.index(i) for i in results if '#define VERSION' in i][0]

#if there is no definition, append the base version to the file
if(idx == -1):
    results.append(BASE_VER)
else:

    lIdx = results[idx].find('("v') + 3
    rIdx = results[idx].find('")')

    if(lIdx == -1 or rIdx == -1):
        results[idx] = BASE_VER
    
    
    #find number of '.' 
    cnt = results[idx].count('.')

    if(cnt == 3):
        temp = results[idx][lIdx:rIdx]
        majorIdx = temp.index('.')
        minorIdx = temp.index('.',majorIdx+1)
        verIdx = temp.index('.',minorIdx+1)
        major = temp[:temp.index('.')]
        minor = temp[temp.index('.')]
            
        vStr = temp[:verIdx+1]
        build = int(temp[verIdx+1:])
        build = build + 1
        vStr = vStr + str(build)
        newLine = DEF_VAL + '("v' + vStr + '")'
      
    if(cnt == 2):
        newLine =  results[idx][:results[idx].rfind('"')] + '.1")'

    if(cnt == 1):
        newLine = results[idx][:results[idx].rfind('"')] + '.0.1")'

    if(cnt == 0):                         
        newLine = results[idx][:results[idx].rfind('"')] + '.0.0.1")'

    results[idx] = newLine

with open(filename,'w') as outputfile:
    for line in results:
        outputfile.write(line + '\n')

sys.exit(0)
