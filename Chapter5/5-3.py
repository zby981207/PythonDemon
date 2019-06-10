import re

#定义获取超链接的函数
def get_url(html):
    urls = re.findall('href=.*?>', html)  # 正则出a链接 href
    urlList = []  # 定义urlList
    for url in urls:
        url = url.replace("href=\"", '')  # 替换href="
        urlList.append(url[:-2])  # 获取的0到-2长度的字符串
    print(urlList)

#字符串信息
html1 = '''<h3>contact us</h3>
<p>contact: manager wang</p>
<p>telephone:12345666</p>
<div id="nav">
<ul>
<li><a class="nav-first" href="/">homepage</a></li>
<li><a href="/lista.php">111</a></li> 
<li><a href="/lista.php">222</a></li>
<li><a href="/order/setorder.php">333</a></li>
<li><a href="/what/cool/ista.php">444</a></li>
</ul>
</div>'''
#调用函数
get_url(html1)