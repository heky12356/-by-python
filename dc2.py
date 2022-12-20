import random

def test_mode(word_list):
    # 读取单词列表
    with open(word_list, 'r') as f:
        words = []
        for line in f:
            words.append(line.strip().split(','))

    # 打乱单词顺序
    random.shuffle(words)

    # 打开正确答案文件和错误答案文件
    with open('correct_answers.txt', 'a') as correct_answers_file, open('incorrect_answers.txt', 'a') as incorrect_answers_file:
        # 遍历单词列表
        for english_word, chinese_meaning in words:
            # 提示用户输入中文意思
            print(f'What is the meaning of "{english_word}"?:')

            # 提供选项
            options = [chinese_meaning]
            while len(options) < 4:
                word = random.choice(words)
                if word[1] not in options:
                    options.append(word[1])

            # 打乱选项顺序
            random.shuffle(options)

            # 遍历选项
            for i, option in enumerate(options):
                print(f'{i + 1}. {option}')

            # 读取用户输入
            user_input = int(input('Enter your answer: '))

            # 判断用户答案是否正确
            if options[user_input - 1] == chinese_meaning:
                print('Correct!')
                # 将英文单词和中文意思写入正确答案文件
                correct_answers_file.write(f'{english_word},{chinese_meaning}\n')
            else:
                print(f'Incorrect. The correct answer is "{chinese_meaning}".')
                # 将英文单词和中文意思写入错误答案文件
                incorrect_answers_file.write(f'{english_word},{chinese_meaning}\n')

test_mode('必修一.txt')
