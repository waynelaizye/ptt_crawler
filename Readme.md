# PTT Crawler (PTT爬蟲)

PTT is the largest discussion board in Taiwan. This script crawls the posts on PTT with a clean data format.

### Usage 

1. Give the words to be crawled in a txt (one word each row) 
2. Set file_name and params in the header
3. Run:
```console
python ptt_cralwer.py
```

### Params

* <b>file_name</b>: Specify the text file that contains the keywords to be crawled
* <b>board</b>: Give the list of boards to be crawled
* <b>data_after</b>: Set a starting date of posts (ex: '2020/07/20')
* <b>save_path</b>: The directory name of the output
* <b>pages_to_crawl_each_word</b>: The maximum pages to be crawled each word
* <b>is_list</b>: 
  * <b>True</b> if the text file is one word each row.
  * <b>False</b> if need multiple keywords for one topic, (ex:
  { 
        'TV': ['television', 'TV' , .....] 
  }) 

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
