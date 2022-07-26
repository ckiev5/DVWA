# DVWA - Security Level: Low

## 1. Brute Force

## 2. Command Injection

## 3. CSRF

## 4. File Inclusion

## 5. File Upload

## 6. Insecure Captcha

## 7. SQL Injection
Nhap thu **"1"** vao input box:  
![SQL Injection_1](https://github.com/ckiev5/DVWA/blob/main/Images/SQL%20Injection_1.png)

Khi nhap **User ID = 1** trang web se tra ve thong tin cua **ID, First name, Surname**, vi vay cau lenh query co the la:
**SELECT first_name, last_name FROM users WHERE user_id = id;**
Thu kiem tra so column cua cau lenh query bang canh nhap **'UNION ODER BY 2--**  
![SQL Injection_2(https://github.com/ckiev5/DVWA/blob/main/Images/SQL%20Injection_2.png)

' UNION SELECT null, table_name FROM INFORMATION_SCHEMA.TABLES-- -

## 8. SQL Injection (Blind)

## 9. Weak Session IDs

## 10. XSS (DOM)
    
## 11. XSS (Reflected)
    
## 12. XSS (Stored)

## 13. CSP Bypass

## 14. JavaScript
