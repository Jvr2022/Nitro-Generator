import random
import string
import time
from tqdm import tqdm
from colorama import Fore, Style

def print_header():
    print(f"""
    {Fore.CYAN}███╗░░██╗██╗████████╗██████╗░░█████╗░░ ██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░{Style.RESET_ALL}
    {Fore.CYAN}████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗ ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗{Style.RESET_ALL}
    {Fore.CYAN}██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║ ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝{Style.RESET_ALL}
    {Fore.CYAN}██║╚████║██║░░░██║░░░██╔══██╗██║░░██║ ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗{Style.RESET_ALL}
    {Fore.CYAN}██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝ ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║{Style.RESET_ALL}
    {Fore.CYAN}╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░ ╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝{Style.RESET_ALL}
    {Fore.CYAN}+-----------------------------------------------------------------+{Style.RESET_ALL}
    {Fore.CYAN}\x1b[37;36m{Style.RESET_ALL}
    {Fore.CYAN}Created by Jvr2022{Style.RESET_ALL}
    {Fore.CYAN}https://github.com/Jvr2022{Style.RESET_ALL}
    {Fore.CYAN}{Style.RESET_ALL}
    {Fore.CYAN}+-----------------------------------------------------------------+{Style.RESET_ALL}
    """)

def print_disclaimer():
    print(f"{Fore.RED}\nTHIS SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND.")
    print("YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER.")
    print("THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.{Style.RESET_ALL}")

def generate_nitro_codes(num):
    nitro_codes = []
    for _ in tqdm(range(num), desc="Generating Nitro Codes", unit="code"):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))
        link = f"{Fore.LIGHTMAGENTA_EX}https://discord.gift/{code}{Style.RESET_ALL}"
        nitro_codes.append(link)
    return nitro_codes

def save_to_file(nitro_codes):
    with open("Nitro.txt", "w", encoding='utf-8') as file:
        for nitro_code in nitro_codes:
            clean_code = nitro_code.replace(f"{Fore.LIGHTMAGENTA_EX}", "").replace(f"{Style.RESET_ALL}", "")
            file.write(clean_code + "\n")

def main():
    print_header()
    print_disclaimer()

    user_agreement = input(f"\n{Fore.RED}Do you accept the terms and conditions? (yes/no): {Style.RESET_ALL}").lower()

    if user_agreement != "yes":
        print(f"{Fore.RED}You must accept the terms and conditions to use this program.{Style.RESET_ALL}")
        return

    num = int(input(f'{Fore.WHITE}How many Nitro links to generate: {Style.RESET_ALL}'))

    if num <= 0:
        print(f"{Fore.RED}Please enter a valid number greater than 0.{Style.RESET_ALL}")
        return

    print(f"{Fore.GREEN}Generating {num} Nitro codes. Please wait...{Style.RESET_ALL}")

    start_time = time.time()
    nitro_codes = generate_nitro_codes(num)

    print(f"\n{Fore.GREEN}Generated Nitro Codes:{Style.RESET_ALL}")
    for code in nitro_codes:
        print(code)

    save_to_file(nitro_codes)
    elapsed_time = time.time() - start_time

    print(f"\n{Fore.GREEN}Generated {num} codes | Time taken: {elapsed_time:.6f} seconds{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Nitro codes have been saved to Nitro.txt.{Style.RESET_ALL}\n")

    time.sleep(0.2)
    input(f"{Fore.WHITE}Press Enter to close this{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
