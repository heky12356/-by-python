words = """
1.,complex          adj.复杂的，难懂的，(语法)复合的
2.,recall            vt.&vi.记起，回想起
3.,qualification       n.(通过考试或学习课程取得的)资格，学历
4.,qualify           vt.&vi.(使)具备资格，(使)合格
5.,ambition          n.追求的目标，夙愿，野心，抱负
6.,ambitious         adj.有野心的，有雄心的
7.,adaptation        n.适应，改编本
8.,comfort          n./vt.安慰，令人感到安慰的人或事物，舒服，安逸/安慰，抚慰
9.,tutor             n.(英国大学中的)助教，导师，家庭教师
10.,cite              vt.引用，引述
11.,participation       n.参加，参与
12.,participate        vi.参加，参与
13.,participate in      参加，参与
14.,presentation        n.报告，陈述，出示，拿出
15.,speak up          大声点说，明确表态
16.,feel at home       舒服自在，不拘束
17.,engage            vi./vt.参加，参与(活动)│吸引(注意力、兴趣)
18.,engage in          (使)从事，参与；
19.,involve            vi.包含，需要，涉及，影响,(使)参加
20.,get involved in      参与，卷入，与……有关联
21.,messenger         n.送信人，信使
22.,edition            n.(报纸、杂志)一份，(广播、电视节目)一期、一辑，版次
23.,culture shock       文化冲击
24.,zone             n.(有别于周围的)地区，地带，区域
25.,comfort zone       舒适区，舒适范围
26.,overwhelming      adj.无法抗拒的，巨大的，压倒性的
27.,homesickness       n.思乡病，乡愁
28.,motivated          adj.积极的，主动的
29.,motivation          n.动力，积极性，动机
30.,motivate            vt. 成为……的动机，激发，激励
31.,advisor            n.顾问
32.,adviser            n.顾问
33.,reasonable          adj.有道理的，合情理的
34.,expectation         n.期望，预期，期待
35.,applicant           n.申请人
36.,firm               n./adj.公司，商行，事务所│结实的，牢固的，坚定的
37.,exposure           n.接触，体验，暴露，揭露
38.,expose             vt.使接触，使体验，显露，使暴露于(险境)
39.,insight             n.洞察力，眼光
40.,departure           n.离开，启程，出发
41.,setting            n.环境，背景，(小说等的)情节背景
42.,grasp             vt.理解，领会，抓紧
43.,dramatic          adj.巨大的，突然的，急剧的，喜剧(般)的
44.,expense           n.费用，花费，开销
45.,cost an arm and a leg  (使)花一大笔钱
46.,tremendous        adj.巨大的，极大的
47.,behave              vt./vi.&vt.表现/表现得体，有礼貌
48.,surroundings          n.环境，周围的事物
49.,surrounding          adj.周围的，附近的
50.,mature              adj.成熟的
51.,depressed            adj.沮丧的，意志消沉的
52.,depress              vt.使沮丧，使忧愁
53.,boom               vi./n.迅速发展，繁荣/迅速发展，繁荣
54.,strengthen           vi.&vt.加强，增强，巩固
55.,deny                vt.否认，否定，拒绝
56.,optimistic            adj乐观的
57.,gain                v./n.获得，贏得，取得，增加│好处，增加
58.,perspective           n.(思考问题的)角度，观点
59.,competence          n.能力，胜任，本领
60.,competent          adj.有能力的，称职的
61.,envoy               n.使者，使节，代表
62.,cooperate           vi.合作，协作，配合
63.,angle                n.角，角度，立场
64.,outlook              n.前景，可能性，观点
65.,belt                 n.腰带，地带
66.,initiative             n.倡议，新方案
67.,sincerely             adv.真诚地，诚实地
68.,budget              n.预算
69.,side with            支持，站在……的一边
70.,logical              adj.合乎逻辑的，合情合理的
71.,as far as I know        据我所知
72.,as far as I am concerned 就我而言，依我看来
73.,in summary           总的来说，总之
74.,generally speaking      一般来说
75.,outcome             n.结果，效果
76.,Rome               罗马(意大利首都)，(史)罗马城，罗马帝国
77.,Aisha                艾莎
78.,the Belt and Road Initiative  “一带一路”倡议科

"""

# 按行分割字符串
lines = words.strip().split('\n')

# 将单词写入文件
with open('words.txt', 'a') as f:
    for line in lines:
        # 使用空格分割单词和意思
        english_word, chinese_meaning = line.split(' ',1)
        # 将单词写入文件
        f.write(f'{english_word},{chinese_meaning}\n')


