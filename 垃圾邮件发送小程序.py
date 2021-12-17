from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = []
while True:
    receiver_email = input('请输入收件人邮箱地址To: ')
    to_addr.append(receiver_email)
    tag = input("是否需要继续输入邮箱，如果需要输入收件邮箱，按其他按键继续；如果不再需要输入收件邮箱，按n退出，开始发送邮件\n")
    if tag == 'n':
        break

content = '''
关于这个事，我简单说两句，你明白就行，总而言之，这个事呢，现在就是这个情况，具体的呢，大家也都看得到，我因为这个身份上的问题，也得出来说那么几句，可能，你听的不是很明白，但是意思就是那么个意思。
-----这是一封自动发送的垃圾邮件-----
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'代启蒙 <%s>' % from_addr)
msg['To'] = _format_addr(u' <%s>' % to_addr)
msg['Subject'] = Header(u'关于寒假提前考试的安排', 'utf-8').encode()

try:
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print("邮件发送成功！")
except:
    print("发送失败")