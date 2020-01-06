#!/usr/bin/python

import requests, json, pyjq, time
from collections import namedtuple

TRACK_ENTRY = namedtuple('TrackEntry', ('timestamp', 'location', 'status'))

def main():
    from sys import argv
    try:
        number = argv[1]
    except IndexError:
        print('Usage: {0} <tracking number>'.format(argv[0]))
        raise SystemExit(1)
    else:
        json_data = track_request(number)

        raw_data = pyjq.all('.[] | .[0].time, .[0].postaNev, .[0].tranzakcioTipusLeirasSimple',json_data)
        
        result = TRACK_ENTRY(timestamp=time.ctime(raw_data[0]/1000), location=raw_data[1], status=raw_data[2])
        
        print('\t'.join((result.timestamp, result.location, result.status)))
        
        
def track_request(number):
    url = 'https://postamobil.eu/PostaWeb/TrackingInfo?ragszam='+number+'&language=1&registered=true'
    session = requests.session()
    resp = session.get(url)
    return json.loads(resp.content)
        
if __name__ == '__main__':
    main()
