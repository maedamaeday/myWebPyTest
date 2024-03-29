# myWebPyTest

## outline
Run a python code (or any type of program) through web browser.
A user can specify arguments in html forms and run a python script with the given arguments.
Output texts will appear in a new page.  

reference : https://qiita.com/goodboy_max/items/833d482827bf0efab45a

## how to use
1. put the scripts in this repository
1. run http server on the machine you'd like to run the script. This can be done easily with the following python command (python3 is assumed):
   ``` python -m http.server 8080 --cgi ```  
   Please do not forget to add ```--cgi``` option. ```8080``` is a port number and any different number is also available. The process should be kept during the following steps.
1. open a web browser and go to the following URL:  
   ``` http://127.0.0.1:8080 ```  
   Here the IP should be the above number in case you launch the browser on the same machine where you run the http server in the above step. You can also specify the proper IP of the machine you run the http server when you launch the browser in a different machine which is inside the same network with the server. The port number must be the same with one you specified in the above step.
1. You should see several kinds of forms to put arguments for the python script. An example code will run when you fill values with the forms and press "RUN" buttom.
1. Outputs of the example script appear in the next page.


## notes
- はまった点
  - "localhost"でなく"127.0.0.1"としてあげないと動かない. (特にpost_get_test.htmlの中で.pyを呼び出すところ)
  - 実行権限をつけておかないといけない.
  - pythonの出力がhtmlで解釈できる形になっていないと, .pyをダウンロードしようとする.

- githubの使い方
  - 公開鍵を登録しないといけない.
  - .ssh/configに使う秘密鍵を書いておかないといけない.
  - 上記で参考にしたサイト : https://qiita.com/shizuma/items/2b2f873a0034839e47ce
  - markdownがうまく書けない.
