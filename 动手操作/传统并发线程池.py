#coding:utf-8
import socket

"""下载xkcd.com网站的一个页面"""
def fetch(url):
    sock = socket.socket()
    socket.connect(('xkcd.com',80))
    request = 'GET{}HTTP/1.0\r\nHost:xkcd.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(1024*4)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    #links = parse_links(response)

"""异步操作"""
def yibu():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(("xkcd.com", 80))
    except BlockingIOError:
        pass

