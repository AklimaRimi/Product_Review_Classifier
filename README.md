# Product_Review_Classifier

# Goal

The Goal of this project is collect data from a well known website, preprocess, using the data train a NLP model, deploy and build a interface or website.

# Description
## Data Collection

For this project I've collected data from [this website](https://www.amazon.com/LUXSWAY-Wireless-Operated-Rotatable-Diplomas-Gold/product-reviews/B07NVZ5657/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=critical). Actually the `Positive and Negative` reviews. 1221 reviews are collected.

## Preprocess

I did basic NLP preprocessing. 

1. Removed any `NULL` values from dataset
2. For tokenization, Count vectorization I used model from `HuggingFace` named `distilbert-base-uncased-finetuned-sst-2-english` which is most downloaded and one of the famous models.

## Choose Model

As this project is NLP based, So I used `Blurr` api which gives better accurate. Actually `Blurr` api is combined with `fastai` and `Huggingface`, which is make sense. 

Using `Blurr` api I applied [this model](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) same as used for preprocessing.

I didn't use another model because this model already gave me **99%**  Accuracy, Which is a great Achievement.

## Deployment

For deploymet this project I've choose `HuggingFace` website which is free to use with limitations. 

You can use my work :https://huggingface.co/spaces/Rimi98/ReviewClassifier

![](https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/hf1.png)

![](https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/hf2.png)

All of my work, model and other stuff in : https://github.com/AklimaRimi/Product_Review_Classifier/tree/hugging_face/deployment

## Interface  

For this project I used `Flask` to build a website. This website is rendered.
All of my works  for this interface in : https://github.com/AklimaRimi/Product_Review_Classifier/tree/main

https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/flask.png

