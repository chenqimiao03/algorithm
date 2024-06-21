# 数据结构与算法

## 复杂度

### 时间复杂度

一个和数据量有关，只要高阶项、不要低阶项和常数项的操作次数表达式

常见复杂度一览：O(1) O(logN) O(N*logN) O(N^2) ... O(N^K) O(2^N) ... O(K^N) ... O(N!)

调和级数：1/1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/N，收敛于 O(logN)

递归函数时间复杂度分析（master 公式）：所有子问题规模相同的递归才能使用 master 公式，T(n) = a * T(n / b) + O(n^c)，其中 a,b,c 都是常数

1. 如果 log(b, a) < c，那么时间复杂度为：O(n^c)
2. 如果 log(b, a) > c，那么时间复杂度为：O(n^log(b, a))
3. 如果 log(b, a) = c，那么时间复杂度为：O(n^c * log(n))

其中：T(n) = 2 * T(n / 2) + O(n * log(n)) 的时间复杂度为：O(n * log(n))

### 最优解

先满足时间复杂度最优，然后尽量少用空间的解

## 算法

### 位运算

见 `bitwise.py`

### 归并分治

原理：

1. 思考一个问题在大范围上的答案，是否等于，**左部分的答案 + 右部分的答案 + 跨越左右产生的答案**。
2. 计算**跨越左右产生的答案**时，如果加上左、右各自有序这个设定，会不会获得计算的便利性。

如果以上两点都成立，那么该问题很可能被归并分支解决，求解答案的过程中只需要加入归并排序的过程即可，因为要让左、右各自有序，来获得计算的便利性。

### 排序

|     排序算法      |    时间复杂度    |   空间复杂度   | 稳定性 |
|:-------------:|:-----------:|:---------:|:---:|
| selectionSort |   O(N^2)    |   O(1)    |  无  |
|  bubbleSort   |   O(N^2)    |   O(1)    |  有  |
| insertionSort |   O(N^2)    |   O(1)    |  有  |
|   mergeSort   | O(N*log(N)) |   O(N)    |  有  |
|   quickSort   | O(N*log(N)) | O(log(N)) |  无  |
|   heapSort    | O(N*log(N)) |   O(1)    |  无  |
|   countSort   |    O(N)     |   O(M)    |  有  |
|   radixSort   |    O(N)     |   O(M)    |  有  |

#### 注意事项

1. 在数据量非常小的情况下**插入排序**可以做到非常迅速
2. 性能优异、实现简单且利于改进、不在乎稳定性，可以选择**随机快速排序**
3. 性能优异、不在乎额外空间占用、要求有稳定性，可以选择**归并排序**
4. 性能优异、额外空间占用要求O(1)、不在乎稳定性，可以选择**堆排序**

### 递归

代码模板：

```python
def r(level, param1, param2,...):
    # 递归中止条件
    if level > MAX_LEVEL:
        process_result
        return
    # process logic in current level
    process(level, data)
    # drill down
    r(level + 1, p1, p2,...)
    # reverse the current level status if needed
```

### 动态规划

### 贪心算法

### 字符串

#### KMP

- 对模式串求前缀和后缀相等的最大长度

例如：模式串```abbabb```

| length | 1 | 2 | 3 | 4 | 5 | 6 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| prefix | a | ab | abb | abba | abbab | \\ |
| suffix | b | bb | abb | babb | bbabb | \\ |

故字符串 ```abbabb``` 的最大长度为 3

求模式串的 $next$ 数组

例如：模式串```aabaabsaabaabst```

```i```位置的信息只和之前的字符串有关，由于 ```0```号位置之前没有字符串所以 $next[0]=-1$

```1```号位置，由于前缀和后缀都不能取到整体，所以$next[1]=0$

第```i```号位置 $next[i]=pattern[0]...pattern[i-1]$的前缀和后缀相等的最大长度


- text 和 pattern 的匹配过程

例如：

text 是 ```abbstkscabbstks...```

| index | 0 | 1| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | ... |
| :--: | :--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |
| character | a | b | b | s | t | k | s | c | a | b | b | s | t | k | s | ... |

pattern 是```abbstkscabbstkz...```

| index | 0 | 1| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | ... |
| :--: | :--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |:--: |
| character | a | b | b | s | t | k | s | c | a | b | b | s | t | k | z | ... |

由于 $text[14] != pattern[14]$ 又 $text[8]...text[13]=pattern[0]...pattern[5]$ 所以下次直接比较 $text[14]$ 和 $pattern[6]$ 即可

证明**跳过部分无论如何都匹配不到 pattern**

**text**

| index | ... | i | ...| k | ... | j | ... | x |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| character | ... | a | ... | . | . |. |... | . |


**pattern**

| index | 0 | ... | p |  ...| z | ... | q | ... | y |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| character | a | ...| . | ... | . | ... | . | ... | . |

$text$ 的子串 $text[i]...text[x-1]$和 $pattern[0]...pattern[y-1]$ 是匹配的只有 $text[x]$ 和 $pattern[y]$ 是不匹配的 

设 $pattern[0]...pattern[p]$ 和 $pattern[z]...pattern[q]$ 是 $pattern[y]$ 的最长的前后缀

