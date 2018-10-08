#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import unittest
from htmltable_df.extractor import Extractor


class TestSimpleExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2'], [u'3', u'4']]
        )


class TestExtractorTransformer(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html, transformer=int)

    def test_config_transformer(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[1, 2], [3, 4]]
        )


class TestPassId(unittest.TestCase):
    def test_init_with_id(self):
        html = """
        <table id='wanted'>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        <table id='unwanted'>
            <tr>
              <td>unwanted</td>
            </tr>
        </table>
        """
        pq_html = pq(html)
        extractor = Extractor(pq_html, jquery='#wanted').parse()
        self.assertEqual(
            extractor.return_list(),
            [[u'1', u'2'], [u'3', u'4']]
        )


class TestComplexExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
                <td rowspan=2>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td colspan=2>4</td>
            </tr>
            <tr>
                <td colspan=3>5</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2', u'3'], [u'1', u'4', u'4'], [u'5', u'5', u'5']]
        )


class TestConflictedExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
                <td rowspan=2>1</td>
                <td>2</td>
                <td rowspan=3>3</td>
            </tr>
            <tr>
                <td colspan=2>4</td>
            </tr>
            <tr>
                <td colspan=2>5</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2', u'3'], [u'1', u'4', u'3'], [u'5', u'5', u'3']]
        )


class TestConflictedExtractor(unittest.TestCase):
    def setUp(self):
        html = """
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
        """
        self.extractor = Extractor(html)

    def test_return_df(self):
        self.assertEqual(
            self.extractor.df().as_matrix().tolist(),
            [['1101', '台泥', '10757628', '11539982', '7858569', '-6.77', '36.89', '57500244', '45893851', '25.28', '-'],
             ['1102', '亞泥', '7549925', '7698165', '5331442', '-1.92', '41.61', '39010235', '28812149', '35.39', '-'],
             ['1103', '嘉泥', '172927', '185856', '143629', '-6.95', '20.39', '1000927', '1058885', '-5.47', '-'],
             ['1104', '環球水泥', '337575', '426170', '318948', '-20.78', '5.84', '2314855', '2159764', '7.18', '-'],
             ['1108', '幸福水泥', '276298', '294581', '243699', '-6.20', '13.37', '1684245', '1761992', '-4.41', '-'],
             ['1109', '信大水泥', '577408', '625561', '418868', '-7.69', '37.84', '2809558', '2317812', '21.21', '-'],
             ['1110', '東泥', '119405', '142543', '107913', '-16.23', '10.64', '792195', '684515', '15.73', '-'],
             ['合計', '合計', '19791166', '20912858', '14423068', '-5.36', '37.21', '105112259', '82688968', '27.11', '']]
        )


if __name__ == '__main__':
    unittest.main()
