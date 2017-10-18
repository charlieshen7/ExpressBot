#!/usr/bin/python
# coding:utf-8

import random

refuse_messages = [
    '世上没有什么事情比必然与偶然更难懂了，就像要懂得木头人的爱恋之情一样困难。',
    '咱活到现在，只要是让咱感到羞耻的人，咱都可以说出那个人的名字。这些名字当中还得再加上一个新的名字，那就是汝！',
    '半吊子的聪明只会招来死亡。',
    '人呐……在这种时候似乎会说『最近的年轻人……』呗。',
    '真是的，汝惊慌失措时的样子还比较可爱呐。',
    '因为汝是个大笨驴，如果没说出来，汝根本察觉不到呗。',
    '在汝的脆弱心灵冻僵前，咱得赶紧用爪子好好抓上几道伤口才行。',
    '汝不懂也罢。不……如果连汝也发现了，咱或许会有些困扰呗。',
    '哼。俗话说一不做二不休，到时候咱也会很快地把汝吃进肚子里。',
    '因为汝这种人说谎不眨眼的啊。一定会有的没的乱写一通。',
    '汝认为所有人都要遵循汝的常识是吗？'
]

not_found_messages = [
    '说谎的时候，重点不在于说谎的内容，而在于为何要说谎。',
    '就算是咱，也有不能回答的事。',
    '汝的脑筋虽然转得快，但经验还是不够。',
    '就算如此，咱还是希望听到汝说出口。所以，重来一次。',
    '又没有人起床，也只能睡觉呗。不睡觉只会觉得冷，而且还会饿肚子。'
]


def reply_refuse():
    return random.choice(refuse_messages)


def reply_not_found():
    return random.choice(not_found_messages)