# Natural Language Processing

## Getting started

Build a Machine Learning NLP REST API with Spacy, Flask and Docker

***Prerequisites***

```code
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

***Running the app***

```code
$ docker-compose up
```

### Information extraction from articles

All requests will have the form

```json
{
    "articles" : ["article1", "article2", ...]
}
```

**Definition**

`POST /query`

**Response**

- `202 ACCEPTED` on success

All responses will have the form

```json
{
    "message" : "success",
    "tags" : 
        [
            {
                "text" : "text1",
                "label" : "label1"
            },
            {
                "text" : "text2",
                "label" : "text2"
            },
            {
                "text" : "...",
                "label" : "..."              
            }
        ]
}
```


