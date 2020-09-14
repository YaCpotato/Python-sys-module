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
- sys.breakpointhook()
- sys.ps1,ps2
- sys.exit()

---
### sys.exit([args])
~~システムを終了する~~ **(終了コードを伴って) SystemExit 例外を投げる**関数。
- except(else),finallyしてやればプログラムを続けることはできる

+++

### ただのexit([args])との比較
- インタプリタでもスクリプトでもどちらも使用可能
- **(終了コードを伴って) SystemExit 例外を投げる**関数。
- exitは()がないと  `Use exit() or Ctrl-D (i.e. EOF) to exit`が出力されるが、sys.exitは`<built-in function exit>`

+++
### os._exit(code)
- 例外を投げることなくマジでプロセス(スクリプト)が終了する。ちなみにError code必須(:integer)

+++
### 復習

+++?code=sampleexit.py&lang=python
@snap[south span-100]
@[1](Socket.IO enables real-time, bidirectional, event-based communication.)
@[2,3](Tweet Stream is node module that connects to the public twitter stream.)
@[5-10](To process interesting Tweets, simply register a custom handler.)
@snapend

