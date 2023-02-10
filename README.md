# Product_Review_Classifier


# Goal


The objective of this project is to get information from a well-known website, preprocess it, train an NLP model using the data, then deploy it and create an interface or website.


# Description
## Data Collection


For this project I've collected data from [this website](https://www.amazon.com/LUXSWAY-Wireless-Operated-Rotatable-Diplomas-Gold/product-reviews/B07NVZ5657/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=critical). Actually the `Positive and Negative` reviews. 1221 reviews are collected.


## Preprocess


I did basic NLP preprocessing. 


1. Removed any `NULL` values from dataset
2. I utilized a model from `HuggingFace` called `distilbert-base-uncased-finetuned-sst-2-english` which is one of the most popular and most downloaded models, for tokenization and count vectorization.


## Choose Model


I chose the `Blurr` api since it provides better accuracy for this NLP-based project. Actually, `fastai` and `Huggingface` are combined with the `Blurr` API, which makes sense.


 Applied [this model] (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) using the `Blurr` api, that was identical to the model used for preprocessing.


This model previously provided me with **99%** Accuracy, which is a fantastic Achievement, thus I didn't require another one.


## Deployment


I've decided to use the free platform `HuggingFace` for the project's deployment. 


You can use my work :https://huggingface.co/spaces/Rimi98/ReviewClassifier


![](https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/hf1.png)


![](https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/hf2.png)


All of my work, model and other stuff in : https://github.com/AklimaRimi/Product_Review_Classifier/tree/hugging_face/deployment


## Interface  


I created a webpage for this project using the framework flask. This site has been rendered.
All of my works  for this interface in : https://github.com/AklimaRimi/Product_Review_Classifier/tree/main


https://github.com/AklimaRimi/Product_Review_Classifier/blob/hugging_face/images/flask.png





