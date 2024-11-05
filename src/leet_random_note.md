# 赎金信

赎金信为什么要从杂志里取字？

绑匪为了不暴露字迹，拿了一页杂志，在上面圈字母，组成一句话，用来勒索。

例句： The kidnappers circled letters in the magazine to form a ransom note in order not to reveal their handwriting. 绑匪为了不暴露字迹，在杂志上圈选字母组成赎金信。

## 题目描述

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

**示例 1：**

**输入：**ransomNote = "a", magazine = "b"
**输出：**false

**示例 2：**

**输入：**ransomNote = "aa", magazine = "ab"
**输出：**false

**示例 3：**

**输入**：ransomNote = "aa", magazine = "aab"
**输出**：true

**提示**：

1 <= ransomNote.length, magazine.length <= 105
ransomNote 和 magazine 由小写英文字母组成。

## 解题思路

1. 如果字符串 magazine 的长度小于字符串 ransomNote 的长度，则我们可以肯定 magazine 无法构成 ransomNote，此时直接返回 false。
1. 遍历获取 ransomNote 每个元素，判断在 magazine 是否存在，若是存在直接替换 replace(elm, '', 1) ， 这里 1， 题目中每个字符只能使用 1 次，因此每次替换只替换 1 次。magazine 最后结果 不为空 返回值为 True 。否则 返回值为 False。

## LeetCode

LeetCode 结果提交:

![LeetCode 结果提交](Img/leet_ransom.png)
