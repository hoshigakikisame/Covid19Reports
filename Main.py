from covid import Covid
from colorama import Fore, Style

print(Fore.GREEN + '\ngathering information...\n' + Style.RESET_ALL)

covid = Covid(source='worldometers')

list_negara = [print('- {}'.format(negara)) for negara in sorted(covid.list_countries())]

input_negara = input('\nNama negara : ')

if input_negara in covid.list_countries():
    hasil = covid.get_status_by_country_name(input_negara)
else:
    print(Fore.RED + "\nNama negara tidak ada dalam index!" + Style.RESET_ALL)
    quit()

print(Fore.GREEN + '\n========================\nhasil\n========================' + Style.RESET_ALL)

hasil = [print('{}  : {}'.format(item, hasil[item])) for item in hasil]
