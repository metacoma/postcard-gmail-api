#!/bin/sh

NAME=$1
#CODE=$2


convert ./postcard.jpg -fill red -gravity North -pointsize 30 -annotate +0+200 "$NAME!" png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+250 'Поздравляем вас с наступающим Новым годом!' png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+280 'Желаем профессиональных побед, осуществления всего задуманного' png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+300 'мира и благополучия!' png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+350 'В этом году мы хотим преподнести вам в качестве подарка' png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+380 'xxxxxxxxxx' png:- |\
convert png:- -gravity North -pointsize 20 -annotate +0+410 'xxxxxxx' png:- |\
convert png:- -gravity North -pointsize 10 -annotate +0+500 'xxxxxxx' png:- |\
convert png:- -gravity North -pointsize 10 -annotate +0+510 'Пожалуйста, ознакомьтесь с условиями продажи товаров и использования сертификата перед покупкой.' png:- |\
convert png:- -gravity North -pointsize 10 -annotate +0+520 'xxxxxx' png:- 
