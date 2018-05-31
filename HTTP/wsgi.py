'''
最简单的Web应用就是把HTML用文件保存好，用一个现在的HTTP服务器软件，接受用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见
的静态服务器起就是干这件事情的
如果要动态生成HTML，就需要上诉步骤自己来实现，不过接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写
动态HTML就得花个把月去读HTTP规范
正确的做法是底层代码由专门的服务器软件实现，我们用python专注生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以就需要一个
统一的接口，让我们专心用python编写web业务，这个接口就是WSGI:Web Server Gateway interface.
WSGI接口定义很简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
'''
#python中内置一个WSGI服务器
from wsgiref.simple_server import make_server

#响应函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'jack')
    return [body.encode('utf-8')]

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
#无论多发复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()
#加上返回值作为Body