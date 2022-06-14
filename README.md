# SEM_MKT_DataSpider
SEM渠道市场推广数据爬虫-百度/360/搜狗/神马


Python环境为Python3.8

目的：获取个SEM推广平台的展现、点击、消费等推广数据
流程：
  1. 发送模拟网络请求
  2. 解析返回的json数据
  3. 处理推广数据，写入Excel
使用方法：
  运行 mkt.py 文件

以下文件分别对应几个推广平台，用于对其数据看板页面进行数据爬取。
如果平台的方法或字段有变换，则需要修改对应的代码：
  - BDmkt.py：百度营销搜索推广  https://fengchao.baidu.com/
  - SLLmkt.py：360点睛实效平台  https://dianjing.e.360.cn/
  - SGmkt.py：搜狗广告投放平台  http://xuri.p4p.sogou.com/
  - SMmkt.py：UC神马超级汇川    https://e.uc.cn/

