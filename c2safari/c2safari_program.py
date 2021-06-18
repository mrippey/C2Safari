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

    print(colors.GRAY + '1 ' +  colors.BLUE+'[Cobalt Strike]' + colors.WHITE+' Servers with similar HTTP response headers')
    print(colors.GRAY + '2 ' +  colors.BLUE+'[Covenant C2]' + colors.WHITE+' Servers that may or may not be Covenant C2 infra')
    print(colors.GRAY + '3 ' +  colors.BLUE+'[Responder]' + colors.WHITE+' Servers with hard-coded date from source code')
    print(colors.GRAY + '4 ' +  colors.BLUE+'[Metasploit]' + colors.WHITE+' Servers with favicon hash similar to Metasploit')
    print(colors.GRAY + 'Q ' +  colors.RED + 'Quit Program')


def main():
    while True:
        display_menu()
        print('\n')
        menu_selection = input(colors.WHITE+'[MENU] ' + colors.GREEN+'Enter a selection from the choices above:  ' + colors.WHITE)
        print('\n')
        if menu_selection == '1':
            c2safari_queries.find_cs_servers()
        elif menu_selection == '2':
            c2safari_queries.find_cov_servers()
        elif menu_selection == '3':
            c2safari_queries.find_responder_servers()
        elif menu_selection == '4':
            c2safari_queries.find_meta_servers()
        elif menu_selection.lower() == 'q':
            sys.exit()
        else:
            print(f'Oops {menu_selection} was not recognized, try again')


if __name__ == '__main__':
    main()
