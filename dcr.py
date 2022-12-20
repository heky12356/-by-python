def add_word():
    english_word = input('Please enter the English word: ')
    chinese_meaning = input('Please enter the Chinese meaning: ')

    # 将单词写入文件
    with open('words.txt', 'a') as f:
        f.write(f'{english_word},{chinese_meaning}\n')
while 1:
    add_word()
