# eecs2405_hw1
[toc]
## 功能
In this assignment, you need to write programs to analyze [open-source auto weather station data from Central Weather Bureau (CWB)](https://ci.taiwan.gov.tw/dsp/en/environmental_cwb_auto_en.aspx)
![](https://i.imgur.com/gH0ls2f.png)
##  how to setup and run your program 
**set up**
```shell=
git clone https://github.com/oliveoil212/eecs2405_hw1.git
```
**run**
the under this repo directory
```shell=
python  ./hw1.py
```
##  what are the results
![](https://i.imgur.com/AI4GBdS.png)

## 程式碼
```python=
# filter config
targets = ["C0A880", "C0F9A0", "C0G640","C0R190", "C0X260"]
ignored = ['-99.000','-999.000']
targets_data = {}
# filter
for row in data:
   id = row.get('station_id')
   wind_speed = row.get('WDSD')
   if id in targets and wind_speed not in ignored:
      targets_data.setdefault(id, []).append(float(wind_speed))
```
targets中放我們要的station_id，ignored中放要無視的數值。
這段的功能是把想要資料從data中過濾出來，放進targets_data的dictonary裡面

sample_input的targets_data<br>
![](https://i.imgur.com/WeFwZzv.png)

---
```python=
# analyze
targets.sort()
result =[]
for target in targets:
   target_WDSD_data = targets_data.get(target)
   if target_WDSD_data != None:
      max_range = str("{:.1f}".format(max(target_WDSD_data) - min(target_WDSD_data)))
   else:
      max_range = 'None'
   result.append([target, max_range])
```
利用.sort()先將targets排成Lexicographic order
取最大最小值算出max_range，並將答案依序放進result中

---
```python=
print(result)
```
sample_input的結果
![](https://i.imgur.com/VXNH4wv.png)<br>
108061213.cvs的結果
![](https://i.imgur.com/PcyP7wg.png)

