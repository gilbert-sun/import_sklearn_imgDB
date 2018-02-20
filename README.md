# import_sklearn_imgDB

Import dataset from your img DB to convert to sklearn format

For AI need 要把LFW/CASIA/MS CELEB 1M資料庫讀進來，花了很多時間在研究，下面是我在github的成果
我自己寫的可以讀出所有img data set符合sklearn/keras 深度學習套件所需之格式
即格式為ndarray，由data和target和name 共三部分组成的
之後只要輸入四個參數 即
* folder name, # CASIA/MS_CELEB_1Million
* w = 64 , #寬
* h = 64 ,#高
* nPer = 1200 #人

## fetch_people_face_db.py

    Read img建立 initial img data base

## sklearn_data.py

    Let img data convert to sklearn img DB 可以使用的模式，即格式为ndarry，由data和target和name 3部分组成的数据

## casia_part folder
    Extracted some file from CASIA face img datasets

## Demo image
![Demo Image](./casia_part/1.png)

## Ref. VIP to take a look
#### 1).tensorflow/tflearn import imgDB  method
https://mrlittlepig.github.io/2017/04/30/tensorflow-for-image-processing/
#### 2).keras/sklearn  import imgDB  method
http://blog.csdn.net/nanbei2463776506/article/details/63253467
#### 3).MS_CELEB_1M 60G, aligned
http://www.msceleb.org/download/aligned
http://www.msceleb.org/celeb1m/dataset
#### 4).CASIA-WebFace.zip 4.1G full版
https://pan.baidu.com/s/1nvtn6bf
#### 5).CelebA full版
https://pan.baidu.com/s/1eSNpdRG
#### 6).lfw_6000_pair.zip 141M版
https://pan.baidu.com/s/1bpjJy8n
#### 7).lfwcrop_color.zip 145M  full版
http://conradsanderson.id.au/lfwcrop/lfwcrop_color.zip
#### 8).lfw Drop download
https://www.dropbox.com/sh/2657rgcts8x45s1/AAA8XCv6OeVjdhlk9WGoe7oha?dl=0


## Ref. Face recognization DB introduction
Ref: https://www.zhihu.com/question/33505655/answer/67492825
1.     李子青组的 CASIA-WebFace(50万，1万个人). 需申请.Center for Biometrics and Security Research
2.     微软的MSRA-CFW ( 202792 张, 1583人). 可以直接通过OneDrive下载.MSRA-CFW: Data Set of Celebrity Faces on the Web
3.     汤晓欧实验室的CelebA(20万+), 标注信息丰富. 现在可以直接从百度网盘下载 Large-scale CelebFaces Attributes (CelebA) Dataset
4.     LFW (Labeled Faces in the Wild Home) 5,749人, 13,233張http://vis-www.cs.umass.edu/lfw/