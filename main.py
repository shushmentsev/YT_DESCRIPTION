if __name__ == '__main__':

    shorts_flag = False

    # Получаем фразу:
    phrase = input('Введите название видео: ').strip()

    # Обрабатываем фразу:
    phrase = phrase.split()
    phrase = ' '.join(phrase)

    # Составление имени видео:
    aan = 'a' if phrase[0] not in ['a', 'A'] else 'an'
    video_name = 'How to draw {} {} (2021) | Step by step | Drawing'.format(aan, phrase)

    # Добавление #Shorts к названию:
    video_name += ' #Shorts' if shorts_flag else ''

    # Составление описания:
    stickers_url = 'https://t.me/addstickers/HowToDraw'
    video_desc = 'Learn How to draw {} {} '.format(aan, phrase)
    video_desc += 'step by step in 2021\n\n'
    video_desc += 'Stickers: {}\n\n'.format(stickers_url)
    video_desc += '#howtodraw #drawing #{}\n'.format(''.join(list(phrase)))
    video_desc += '2021'

    # Добавление #Shorts к описанию:
    video_desc += ' #Shorts' if shorts_flag else ''
    
    # Вывод:
    print('Название видео:', '\n', video_name, '\n')
    print('Описание видео:', '\n', video_desc, '\n')
