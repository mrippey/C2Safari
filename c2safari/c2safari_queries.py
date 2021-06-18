from secrets import sho_api_key
import shodan 
from prompt_toolkit.shortcuts import ProgressBar
import time 


SHODAN_API_KEY = sho_api_key

api = shodan.Shodan(SHODAN_API_KEY)

def find_cs_servers():
    try:

        query_shodan = api.search('product:"cobalt strike team server"')

        with ProgressBar() as pb:
            for _ in pb(range(100)):
                time.sleep(.01)
        print()

        if query_shodan['total'] <= 0:
            print('No results returned. Exiting...')

        print(f'First five results of {query_shodan["total"]} found:'+'\n')
        for idx, shodan_output in enumerate(query_shodan['matches'][:5], start=1):
                print(f'{idx}. IP: {shodan_output["ip_str"]}')
                print(shodan_output['data'])
                print(f'Open Ports: {shodan_output["port"]}')
                print('')
        input('Press ENTER to continue')
    
    except shodan.APIError as e:
        print(f'Error: {e}')


def find_cov_servers():
    try:

        query_shodan = api.search('ssl:Covenant http.component:Blazor')

        with ProgressBar() as pb:
            for _ in pb(range(100)):
                time.sleep(.01)
        print()

        if query_shodan['total'] <= 0:
            print('No results returned. Exiting...')

        print(f'First five results of {query_shodan["total"]} found:'+'\n')
        for idx, shodan_output in enumerate(query_shodan['matches'][:5], start=1):
                print(f'{idx}. IP: {shodan_output["ip_str"]}')
                print(shodan_output['data'])
                print(f'Open Ports: {shodan_output["port"]}')
                print('')
        input('Press ENTER to continue')

    except shodan.APIError as e:
        print(f'Error: {e}')


def find_responder_servers():
    try:

        query_shodan = api.search("HTTP/1.1 401 Unauthorized" "Date: Wed, 12 Sep 2012 13:06:55 GMT")

        with ProgressBar() as pb:
            for _ in pb(range(100)):
                time.sleep(.01)
        print()

        if query_shodan['total'] <= 0:
            print('No results returned. Exiting...')

        print(f'First five results of {query_shodan["total"]} found:'+'\n')
        
        for idx, shodan_out in enumerate(query_shodan['matches'][:5], start=1):
                print(f'{idx}. IP: {shodan_out["ip_str"]}')
                print(shodan_out['data'])
                print(shodan_out['port'])
                print('')
        input('Press ENTER to continue')

    except shodan.APIError as e:
        print(f'Error: {e}')


def find_meta_servers():
    try:

        query_shodan = api.search('http.favicon.hash:"-127886975"')

        with ProgressBar() as pb:
            for _ in pb(range(100)):
                time.sleep(.01)
        print()

        if query_shodan['total'] <= 0:
            print('No results returned. Exiting...')
      
        print(f'First five results of {query_shodan["total"]} found:'+'\n')
        for idx, shodan_output in enumerate(query_shodan['matches'][:5], start=1):
                print(f'{idx}. IP: {shodan_output["ip_str"]}')
                print(shodan_output['data'])
                print(f'Open Ports: {shodan_output["port"]}')
                print('')
        input('Press ENTER to continue')
    
    except shodan.APIError as e:
        print(f'Error: {e}')



""" Shodan Queries """
# cobalt strike: 'product:"cobalt strike team server"'
# covenant: ssl:Covenant http.component:Blazor
# responder: "HTTP/1.1 401 Unauthorized" "Date: Wed, 12 Sep 2012 13:06:55 GMT"
# metasploit: http.favicon.hash:"-127886975"