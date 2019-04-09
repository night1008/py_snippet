# data2bs64

把json数据转换成base64字符串，同时把`+`和`/`分别替换成`-`和`_`，同时删除末尾的`=`

目的是为了能把base64字符串放url的参数中，能够在url传递结构数据

```
cd data2bs64
python main.py
```