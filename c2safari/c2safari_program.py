from prompt_toolkit import prompt
import c2safari_queries
import sys


class colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    IGREEN = "\033[92m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    PURPLE = "\033[1;35m"
    GRAY = "\033[1;30m"
    WHITE = "\033[37m"
    ORANGE = '\033[0;33m'
    

def display_menu():
    print(colors.GRAY+'''                                                                           
  ,----..       ,----,            .--.--.                                                
 /   /   \    .'   .' \          /  /    '.             .--.,                    ,--,    
|   :     : ,----,'    |        |  :  /`. /           ,--.'  \           __  ,-,--.'|    
.   |  ;. / |    :  .  ;        ;  |  |--`            |  | /\/         ,' ,'/ /|  |,     
.   ; /--`  ;    |.'  /         |  :  ;_     ,--.--.  :  : :   ,--.--. '  | |' `--'_     
;   | ;     `----'/  ;           \  \    `. /       \ :  | |-,/       \|  |   ,,' ,'|    
|   : |       /  ;  /             `----.   .--.  .-. ||  : :/.--.  .-. '  :  / '  | |    
.   | '___   ;  /  /-,            __ \  \  |\__\/: . .|  |  .'\__\/: . |  | '  |  | :    
'   ; : .'| /  /  /.`|           /  /`--'  /," .--.; |'  : '  ," .--.; ;  : |  '  : |__  
'   | '/  ./__;      :          '--'.     //  /  ,.  ||  | | /  /  ,.  |  , ;  |  | '.'| 
|   :    /|   :    .'             `--'---';  :   .'   |  : \;  :   .'   ---'   ;  :    ; 
 \   \ .' ;   | .'                        |  ,     .-.|  |,'|  ,     .-./      |  ,   /  
  `---`   `---'                            `--`---'   `--'   `--`---'           ---`-'   
                                                                  
    ''')
    print('Author: Michael Rippey')
    print() 

    print(colors.GRAY + 'Query 1 ' +  colors.BLUE+'[Cobalt Strike Query]' + colors.WHITE+' product:cobalt strike team server')
    print(colors.GRAY + 'Query 2 ' +  colors.BLUE+'[Covenant C2 Query]' + colors.WHITE+' ssl:Covenant http.component:Blazor')
    print(colors.GRAY + 'Query 3 ' +  colors.BLUE+'[Responder Query]' + colors.WHITE+' HTTP/1.1 401 Unauthorized" "Date: Wed, 12 Sep 2012 13:06:55 GMT')
    print(colors.GRAY + 'Query 4 ' +  colors.BLUE+'[Metasploit Query]' + colors.WHITE+' http.favicon.hash:"-127886975')
    print(colors.GRAY + 'Q ' +  colors.RED + 'Quit Program' + colors.END)

def main():
    while True:
        display_menu()
        print('\n')
        menu_selection = input(colors.WHITE+'[MENU] ' + colors.GREEN+'Enter a selection from the choices above:  ' + colors.WHITE)
        print('\n')
        query1 = 'product:"cobalt strike team server"'
        query2 = 'ssl:Covenant http.component:Blazor'
        query3 = "HTTP/1.1 401 Unauthorized" "Date: Wed, 12 Sep 2012 13:06:55 GMT"
        query4 = 'http.favicon.hash:"-127886975"'

        if menu_selection.lower() == 'q':
            sys.exit()
        
        elif menu_selection.lower() == '1':
            for _q in [query1]:
                c2safari_queries.base_shodan_query(_q)
        
        elif menu_selection.lower() == '2':
            for _q in [query2]:
                c2safari_queries.base_shodan_query(_q)
        
        elif menu_selection.lower() == '3':
            for _q in [query3]:
                c2safari_queries.base_shodan_query(_q)

        elif menu_selection.lower() == '4':
            for _q in [query4]:
                c2safari_queries.base_shodan_query(_q)
          
        else:
            print(f'Oops {menu_selection} was not recognized, try again')


if __name__ == '__main__':
    main()
