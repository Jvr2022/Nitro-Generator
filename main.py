import random
import string
import time

def print_header():
    print("""
    \033[1;36m███╗░░██╗██╗████████╗██████╗░░█████╗░░ ██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░\033[0m
    \033[1;36m████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗ ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗\033[0m
    \033[1;36m██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║ ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝\033[0m
    \033[1;36m██║╚████║██║░░░██║░░░██╔══██╗██║░░██║ ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗\033[0m
    \033[1;36m██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝ ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░██║░░██║██║░░██║\033[0m
    \033[1;36m╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░ ╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\033[0m
    \033[1;36m+-----------------------------------------------------------------+\033[0m
    \033[1;36m\x1b[37;36m\033[0m
    \033[1;36mCreated by Jvr2022\033[0m
    \033[1;36mhttps://github.com/Jvr2022\033[0m
    \033[1;36m\033[0m
    \033[1;36m+-----------------------------------------------------------------+\033[0m
    """)

def print_disclaimer():
    print("\033[1;31m\nTHIS SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND.")
    print("YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER.")
    print("THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.\033[0m")

def generate_nitro_codes(num):
  nitro_codes = []
  for _ in range(num):
      code = "".join(random.choices(
          string.ascii_uppercase + string.digits + string.ascii_lowercase,
          k=16
      ))
      link = f"\033[1;35mhttps://discord.gift/{code}\033[0m"
      nitro_codes.append(link)
  return nitro_codes

def save_to_file(nitro_codes):
  with open("Nitro.txt", "w", encoding='utf-8') as file:
      for nitro_code in nitro_codes:
          clean_code = nitro_code.replace("\033[1;35m", "").replace("\033[0m", "")
          file.write(clean_code + "\n")

def main():
    print_header()
    print_disclaimer()

    user_agreement = input("\n\033[1;31mDo you accept the terms and conditions? (yes/no): \033[0m").lower()

    if user_agreement != "yes":
        print("\033[1;31mYou must accept the terms and conditions to use this program.\033[0m")
        return

    num = int(input('\033[1;37mHow many Nitro links to generate: \033[0m'))

    if num <= 0:
        print("\033[1;31mPlease enter a valid number greater than 0.\033[0m")
        return

    print(f"\033[1;32mGenerating {num} Nitro codes. Please wait...\033[0m")

    start_time = time.time()
    nitro_codes = generate_nitro_codes(num)

    print("\n\033[1;32mGenerated Nitro Codes:\033[0m")
    for code in nitro_codes:
        print(code)

    save_to_file(nitro_codes)
    elapsed_time = time.time() - start_time

    print(f"\n\033[1;32mGenerated {num} codes | Time taken: {elapsed_time:.6f} seconds\033[0m")
    print("\033[1;36mNitro codes have been saved to Nitro.txt.\033[0m")
    print("\033[1;36mThank you for using this Nitro code generator.\033[0m")
    print("\033[1;36mFeel free to share the joy of Nitro with your friends!\033[0m\n")

    time.sleep(0.2)
    input("\033[1;37mPress Enter to close this\033[0m")

if __name__ == "__main__":
    main()
