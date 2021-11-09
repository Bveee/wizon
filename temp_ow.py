import requests
from bs4 import BeautifulSoup

# search = input('Напишите модель телефона: ').replace(' ', '+')

# url = 'https://www.ozon.ru/category/smartfony-15502/'\
#     '?from_global=true&sorting=rating&text='+search

# headers = {
#     'User-Agent': 'Firefox',
#
#     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19041'
#     # 'xcid': 'b293409686e1c9241d026314704b8278',
#     # '__Secure-refresh-token': '3.0.Ibzq-SjmSAGJ5S2ocVOYCQ.88.l8cMBQAAAABhg9OSD7frs6N3ZWKgAICQoA..20211104143530.JhNFZ2cYTrW4MNvp6LGOzRG38EqWEv_6-Er5-yeSSn4',
#     # '__Secure-access-token': '3.0.Ibzq-SjmSAGJ5S2ocVOYCQ.88.l8cMBQAAAABhg9OSD7frs6N3ZWKgAICQoA..20211104143530.rcuvnG7CCc6S2TCKyixWfAKLh2JYHKhYF5A4OtQQMKE; incap_ses_584_1101384=WcJ5UmzUQhQH0/ZGqckaCJHTg2EAAAAATt0D4GqN4OosEDKE+PCKcg==',
#     # 'visid_incap_1101384': '7S0Hsno0RFS+ocqGutnWjn/Tg2EAAAAAQUIPAAAAAABeVlfXJensMfoFOshamww4',
#     # '__Secure-ext_xcid': 'b293409686e1c9241d026314704b8278',
#     # '__Secure-ab-group': '88',
#     # '__Secure-user-id': '0',
#     # 'nlbi_1101384': '1lwScq40WgvO1xpQK8plmQAAAABosbWPktE3ycqa0QctrC5u',
#
#     # 'content-security-policy': "upgrade-insecure-requests;default-src https: wss: data: blob:;worker-src https: wss: data: blob:;style-src https: 'unsafe-inline';object-src 'self';script-src 'unsafe-inline' 'unsafe-eval' 'self' bundle.ozon.ru ozon2-st.secure.footprint.net *.ozone.ru *.ozon.ru connect.facebook.net *.ngenix.net shopnetic.com s.go-mpulse.net ozon-api.exponea.com *.maps.yandex.net yandex.ru yastatic.net *.yandex.ru vk.com cdn.rutarget.ru tns-counter.ru www.tns-counter.ru top-fwz1.mail.ru googleads.g.doubleclick.net www.google-analytics.com static.criteo.net sslwidget.criteo.com widget.eu.criteo.com *.o3.ru www.youtube.com www.googleadservices.com 'nonce-f2e4c4c7-4878-4179-bd84-e0f0f0c11720';report-uri https://xapi.ozon.ru/csp-log/",
#     # 'content-security-policy-report-only': "frame-src 'self' *.ozon.ru *.youtube.com creativecdn.com;report-uri https://xapi.ozon.ru/csp-log/"
# }

url = 'https://www.wildberries.ru/catalog/0/search.aspx?search=xiaomi&xsubject=515&sort=rate'
req = requests.get(url=url)  # , params=headers)
bs = BeautifulSoup(req.text, 'html.parser')
# title = bs.find('span', {'class': 'a7y a8a2 a8a6 a8b2 f-tsBodyL bj5'}).find('span').text

with open('test_html.html', 'w') as f:
    f.write(req.text)

print(url)
print(req.text)
