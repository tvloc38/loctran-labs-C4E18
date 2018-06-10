from gmail import GMail, Message
from random import choice
from datetime import datetime

gmail = GMail('LocTran<loctran.mict@gmail.com>','Mict12345')
now = datetime.now()

html_content = ''' 
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa việt nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Họ t&ecirc;n : Trần Văn Lộc</p>
<p style="text-align: left;">H&ocirc;m nay nghỉ vì {{lido}}.</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Lộc</p>
'''

lido = ["ốm", "sốt", "cảm", "đau bụng", "sốt xuất huyết"]
n = choice(lido)

html_content_replace = html_content.replace('{{lido}}',n)

while True:
    if now.hour > 7:
        msg = Message('Test Message',
            to='loctran.mict@gmail.com',
            text="Hello",
            html=html_content_replace
            )
        gmail.send(msg)
        break