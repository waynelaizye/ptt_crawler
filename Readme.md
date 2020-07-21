# PTT Crawler (PTT爬蟲)

### Usage 

1. Give the words to be crawled in a txt (one word each row) 
2. Set file_name and params in the header
3. Run:
```console
python ptt_cralwer.py
```

It can also search multiple words for one term by giving json file and setting "is_list" to False 
ex: { 
        'TV': ['television', 'TV' , .....] 
    } 

### Params

* file_name: Specify the text file that contains the keywords to be crawled
* board: Give the list of boards to be crawled
* data_after: Set a starting date of posts (ex: '2020/07/20')
* save_path: The directory name of the output
* pages_to_crawl_each_word: The maximum pages to be crawled each word
* is_list: True if the text file is one word each row

### Sample output:
```json
[
    {
        "title": "富邦數位帳戶幫你付口罩",
        "date": "2020/03/25",
        "content": "3/25-4/10 限數存新戶，限回饋3次  https://i.imgur.com/werhaGD.jpg  網址：https://is.gd/dL3WH5  早上立馬開戶，剛剛收到核准通知，這速度...太威了，還沒開過的衝一發  ",
        "comment": [
            {
                "push": "推 ",
                "text": ": 馬上核准，你是富邦舊戶？"
            },
            {
                "push": "→ ",
                "text": ": 信用卡有三張"
            },
            {
                "push": "→ ",
                "text": ": 但沒開過一般戶"
            },
            {
                "push": "→ ",
                "text": ": 一般都會打電話確認一些資料。"
            },
            {
                "push": "推 ",
                "text": ": 就開戶送66元的概念 但送的有點少"
            }
        ]
    }
]
```
