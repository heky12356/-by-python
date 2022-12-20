import random
# 自动录入单词的函数
def add_word():
    english_word = input('Please enter the English word: ')
    chinese_meaning = input('Please enter the Chinese meaning: ')

    # 将单词写入文件
    with open('words.txt', 'a', encoding='utf-8') as f:
        f.write(f'{english_word},{chinese_meaning}\n')

# 回答错了之后输出正确的答案
def show_correct_answer(english_word, chinese_meaning):
    print(f'The correct answer is "{chinese_meaning}"')
# 定义一个函数用于处理录入的单词
def process_words(words):
    # 初始化变量
    correct_count = 0
    incorrect_count = 0
    passed_words = []
    failed_words = []

    # 随机打乱单词的顺序
    random.shuffle(words)

    # 遍历每一个单词
    for word in words:
        # 提取单词和对应的中文意思
        english_word = word[0]
        chinese_meaning = word[1]

        # 输出单词，请求回答中文意思
        print(f'What is the Chinese meaning of "{english_word}"? ')
        answer = input()

        # 判断回答是否正确
        if answer == chinese_meaning:
            # 答对了，将单词放到 passed_words 中
            passed_words.append(word)
            correct_count += 1
        else:
            show_correct_answer(english_word, chinese_meaning)

            # 答错了，将单词放到 failed_words 中
            failed_words.append(word)
            incorrect_count += 1

    # 输出测试结果
    if correct_count >= 60:
        print('You passed the test!')
    else:
        print('You failed the test.')
    print(f'Correct: {correct_count}, Incorrect: {incorrect_count}')

    # 返回通过测试的单词和未通过测试的单词的列表
    return passed_words, failed_words

# 定义一个函数用于更新单词列表
def update_words(words, passed_words, failed_words):
    # 将 passed_words 中的单词从 words 中删除
    for word in passed_words:
        words.remove(word)
    return words
# 选择提
def changes():
    # 读取单词列表
    with open('words.txt', 'r', encoding='utf-8') as f:
        words = []
        for line in f:
            words.append(line.strip().split(','))

    # 打乱单词顺序
    random.shuffle(words)

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
        user_input = input('Enter your answer: ')

        # 判断用户输入是否正确
        if user_input == chinese_meaning:
            print('Correct!')
        else:
            print('Incorrect. The correct answer is:', chinese_meaning)

# 从文件中读取单词列表
with open('words.txt', 'r') as f:
    words = []
    for line in f:
        # 将单词和对应的中文意思放到一个列表中
                words.append(line.strip().split(','))

# 重复测试直到通过
while True:
    # 处理单词列表
    passed_words, failed_words = process_words(words)

    # 如果通过了测试，则退出循环
    if len(failed_words) == 0:
        break

    # 更新单词列表
    words = update_words(words, passed_words, failed_words)

# 将通过测试的单词写入文件
with open('passed_words.txt', 'w') as f:
    for word in passed_words:
        f.write(f"{word[0]},{word[1]}\n")

# 输出恭喜信息
print('Congratulations, you have passed all the tests!')

