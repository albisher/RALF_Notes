import sys

def print_banner():
    """Prints the RALF Notes ASCII logo."""
    
    # ANSI escape codes for coloring (Cyan for RALF, White for Notes)
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    logo = r"""
    ______  ___   _       ______  
    | ___ \/ _ \ | |      |  ___| 
    | |_/ / /_\ \| |      | |_    
    |    /|  _  || |      |  _|   
    | |\ \| | | || |____  | |     
    \_| \_\_| |_/\_____/  \_|     
    """
    
    subtitle = r"""
     _   _       _            
    | \ | |     | |           
    |  \| | ___ | |_ ___  ___ 
    | . ` |/ _ \| __/ _ \/ __|
    | |\  | (_) | ||  __/\__ \
    \_| \_/\___/ \__\___||___/
    """

    print(f"{CYAN}{logo}{RESET}")
    print(f"{WHITE}{subtitle}{RESET}")
    print("-" * 50)
    print(" initializing local model: ministral-3:3b...")
    print("-" * 50)

if __name__ == "__main__":
    print_banner()