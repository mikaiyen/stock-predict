import pandas as pd 
import numpy as np
data = pd.read_csv('new.csv',thousands=',')

data['自營商買進股數']=data['自營商買進股數(自行買賣)'].fillna(0)+data['自營商買進股數(避險)'].fillna(0)
data['自營商賣出股數']=data['自營商賣出股數(自行買賣)'].fillna(0)+data['自營商賣出股數(避險)'].fillna(0)
data=data.drop(['證券代號','證券名稱','自營商買進股數(自行買賣)','自營商買進股數(避險)','自營商賣出股數(自行買賣)'
                ,'自營商賣出股數(避險)','自營商買賣超股數(自行買賣)','自營商買賣超股數(避險)'],axis=1)
data['外資買進股數']=data['外陸資買進股數(不含外資自營商)'].fillna(0)+data['外資自營商買進股數'].fillna(0)
data['外資賣出股數']=data['外陸資賣出股數(不含外資自營商)'].fillna(0)+data['外資自營商賣出股數'].fillna(0)
data['外資買賣超股數']=data['外陸資買賣超股數(不含外資自營商)'].fillna(0)+data['外資自營商買賣超股數'].fillna(0)
data=data.drop(['外陸資買進股數(不含外資自營商)','外陸資賣出股數(不含外資自營商)','外陸資買賣超股數(不含外資自營商)'
                ,'外資自營商買進股數','外資自營商賣出股數','外資自營商買賣超股數'],axis=1)
data['DateTime']=pd.to_datetime(data['Date'], format='%Y%m%d')
data=data.drop(['Date'],axis=1)
cols=data.columns.tolist()
cols=cols[-1:]+cols[:-1]
data=data[cols]
data.rename(columns={'成交股數': 'Volume', '成交筆數': 'Transaction', '成交金額': 'Value', '開盤價': 'Open'
                     , '最高價': 'High', '最低價': 'Low', '收盤價': 'Close', '漲跌(+/-)': 'Dir', '漲跌價差': 'Change'
                     , '外資買進股數': 'ForeignBuy', '外資賣出股數': 'ForeignSell', '外資買賣超股數': 'ForeignNet'
                     , '投信買進股數': 'TrustBuy', '投信賣出股數': 'TrustSell', '投信買賣超股數': 'TrustNet'
                     , '自營商買賣超股數': 'DealerNet', '自營商買進股數': 'DealerBuy', '自營商賣出股數': 'DealerSell'
                     , '三大法人買賣超股數': 'InvestorsNet', '本益比': 'PE-Ratio', '股價淨值比': 'PBR', '殖利率': 'Yield'}, inplace=True)

data['Volume']=(data['Volume']/1000).astype(int)
data['ForeignBuy']=(data['ForeignBuy']/1000).astype(int)
data['ForeignSell']=(data['ForeignSell']/1000).astype(int)
data['ForeignNet']=(data['ForeignNet']/1000).astype(int)
data['TrustBuy']=(data['TrustBuy']/1000).astype(int)
data['TrustSell']=(data['TrustSell']/1000).astype(int)
data['TrustNet']=(data['TrustNet']/1000).astype(int)
data['DealerNet']=(data['DealerNet']/1000).astype(int)
data['DealerBuy']=(data['DealerBuy']/1000).astype(int)
data['DealerSell']=(data['DealerSell']/1000).astype(int)
data['InvestorsNet']=(data['InvestorsNet']/1000).astype(int)

data=data.drop(['Value'],axis=1)

data0 = pd.read_csv('fulldata.csv',thousands=',')
data0['DateTime']=pd.to_datetime(data0['DateTime'], format='%Y/%m/%d')

datanew = pd.concat([data0,data],axis=0)

datanew.to_csv('fulldata.csv', encoding='utf-8',index=None)