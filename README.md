# HTML Table To DataFrame

使用pyquery解析HTML的table存成DataFrame



## Installation

```bash
pip install pyquery
pip install htmltable-df
```

## Usage

### Example 

<table width="100%" border="5" bordercolor="#FF6600" bgcolor="#FFFFFF">
    <tbody>
    <tr>
        <th class="tt" colspan="2">&nbsp;</th>
        <th class="tt" colspan="5">營業收入</th>
        <th class="tt" colspan="3">累計營業收入</th>
        <th rowspan="2" class="tt">備註</th>
    </tr>
    <tr>
        <th class="tt">公司<br>代號</th>
        <th class="tt">公司名稱</th>
        <th class="tt">當月營收</th>
        <th class="tt">上月營收</th>
        <th class="tt">去年當月營收</th>
        <th class="tt">上月比較<br>增減(%)</th>
        <th class="tt">去年同月<br>增減(%)</th>
        <th class="tt">當月累計營收</th>
        <th class="tt">去年累計營收</th>
        <th class="tt">前期比較<br>增減(%)</th>
    </tr>
    <tr align="right">
        <td align="center">1101</td>
        <td align="left">台泥</td>
        <td nowrap=""> 10,757,628</td>
        <td nowrap=""> 11,539,982</td>
        <td nowrap=""> 7,858,569</td>
        <td nowrap=""> -6.77</td>
        <td nowrap=""> 36.89</td>
        <td nowrap=""> 57,500,244</td>
        <td nowrap=""> 45,893,851</td>
        <td nowrap=""> 25.28</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1102</td>
        <td align="left">亞泥</td>
        <td nowrap=""> 7,549,925</td>
        <td nowrap=""> 7,698,165</td>
        <td nowrap=""> 5,331,442</td>
        <td nowrap=""> -1.92</td>
        <td nowrap=""> 41.61</td>
        <td nowrap=""> 39,010,235</td>
        <td nowrap=""> 28,812,149</td>
        <td nowrap=""> 35.39</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1103</td>
        <td align="left">嘉泥</td>
        <td nowrap=""> 172,927</td>
        <td nowrap=""> 185,856</td>
        <td nowrap=""> 143,629</td>
        <td nowrap=""> -6.95</td>
        <td nowrap=""> 20.39</td>
        <td nowrap=""> 1,000,927</td>
        <td nowrap=""> 1,058,885</td>
        <td nowrap=""> -5.47</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1104</td>
        <td align="left">環球水泥</td>
        <td nowrap=""> 337,575</td>
        <td nowrap=""> 426,170</td>
        <td nowrap=""> 318,948</td>
        <td nowrap=""> -20.78</td>
        <td nowrap=""> 5.84</td>
        <td nowrap=""> 2,314,855</td>
        <td nowrap=""> 2,159,764</td>
        <td nowrap=""> 7.18</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1108</td>
        <td align="left">幸福水泥</td>
        <td nowrap=""> 276,298</td>
        <td nowrap=""> 294,581</td>
        <td nowrap=""> 243,699</td>
        <td nowrap=""> -6.20</td>
        <td nowrap=""> 13.37</td>
        <td nowrap=""> 1,684,245</td>
        <td nowrap=""> 1,761,992</td>
        <td nowrap=""> -4.41</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1109</td>
        <td align="left">信大水泥</td>
        <td nowrap=""> 577,408</td>
        <td nowrap=""> 625,561</td>
        <td nowrap=""> 418,868</td>
        <td nowrap=""> -7.69</td>
        <td nowrap=""> 37.84</td>
        <td nowrap=""> 2,809,558</td>
        <td nowrap=""> 2,317,812</td>
        <td nowrap=""> 21.21</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <td align="center">1110</td>
        <td align="left">東泥</td>
        <td nowrap=""> 119,405</td>
        <td nowrap=""> 142,543</td>
        <td nowrap=""> 107,913</td>
        <td nowrap=""> -16.23</td>
        <td nowrap=""> 10.64</td>
        <td nowrap=""> 792,195</td>
        <td nowrap=""> 684,515</td>
        <td nowrap=""> 15.73</td>
        <td align="center">-</td>
    </tr>
    <tr align="right">
        <th class="tt" nowrap="" colspan="2" align="center">合計</th>
        <td nowrap=""> 19,791,166</td>
        <td nowrap=""> 20,912,858</td>
        <td nowrap=""> 14,423,068</td>
        <td nowrap=""> -5.36</td>
        <td nowrap=""> 37.21</td>
        <td> 105,112,259</td>
        <td> 82,688,968</td>
        <td nowrap=""> 27.11</td>
        <td>&nbsp;</td>
    </tr>
    </tbody>
