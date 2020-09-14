## Pythonのsysモジュール

---

### はじめに

---

### 自己紹介

---

### 目次

- sysモジュール
- できること
- Tips

---
### sys
@snap[west span-40]
@box[bg-gold text-white rounded box-padding](インタプリタで使用・管理している変数や、インタプリタの動作に深く関連する関数を定義)
@snapend


---
### 今回解説する関数
- sys.argv
- sys.exit()
- sys.ps1,ps2
- sys.breakpointhook()

- sys._debugmallocstats()

---
### sys.exit
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#000000&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2020-09-14T14:14:59.983Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36\&quot; etag=\&quot;aTYT-u2BaRTozPS_oy63\&quot; version=\&quot;13.4.2\&quot; type=\&quot;device\&quot;&gt;&lt;diagram id=\&quot;G_GoNFoBZG3SDfA-N0-Y\&quot; name=\&quot;Page-1\&quot;&gt;zZVNc5swEIZ/DTPtwRlAhuBj7Ljtpb34kGNGFgtoKhAVsoH++i6W+CpJ28zYmV5Aene1Es+7jByyy5vPipbZVxmDcHw3bhzy6Pj+Zh3isxNaI4QeMUKqeGwkbxQO/CdY0bXqicdQzRK1lELzci4yWRTA9EyjSsl6npZIMd+1pCkshAOjYqk+8VhnRo38+1H/AjzN+p29cGMiOe2T7ZdUGY1lPZHI3iE7JaU2o7zZgejY9VzMuk+vRIeDKSj0vyzYsif32/mxXvk6iNznaOvVq9XaVDlTcbIf7PihwHrbRGJZPLVuLYrwx0n2gVV1MeoBE/ygbMYgjtLurTNEj9F9w6DUXBZ9WTyfqWzyLJphE1/JUxFDd2QXw3XGNRxKyrpojQ2GWqZzgTMPh2dQmqNXD4KnBWpalkPNLgbNq6y8wQHsXJA5aNViSr9gY02zXev1JtZjD5C+RbOp/5EVqe27dKg9WoMD684bnPIWTlVtdQcN1x8+/oGi93eKCRdiJ4VUl7UkphAlDPVKK/kdJpGQRXBMrkN4+MHb3+YTwgP1KeHwVoD9BeAbwE0SCNmLcOP7zdF1rwOXhP8bXLKAK6u751sAjhi8DPgYBevgSoCDd+xenI6XxCU2uWnJ/hc=&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://app.diagrams.net/js/viewer-static.min.js"></script>
