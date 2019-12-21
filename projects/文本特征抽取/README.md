## 文本特征抽取项目 ##

**项目名称：** 完整版本文本特征抽取

**项目要求：**[详情参见本链接](https://github.com/superxiaoqiang/blcu_py_nlp/blob/master/ch11_Python_Advanced6_NLP_1.md)

**项目功能：**

类似于 Coh-Metrix 的简略版 Mini-Metrix

#### Coh-Metrix功能分析 ####
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
  - PCNARz（叙述性）叙述性文本讲述故事
  - PCNARp
  - PCSYNz（语法简洁性）文本中句子包含较少单词并使用更为简单、熟悉的句法结构的程度。
  - PCSYNp
  - PCCNCz（单词具体性）具体有意义的单词
  - PCCNCp
  - PCREFz（参照凝聚力）高凝聚力的文本集中体现思想，低凝聚力的文本通常更难以处理
  - PCREFp
  - PCDCz（深度内聚）因果关系和逻辑关系
  - PCDCp
  - PCVERBz（动词衔接）文本中动词重叠的程度
  - PCVERBp
  - PCCONNz（连接性）文本中包含明确的对抗性，加性和比较性连接词以表达文本中的关系的程度
  - PCCONNp
  - PCTEMPz（时间）包含更多关于时间性的线索并且具有更一致的时间性（即时态，方面）的文本更易于处理和理解
  - PCTEMPp
-  Referential Cohesion（参照内聚）本地句子或共指之间内容词的重叠
  - CRFNO1（相邻名词重叠）
  - CRFNOa（全局重叠）
  - CRFAO1（参数重叠）当一个句子中的名词与另一句子中的相同名词（单数或复数形式）重叠时，就会发生参数重叠
  - CRFAOa
  - 
  


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
