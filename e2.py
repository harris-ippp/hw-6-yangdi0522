#！usr/bin/env python

import requests

for line in open('ELECTION_ID'):
    addr = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'.format(line[5:10]) 
    resp = requests.get(addr)
    file_name = 'president_general_{}.csv'.format(line[0:4])
    with open(file_name,'w') as output:
        output.write(resp.text)
