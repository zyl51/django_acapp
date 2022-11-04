from django.http import HttpResponse

def index(request):     #前端过来的页面都有request，现在用不到
    line1 = '<h1 style="text-align: center">术士之战</h1>'      #标题
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.52miji.com%2Fimage%2F2016%2F09%2F23%2F146e29c3c001304525aa6aeb40485faa.jpg&refer=http%3A%2F%2Fimg.52miji.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1669777763&t=e3eca5d086943c6070ce09a4d3f8456e" width = 1800>'

    line3 = '<hr>'      #一个分割符
    line4 = '<a href="play/">进入游戏界面</a>'  #按钮，可点击

    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'

    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.52miji.com%2Fimage%2F2016%2F09%2F23%2F146e29c3c001304525aa6aeb40485faa.jpg&refer=http%3A%2F%2Fimg.52miji.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1669777763&t=e3eca5d086943c6070ce09a4d3f8456e" width = 1800>'

    line3 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1 + line3 + '<hr>' + line2)
