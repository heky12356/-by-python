import random

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

# 从文件中读取单词列表
with open('选择性必修二U1.txt', 'r') as f:
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

