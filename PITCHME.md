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
~~システムを終了する~~ **(終了コードを伴って) SystemExit 例外を投げる**関数。
- except(else),finallyしてやればプログラムを続けることはできる
#### ただのexitとの比較
- インタプリタでもスクリプトでもどちらも使用可能
- **(終了コードを伴って) SystemExit 例外を投げる**関数。
- exitは()がないと  `Use exit() or Ctrl-D (i.e. EOF) to exit`が出力されるが、sys.exitは`<built-in function exit>`
#### os._exit(code)
- 例外を投げることなくマジでプロセス(スクリプト)が終了する。ちなみにError code必須(:integer)
