## 文本特征抽取项目 ##

**项目名称：** 完整版本文本特征抽取

**项目要求：**[详情参见本链接](https://github.com/superxiaoqiang/blcu_py_nlp/blob/master/ch11_Python_Advanced6_NLP_1.md)

**项目功能：**
- Descriptive模块（描述性指标）
  - DESPC（段落数）
  - DESSC（句子数）
  - DESWC（字数）
  - DESPL（平均段落长度）
  - DESPLd（段落平均长度的标准差）
  - DESSL（句子平均长度）
  - DESSLd（句子平均长度的标准差）
  - DESWLsy（单词的平均音节数）
  - DESWLsyd（单词的平均音节数的标准差）
  - DESWLlt（单词中的平均字母数）
  - DESWLltd（单词平均字母数的标准偏差）
- Text Easability Principal Component Scores模块（文本易用性）
  - PCNARz（叙述性）
  - PCNARp（语法简洁性）
  - PCSYNz（单词具体性）
  - PCSYNp（
  - PCCNCz
  - PCCNCp
  - PCREFz
  - PCREFp
  - PCDCz
  - PCDCp
  - PCVERBz
  - PCVERBp
  - PCCONNz
  - PCCONNp
  - PCTEMPz
  - PCTEMPp
- 进行英文词频统计
- 将统计结果保存到csv文件中（每个txt文件对应一个csv文件结果）

**项目成员：**
- 读取文件：杨瑞霞
- 中文分词以及词频统计：张伊晗
- 英文词频统计：张伊晗
- 导出csv文件：杨澜

**文件构成：**

| 文件名 | 函数名 | 说明 | 
| :---: | :--- | :--- | 
| lib.py | 各种功能函数 |  | 
| main.py | Read() | 读取文本并输出中文和英文文本 | 
|  | CountZh()和CountEn() | 统计词频并输出csv文件 | 
|  | main.py | 主函数 | 

**说明文档：** [请下载完整html说明包](https://github.com/yangruixia/nlp/blob/master/projects/%E6%96%87%E6%9C%AC%E8%AF%BB%E5%8F%96/%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3.zip)
