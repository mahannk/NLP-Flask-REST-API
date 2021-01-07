# Natural Language Processing

## Build a Machine Learning REST API with Spacy, Flask and Docker

### Usage

All responses will have the form

```json
{
    "articles" : ["article1", "article2", ...]
}
```

### Process articles for tagging

**Definition**

`POST /query`

**Response**

- `202 ACCEPTED` on success

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


