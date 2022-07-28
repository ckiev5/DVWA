# DVWA - Security Level: Medium  

## 1. Brute Force
Su dung **BurpSuite** bat goi tin khi thuc hien chuc nang **Login**:  
  
![Brute Force_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/Brute%20Force_1.png)  
  
Su dung chuc nang **Intruder**, de tan cong brute force tim kiem mat khau cua tai khoan **admin**  
**Result:**  
O muc do **Medium**, moi lan dang nhap sai se phai doi 2s, viec nay khong chong lai duoc tan cong brute froce nhung co the lam tang thoi gian thuc hien.  
Tai khoan: **admin**  
Mat khau: **password**  
## 2. Command Injection
**Payload**  
```
|| whoami
```
**Result:**  
Chuc nang **Ping a device** da thuc hien loc, loai bo cac ky tu **";" va "&&"**. Nhung bo sot doi voi ky tu **"||"**.  
![Command Injection_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/Command%20Injection_1.png)
  
## 3. CSRF
**Payload**  
```

```
**Result:**  

      
## 4. File Inclusion
**Payload**  
```

```
**Result:**  

      
## 5. File Upload
**Payload**  
```

```
**Result:**  

  
## 6. Insecure CAPTCHA
**Payload**  
```

```
**Result:**  

      
## 7. SQL Injection
**Payload**  
```

```
**Result:**  

  
## 8. SQL Injection (Blind)
**Payload**  
```

```
**Result:**  

  
## 9. Weak Session IDs
**Payload**  
```

```
**Result:**  

  
## 10. XSS (DOM)
**Payload**  
```

```
**Result:**  

  
## 11. XSS (Reflected)
**Payload**  
```

```
**Result:**  

  
## 12. XSS (Stored)
**Payload**  
```

```
**Result:**  

  
## 13. CSP Bypass
**Payload**  
```

```
**Result:**  

  
## 14. JavaScript
**Payload**  
```

```
**Result:**  

  
