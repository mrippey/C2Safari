from secrets import sho_api_key
import shodan 


SHODAN_API_KEY = sho_api_key

api = shodan.Shodan(SHODAN_API_KEY)

# Thanks to @markgreene via the PyBites Slack for helping me clean this function up
def base_shodan_query(my_query):

    query_shodan = api.search(my_query)
    print(f"Executing query: {my_query}\n")

    if query_shodan['total'] == 0:
        print(colors.RED + 'No results found. Returning to menu...\n' + colors.END)
   
    else:
        print(f'First 5 results of {query_shodan["total"]} found:\n' )
        for idx, shodan_output in enumerate(query_shodan['matches'][:5], start=1):
            print(colors.YELLOW + f'{idx}. IP Addr: {shodan_output["ip_str"]}')
            print(colors.YELLOW + f"Open ports: {shodan_output['port']}")
            print(shodan_output['data'])
    
    #return f"The result of {my_query} is ..."
