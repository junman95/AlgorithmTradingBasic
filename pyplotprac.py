import matplotlib.pyplot as plt
import datetime

import pandas_datareader.data as web

'''
#크기가 균일한 Subplots를 이용해 차트 생성

fig = plt.figure()

fig.add_subplot(211)
fig.add_subplot(212)

plt.show()


'''
'''
#내가원하는 사이즈의 axes 생성 AxesSubplot
subplot2grid는 원하는 크기의 그리드(여기서는 (4,4))를 그리고 플롯의 시작위치를 지정해서 그래프를 그린다.

'''
arkg=web.DataReader('ARKG','yahoo')

fig = plt.figure(figsize=(12,8))

top_axes=plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
bottom_axes=plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=4)
#bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)
top_axes.plot(arkg.index,arkg['Close'],label="Close")
bottom_axes.plot(arkg.index,arkg['Volume'],label='Volume')

plt.tight_layout()
plt.show()