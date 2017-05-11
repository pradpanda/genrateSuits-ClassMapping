import xml.etree.cElementTree as ET
import glob
import json
import re
import sys

runid=str(sys.argv[1])
path = '/var/www/coverage-details/'+runid
files = [file for file in glob.glob(path + '/**/*.xml')]


myjson = []

suitename1 = []
for file in files:
    list = []
    ambari_file = "ambari" + file.split('ambari')[1]
    suitename = ambari_file.split('_')[0]
    if not suitename in suitename1:
        suitename1.insert(0, suitename)
        tree = ET.ElementTree(file=file)
        for elem in tree.getiterator(tag='class'):
            if float(elem.get('line-rate')) > 0.0:
                list.append(elem.get('filename'))
        myjson.append({suitename: list})

with open('output.json', 'w') as outfile:
    json.dump(myjson, outfile)

    print "out put data is dumped"


