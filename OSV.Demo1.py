#感谢使用！本汐统事一个一个较长期的项目，开学前会高频率更新，开学后......
#版本：V.DemoA_CN.SP
#！！！看源码前请服用速效救心丸，保命用！！！


#导入包，也可以初始化变量
from random import randint, uniform
from time import sleep
from os import path, system

#水代码，加载。
sleep (2)
print ("\\None*")
sleep  (2)
print ("\\True*")
sleep (1)
print ("\\Reurn_True*")
sleep (1)
print ("\\Start*")#为了高级感 

def clear():
    sleep(0.13)
    system('cls')
for _ in range (7):
    sleep (0.05)
    print ("\r┃",end = "")
    sleep(0.1)
    print ("\r╱",end = "")
    sleep (0.1)
    print ("\r－",end = "")
    sleep (0.1)
    print ("\r╲",end = "")
    sleep(0.05)
sleep (0.05)
print("\r－",end = "")
sleep (3)
print ("Using \033[3;31;40m OriginalOS\033[0m")
sleep (1)
print ("汐统加载中...")
sleep (2)
load = 0
while load <=100:
    print ("已加载\033[1;34;40m", load,"\033[0m %")
    load += randint (1,2)
    sleep (uniform(0,0.1))
print ("加载完成，正在启动。")
sleep (1)
print("操作来自",path.abspath('os.py'))
print ("欢迎使用 \033[3;31;40m OriginalOS \033[0m ")
sleep (0.5)
print ("为保障您的数据安全，本系统不会留下任何数据在云端乃至本地。")
sleep (0.5)
print ('输入"帮助"可获得帮助文档~')
print ("-----------------------------------------------------------------")
print ()

#这才是主体，while 持续响应，if + elif 来实现判断操作。小生不才，只会元组来实现模糊匹配。
while True:
    cz = input("> > > ")
    for _ in range (2):#水个加载~
        sleep (0.1)
        print ("\r┃",end="")
        sleep (0.1)
        print ("\r╱",end="")
        sleep (0.1)
        print ("\r－",end="")
        sleep (0.1)
        print ("\r╲",end="")
    print (cz,"已执行")
    print ()


    if cz == "帮助": 
        print ("""请最小化程序并自行查看源码~~~~~
""")
    elif cz == "更改背景颜色":
        color = input ("请输入您想要更改的颜色，键入“背景颜色帮助”以获得相关帮助文档。")
        if color == "黑色" :
            print ("\033[0;31;40m更改成功！")

    elif cz in ["关闭","关机"]:
        print ("汐统资源撤出开始。")
        sleep (3)
        for close in range (100):
            print ("已撤出\033[1;34;40m",close+1,"\033[0m%")
            sleep (0.08)
        print ("撤出已完成！")
        sleep (0.2)
        print ("正在清除使用痕迹...")
        sleep (0.3)
        clear()
        print ("""汐统资源及使用痕迹已清除""")
        sleep (0.2)
        clear()
        print ("即将关闭！")
        sleep (0.1)
        clear()
        print("操作来自",path.abspath('os.py'))
        sleep (0.1)
        print ("Used \033[3;31;40mOriginalOS")
        sleep (1)
        clear()
        print ("\033[0m%")
        print ("\\Close Ask*")
        sleep (0.05)
        print ("\\True*")
        clear()
        exit (0)

    elif cz in ["哼哼嗯", "114514","田所浩二","下北泽"]:
        for tshe in "哼哼哼嗯嗯嗯嗯嗯嗯啊啊啊啊啊啊嗯嗯哼////":
            print (tshe)
            sleep(0.1)
        clear()
        sleep(1)
        system('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bilibili.com/video/BV185411f7dd?share_source=copy_web&vd_source=94cc671f26dd4255c7bb2103476ed703')
        print ("欢迎回来，上面可能有亿点报错，不用管它，可以输入“清屏”来清除哟~~")

    elif cz in ["清理缓存","缓存清理","清屏","缓存清除","清除缓存"]:
        clear()

    else:
        print ("命令不存在！（错误码：114514）")
        print ("如果忘记命令，请输入 “帮助” 以获得帮助文档！")
    print ("-----------------------------------------------------")