假设位置 $i$ 到位置$j$ 中间的位置 $k$ 开头的子串能匹配到 $pattern$ 所以有 $text[k]...text[x]$ 和 $pattern$有等量的前缀又由于 $text[j]...text[x-1]$ 和 $pattern[0]...pattern[p]$ 是相等的，所以有 $x-1-j=p$ 而假设 $x-1-k>p$ 故假设不成立

#### Manacher

## 数据结构

### 链表

#### 时间复杂度

| 操作 | 时间复杂度 |
| :--: | :--: |
| appendleft | O(1) |
| append | O(1) |
| lookup | O(N) |
| insert | O(1) |
| delete | O(1) |

#### 链表类题目注意点

1. 如果笔试中空间不要求，直接使用容器来解决链表问题
2. 如果笔试中空间要求严格、或者在面试中面试官强调空间优化，需要使用额外空间复杂度O(1)的方法
3. 最常用的技巧：**快慢指针**
4. 链表类题目往往都是很简单的算法问题，核心考察点也并不是算法设计，而是 coding 能力

### 哈希表

哈希表用的是**数组支持按照下标随机访问数据的特性【时间复杂度为 O(1)】**，通过哈希函数把元素的键值映射为下标，然后将数据存储在数组对应下标的位置。查询元素时，用同样的哈希函数，将键值转化数组下标，从对应的数组下标的位置取数据。

#### 设计哈希函数的基本要求

1. 哈希函数计算得到的哈希值是一个非负整数
2. 如果 $KEY1 = KEY2$，那么 $hash(KEY1) = hash(KEY2)$
3. 如果 $KEY1 != KEY2$，那么 $hash(KEY1) != hash(KEY2)$

#### 哈希冲突解决方法

##### 开放寻址法

开放寻址法的核心思想是，如果出现了哈希冲突，就重新探测一个空闲位置，将其插入。

- 线性探测：如果某个数据通过哈希函数计算出对应的哈希值之后，存储位置已经存在数据，那就从当前位置开始，依次往后查找，看是否有空闲位置，直到找到位置。
- 二次探测：线性探测的探测序列为 $hash(key) + 0, hash(key) + 1, hash(key) + 2, ...$，而二次探测的探测序列则是 $hash(key) + 0, hash(key) + 1^2, hash(key) + 2^2, ...$
- 双重哈希：使用一组哈希函数 $hash_{1}(key), hash_{2}(key), hash_{3}(key), ...$，先用第一个哈希函数计算对应的哈希值，如果该位置存在数据，那么再用第二个哈希函数，依次类推，直到找到空闲的存储位置。

优点：

1. 可以有效地利用 CPU 缓存加快查询速度
2. 序列化简单

缺点：

1. 删除数据比较麻烦，需要特殊标记已经删除的数据。
2. 相比链表法，更容易发生哈希冲突。


当数据量比较小，装载因子【已在哈希表中的元素个数 / 哈希表的长度】小的时候，适合采用开放寻址法。

##### 链表法

链表法是一种更加常用的哈希冲突解决方法，相比开放寻址法，它要简单很多。如下图，在散列表中，每个“桶（bucket）”或者“槽（slot）”会对应一条链表，所有哈希值相同的元素都放到相同槽位对应的链表中。

当插入的时候，只需要通过哈希函数计算出对应的哈希槽位，将其插入到对应链表中即可，所以插入的时间复杂度是 O(1)。当查找、删除一个元素时，同样通过哈希函数计算出对应的槽，然后遍历链表查找或者删除。

![image.png](./images/a4b77d593e4cb76acb2b0689294ec17f.png)

优点：

1. 


### 堆

堆是一种特殊的完全二叉树，这个结构（大顶堆/小顶堆）中任何一个子结构的最大值/最小值都在其顶部

完全二叉树和数组前缀范围的对应：

1. i 位置的父亲节点是：(i - 1) / 2
2. i 位置的左孩子是：(i * 2) + 1
3. i 位置的右孩子是：(i * 2) + 2

### 布隆过滤器/位图

$$m=-\frac{n*ln{p}}{(ln{2})^{2}}$$

$$k=ln{2}*\frac{m}{n}$$

$$p_{1}=(1-e^{-\frac{n*k_{1}}{m_{1}}})^{k_{1}}$$

其中：

m 是 bitarray 的大小，n 是样本数量，p 是预计失误率，k 是哈希函数的个数

### 树

#### 二叉树

#### 二叉搜索树

二叉搜索树，也称有序二叉树、排序二叉树，是指一棵空树或者具有下列性质的二叉树：

1. 左子树上**所有结点**的值均小于它的根结点的值；
2. 右子树上**所有结点**的值均大于它的根节点的值；
3. 以此类推：左、右子树也分别为二叉查找树。

中序遍历：升序排列


#### 平衡二叉树





### 图
## 数学

### 等差数列求和公式

$$sum=n*a_{1} + \frac{(n-1)*n}{2}*d$$

### 等比数列求和公式

$$sum=\frac{a_{1}*(1-q^{n})}{1-q}$$

## 缓存

### 最近最少使用缓存（LRUCache）

### 最不经常使用缓存（LFUCache）