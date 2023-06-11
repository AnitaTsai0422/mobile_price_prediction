# 預測手機價格

## File Structure
```
Contentfeed
├── app
│    ├── api
│    │     ├── enpoints
│    │     │       ├── __init__.py 
│    │     │       └── solr.py # service進入點(接受request，進行主邏輯處理) 
│    │     ├──__init__.py 
│    │     └── router.py # Route 的設定
│    │
│    ├── models
│    │     ├──__init__.py
│    │     └──solr.py 
│    │   
│    ├── servic #邏輯層   
│    │     ├──__init__.py
│    │     ├── config.py # 保留字、Dictionary 欄位
│    │     ├──ltr # 基本都不用動(此為重構，除非Geroge有更動，如果有建議重寫因為input可能都不一樣)
│    │     │     ├── data
│    │     │     │   ├──__init__.py
│    │     │     │   ├──extractor.py   
│    │     │     │   ├──transform.py 
│    │     │     │   ├──feature.py 
│    │     │     │   └──dict
│    │     │     │       ├──store2idx.json
│    │     │     │       └──word2idx.json
│    │     │     ├── __init__.py 
│    │     │     └── main.py  # 取得ltr結果         
│    │     │
│    │     ├──solr 
│    │     │     ├── __init__.py
│    │     │     ├──solr_syntax.py #組Solr語法、前端參數的語法
│    │     │     ├──syntax.py #前端參數
│    │     │     ├──main.py #根據post data 的參數進行語法組(via import solr_syntax.py module)
│    │     │     └──url.py # 包含solr 語法、Dictionary語法、IK分詞語法
│    │     └──util 
│    │           ├── __init__.py
│    │           ├──helper.py
│    │           └──logger.py │  
│    └──main.py #服務進入點

 ```