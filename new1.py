import time
import random 
vyou=0
vanamy=0
for i in range(3):
    print('\n这是第%s局游戏' %(i+1))
    you=random.randrange(50,100)
    anamy=random.randrange(50,100)
    heat_you=random.randrange(2,40)
    heat_anamy=random.randrange(2,40)
    print('【玩家】\n血量：%s\n攻击：%s' %(you,heat_you))
    print('----------------------------------')
    time.sleep(1.5)
    print('【敌人】\n血量：%s\n攻击：%s' %(anamy,heat_anamy))
    print('----------------------------------')
    time.sleep(1.5)
    
    while True:
        you=you-heat_anamy
        anamy=anamy-heat_you
        if you<=0 and anamy>=0:
            print('you lose')
            vanamy=vanamy+1
            break
        elif you>0 and anamy>0:
            print('你对敌人发起了攻击，敌方血量还剩'+str(anamy))
            print('敌人对你发起了攻击，你血量还剩'+str(you))
            time.sleep(1.5)
            continue
        elif you>0 and anamy<=0:
            print('you win!')
            vyou=vyou+1
            break
        else:
            print('你们同归于尽了！')
            break
    print('你的积分：'+str(vyou)+'\n敌人的积分：'+str(vanamy))
    time.sleep(2)
if vyou>vanamy:
    print('你取得了最终的胜利！')
elif vanamy>vyou:
    print('很遗憾，你输了！')
else:
    print('平了')