</table>

```python
from htmltable_df.extractor import Extractor
#html可以是PyQuery物件或
extractor = Extractor(html)
extractor.df()
```
print out:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>公司 代號</th>
      <th>公司名稱</th>
      <th>營業收入_當月營收</th>
      <th>營業收入_上月營收</th>
      <th>營業收入_去年當月營收</th>
      <th>營業收入_上月比較 增減(%)</th>
      <th>營業收入_去年同月 增減(%)</th>
      <th>累計營業收入_當月累計營收</th>
      <th>累計營業收入_去年累計營收</th>
      <th>累計營業收入_前期比較 增減(%)</th>
      <th>備註</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1101</td>
      <td>台泥</td>
      <td>10757628</td>
      <td>11539982</td>
      <td>7858569</td>
      <td>-6.77</td>
      <td>36.89</td>
      <td>57500244</td>
      <td>45893851</td>
      <td>25.28</td>
      <td>-</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1102</td>
      <td>亞泥</td>
      <td>7549925</td>
      <td>7698165</td>
      <td>5331442</td>
      <td>-1.92</td>
      <td>41.61</td>
      <td>39010235</td>
      <td>28812149</td>
      <td>35.39</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1103</td>
      <td>嘉泥</td>
      <td>172927</td>
      <td>185856</td>
      <td>143629</td>
      <td>-6.95</td>
      <td>20.39</td>
      <td>1000927</td>
      <td>1058885</td>
      <td>-5.47</td>
      <td>-</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1104</td>
      <td>環球水泥</td>
      <td>337575</td>
      <td>426170</td>
      <td>318948</td>
      <td>-20.78</td>
      <td>5.84</td>
      <td>2314855</td>
      <td>2159764</td>
      <td>7.18</td>
      <td>-</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1108</td>
      <td>幸福水泥</td>
      <td>276298</td>
      <td>294581</td>
      <td>243699</td>
      <td>-6.20</td>
      <td>13.37</td>
      <td>1684245</td>
      <td>1761992</td>
      <td>-4.41</td>
      <td>-</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1109</td>
      <td>信大水泥</td>
      <td>577408</td>
      <td>625561</td>
      <td>418868</td>
      <td>-7.69</td>
      <td>37.84</td>
      <td>2809558</td>
      <td>2317812</td>
      <td>21.21</td>
      <td>-</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1110</td>
      <td>東泥</td>
      <td>119405</td>
      <td>142543</td>
      <td>107913</td>
      <td>-16.23</td>
      <td>10.64</td>
      <td>792195</td>
      <td>684515</td>
      <td>15.73</td>
      <td>-</td>
    </tr>
    <tr>
      <th>7</th>
      <td>合計</td>
      <td>合計</td>
      <td>19791166</td>
      <td>20912858</td>
      <td>14423068</td>
      <td>-5.36</td>
      <td>37.21</td>
      <td>105112259</td>
      <td>82688968</td>
      <td>27.11</td>
      <td></td>
    </tr>
  </tbody>
</table>


```python
# 也可以指定到第2列都是header 結果一樣
extractor.df(header=2)
```

## Authors

* [shiaukuan](https://github.com/shiaukuan/)


## 參考項目

* [html-table-extractor](https://github.com/yuanxu-li/html-table-extractor)

