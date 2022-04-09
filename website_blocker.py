
# !!!!!!!!!ОБЯЗАТЕЛЬНО!!!!!!!!! Запускать от имени админимтратора
from datetime import datetime # Библеотека для времени даты или даты времени

end_time = datetime(2021, 11, 10, 23)  # год , месяц , день ,час

sites_to_bloc = ['www.facebook.com', 'facebook.com']
sites_to_block = ["".join(map(lambda x: x, list(elem))) for elem in sites_to_bloc] # ['www.facebook.com', 'facebook.com'] -> ['www.facebook.com', 'facebook.com'] (Мартышка 2.0.1(чтоб использоввать мап и лямбду на списке))

hosts_pat = "C:/Windows/System32/drivers/etc/hosts"
hosts_path = "".join(map(lambda x: x, list(hosts_pat))) # "C:/Windows/System32/drivers/etc/hosts" -> "C:/Windows/System32/drivers/etc/hosts" (Мартышка 2.0(чтоб использоввать мап и лямбду))

redirec = "127.0.0.1"
redirect = "".join(map(lambda x: x, list(redirec))) # "127.0.0.1" -> "127.0.0.1" (Мартышка 2.0(чтоб использоввать мап и лямбду))


def block_websites():
    if datetime.now() < end_time:
        print("Block sites")
        with open(hosts_path, 'r+') as hostfile:  # r+ : – Открыт для чтения и записи
            hosts_content = hostfile.read() # Читаем наш хост файл

            # Пишем в него каждый сайт который нужно заблокировать но с переадресацией
            [hostfile.write(redirect + ' ' + site + '\n') for site in sites_to_block if site not in hosts_content] # Крутая реализация внутри [] делающая тоже самое что и на линии ниже
                    
                    # ^
                    # |
                    # |

            # for site in sites_to_block:
            #     if site not in hosts_content:
            #         hostfile.write(redirect + ' ' + site + '\n')
    else:
        print('Unblock sites')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines() # Читаем все линии
            hostfile.seek(0) # seek(offset[, from_what]) -> None
                             # offset : Смещение в байтах, относительно позиции, определяемой аргументом from_what.
                             # from_what=0 : Откуда следует осуществить смещение. 0 — от начала файла
            
            for line in lines:
                if not any(site in line for site in sites_to_block): # Тоже очень крутая реализация заслуживающего вашего внимания в одну строку ничем не отличающаяся от нижнего только своей краткостью и брутальностью
                    hostfile.write(line)
                    
                    # ^
                    # |
                    # |
                
                # bulik = []
                # for site in sites_to_block:
                #     bulik.append(site in line)
                # if any(bulik):
                #     hostfile.write(line)

            hostfile.truncate() # Eng: The truncate() method resizes the file to the given number of bytes. If the size is not specified, the current position will be used.


# block_websites() 

if __name__ == '__main__': # Тоже самое что и сверху но запуститься если только запустить здесь
    block_websites()
