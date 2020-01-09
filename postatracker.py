#!/usr/bin/python

import requests, json, pyjq, time, argparse
from collections import namedtuple

TRACK_ENTRY = namedtuple('TrackEntry', ('timestamp', 'location', 'status'))

def main():
    parser = argparse.ArgumentParser(description='CLI Tool to get tracking information from the Magyar Posta')
    parser.add_argument('Number', metavar='number',type=str, help='tracking number')
    parser.add_argument('-v', '--verbose', action='store_true', help='list the detailed tracking information')
    args = parser.parse_args()
    
    if args.verbose:
        json_data = track_request(args.Number)
        
        #TODO
        print "verbose mode"
    
    else:
        json_data = track_request(args.Number)

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
