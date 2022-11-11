import random
def in_dream(day=0, dead=False, kicked=False): #设定函数的初始状态
    dead = not random.randrange(0, 10)   #给dead设定一个随机数，不属于0-9
    kicked = not random.randrange(0, 10) #给kicked 设定一个随机数，不属于0-9
    day += 1   #天数加1
    print('dead:', dead, 'kicked:', kicked)  #打印dead 和kicked的 布尔值

    if dead:  #如果dead为真，即在梦里死掉  ，打印字符串
        print(f"I slept {day} days, and was dead to wake up...")
        return day   #返回dead为真的day的值，即天数
    elif kicked:#如果kicked为真，即在梦里被踢出来，打印字符串
        print(f"I slept {day} days, and was kicked to wake up ...")
        return day   #返回kicked为真的day的值，即天数
    return in_dream(day)  #返回函数的天数
print('The in_dream() function returns:', in_dream())