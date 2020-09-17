## Pythonのsysモジュール

---

### はじめに

このLTではsysの基礎的で簡単な関数を4つほど紹介します。全てご存知の方もいらっしゃるかもしれませんが、ご容赦ください。  
茶番も含まれます。ご容赦ください。

---?image=selfintro.png
### 自己紹介

---

### 目次

- sysとは
- Tips
	- sys.argv
	- sys.breakpointhook()
	- sys.ps1,ps2
	- sys.exit()
---
### sys

@box[bg-gold text-white rounded box-padding](インタプリタで使用・管理している変数や、インタプリタの動作に深く関連する関数を定義)

---
### sys.argv
スクリプト実行時のコマンドライン引数のリストが格納されている
```python
import sys

if __name__ == '__main__':

	for w in sys.argv:
		print(w)
		print(type(w))
```

```
$ python check_argv.py 1 apple [1,2,3]
check_argv.py
<class 'str'>
1
<class 'str'>
apple
<class 'str'>
[1,2,3]
<class 'str'>

```
---
### sys.breakpointhook
この値を書き換え、breakpoint()の呼び出す関数にオリジナルのデバッガを設定可能。  
下記、止まらないデバッガの例

```python
import sys,random,time

def my_debug_function():
	print('俺は止まんねぇからよ、お前らが止まんねぇかぎり、その先に俺はいるぞ！')
	time.sleep(3)
	print('だからよ、、、、')
	time.sleep(4)
	print('止まるんじゃねえぞ、、、。')
	return

sys.breakpointhook = my_debug_function

if __name__ == '__main__':
	breakpoint()
```
---
### sys.ps1.ps2
対話実行の際に出るアレ
```python
>>> for i in range(3):
...     print(i)
... 
0
1
2
```

+++
#### なんと書き換え可能
```python
>>> import sys
>>> sys.ps1 = '(´·ω·`)'
(´·ω·`)sys.ps2 = '|ω·`)'
(´·ω·`)for i in range(3):
|ω·`)   print(i)
|ω·`)
0
1
2
(´·ω·`)
```

+++

### import sysしてsys.ps1,2に好きな文字列を代入するだけです。遊んでみてください

---

### sys.exit([args])
@box[bg-gold text-white rounded box-padding](~~システムを終了する~~ **(終了コードを伴って) SystemExit 例外を投げる**関数。)

- except(else),finallyしてやればプログラムを続けることはできる

+++

### ただのexit([args])との比較
- インタプリタでもスクリプトでもどちらも使用可能
- **(終了コードを伴って) SystemExit 例外を投げる**関数。
- exitは()がないと  `Use exit() or Ctrl-D (i.e. EOF) to exit`が出力されるが、sys.exitは`<built-in function exit>`

+++
### os._exit(code)
@box[bg-gold text-white rounded box-padding](例外を投げることなくマジでプロセス(スクリプト)が終了する。\nちなみにError code必須(:integer))


+++
### 復習

+++?code=sampleexit.py&lang=python
@snap[south span-100]
@[5](1がプリントされます。print関数は自動改行をしますが、endを指定することで改行ではないものにできます)
@[7-9](2がプリントされ、\nによって改行されます。sys.exit()の例外によりtry文を抜けます)
@[10-12](exceptに捕まります。3と4をプリントします。それぞれ改行)
@[14-19](5+改行コードがプリントされ改行。numberは3行目で2と定義したのでif文の中へ、例外が発生します)
@[20-21](exceptに捕まります。7をプリントします)
@[25,26](finallyで9をプリントします)
@[28-33](numberは4の再代入により>3を満たすので中のos._exit(400)が実行されます)
@[34,35](finallyで11をプリントします)
@snapend

+++
### 結果

```
1 2

3
4
5

7
9
```

1と2の間にはスペース

---
### まとめ
