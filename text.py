words = """
1.cholera          n.霍乱
2.severe                 adj.极为恶劣的，十分严重的，严厉的
3.diarrhoea            n.腹泻
4.dehydration        n.脱水
5.frustrated           adj.懊恼的，沮丧的，失意的
6.once and for all     最终地，彻底地
7.contradictory      adj.相互矛盾的，对立的，不一致的
8.infection               n.感染，传染
9.infect                    vt.使感染，传染
10.germ                     n.微生物，细菌，病菌
11.subscribe              vi.认购(股份)，定期订购，定期交纳(会费)
12.subscribe to             同意，赞同
13.proof                     n.证据，证明，检验
14.multiple                adj.数量多的，多种多样的
15.pump                     n.泵，抽水机，打气筒
16.water pump             水泵
17.household              n.一家人，家庭，同住一所(套)房子的人
18.suspect                   vt.&vi.n.怀疑，疑有，不信任│犯罪嫌疑人，可疑对象19.blame             vt./n.把……咎于，责怪，指责│责备，指责
20.handle            n./vt.把手，拉手，柄│处理，搬动，操纵(车辆、动物、工具等)
21.intervention            n.介入，出面，干涉
22.link                           n./vt.联系，纽带│把……连接起来，相关联
23.raw                          adj.未煮的，生的，未经处理的，原始的
24.pure                        adj.干净的，纯的，纯粹的
25.substantial              adj.大量的，价值巨大的，重大的
26.decrease          n./vt.& vi.减少，降低，减少量 (使大小、数量等)减少，减小,降低
27.thanks to                     幸亏，由于
28.statistic                        n.统计数字，统计资料，统计学
29.transform                    vt.& vi.使改观，使改变形态，改变，转变
30.epidemiology              n.流行病学
31.microscope          n.显微镜
32.thinking                       n.思想，思维，见解
33.protein                         n.蛋白质
34.cell                               n.细胞，小房间，单间牢房
35.virus                             n.病毒
36.finding                         n.发现，调查结果，(法律)判决
37.initial                          adj.最初的，开始的，第一的
38.vaccine                         n.疫苗
39.framework                    n.框架，结构
40.theoretical framework    理论框架
41.solid                               adj./n.可靠的，固体的，坚实的│固体
42.cast                                 vt.投射，向……投以(视线、笑容等)，投掷
43.shadow                            n.阴影，影子，背光处
44.rainbow                           n.彩虹
45.pour                                vt.倒出，倾泻，斟(饮料)
46.concrete                           n./adj.混凝土│混凝土制的，确实的，具体的
47.plasma                              n.血浆
48.aerospace                         n.航空航天工业
49.patriotic                            adj.爱国的
50.mechanical                       adj.机械的，发动机的，机器的
51.mechanic                            n.机械师，机械修理工
52.break out                           (战争、打斗等不愉快的事情)突然开始，爆发
53.aviation                              n.航空制造业，航空，飞行
54.defend                               vt.保卫，防守，辩解
55.jet                                       n.喷气式飞机
56.assistant                             n.助理，助手
57.in charge of                          主管，掌管
58.missile                                n.导弹
59.leadership                           n.领导，领导地位，领导才能
60.trace                                 vt./n.追溯，追踪，查出│痕迹，遗迹，踪迹
61.outstanding                       adj.优秀的，杰出的，明显的
62.gifted                                adj.有天赋的，有天才的，天资聪慧的
63.come down                       患(病)，染上(小病)
64.abstract                          adj./n.抽象的，理性的│(文献等的)摘要
65.steady                                 adj.稳定的，平稳的，稳步的
66.concept                               n.概念，观念
67.astronomer                         n.天文学家
68.astronomy                           n.天文学
69.telescope                             n.望远镜
70.besides                            prep./adv.除……之外(还)│而且，此外
71.brilliant                             adj.聪颖的，绝妙的，明亮的
72.furthermore                       adv.此外，再者
73.above all                          最重要的是，尤其是
74.fault                                   n.弱点，过错
75.shift                                   n./vi.&vt.改变，转换，轮班│转移，挪动，转向
76.vivid                                  adj.生动的，鲜明的，丰富的
77.Queen Victoria                维多利亚女王(英国女王)
78.Cambridge                      剑桥(英国城市)
79.non-Newtonian fluid        非牛顿流体
80.the Jet Propulsion Laboratory     喷气推进实验室(美国)
81.Stephen Hawking              斯蒂芬.霍金(英国物理学家)
82.the big bang theory           大爆炸宇宙论
83.Fred Hoyle                         弗雷德.霍伊尔(英国天文学家)


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


