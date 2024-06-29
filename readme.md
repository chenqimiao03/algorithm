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

嵌套类问题的递归解题套路：

1. 定义全局变量 `where`
2. 递归函数 `f(i)`：从 `i` 位置开始出发开始解析，遇到**字符串终止**或**嵌套条件终止**就返回
3. 返回值是 `f(i)` 负责这一段的结果
4. `f(i)` 在返回前更新全局变量 `where`，让上级函数通过 `where` 知道解析到了什么位置，进而继续

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


### 前缀信息技巧

#### 一维差分

问题描述：一开始 `1~N` 范围上的数字都是 `0`。接下来一共有 `m` 个操作。每次操作：`l~r` 范围上依次加上数值 `V`，最终 `1~N` 范围上的每个数字都要正确得到。

过程：
1. 每次操作都在 `L` 位置加上 `V`，在 `R+1` 位置上减去 `V`
2. 所有操作完成后在 `arr` 上生成前缀和
3. `arr` 里就是最终 `1~N` 范围上的每个数字

#### 等差数列差分

问题描述：一开始 `1~N` 范围上的数字都是 `0`。接下来一共有 `m` 个操作。每次操作：`l~r` 范围上依次加上首项 `s`、末项 `e` 和公差 `d` 的数列，最终 `1~N` 范围上的每个数字都要正确得到。

过程：
1. 每次操作调用 `set` 方法
2. 所有操作完成后在 `arr` 上生成两遍前缀和，即调用 `build` 方法
3. `arr` 里就是最终 `1~N` 范围上的每个数字

`set` 方法：

```python
def set(l, r, s, e, d):
    arr[l] += s
    arr[l + 1] += d - s
    arr[r + 1] -= d + e
    arr[r + 2] += e
```

`build` 方法：

```python
def build():
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]
```

#### 二维差分

二维前缀和：目的是预处理出一个结构，以后每次查询二维数组任何范围上的累加和都是`O(1)`的操作

过程：

1. 根据原始状况，生成二维前缀和数组`sum`，其中`sum[i][j]`表示的是左上角`(0,0)`到右下角`(i,j)`这个范围的累加和， $sum[i][j]+=sum[i][j-1]+sum[i-1][j]-sum[i-1][j-1]$

2. 查询左上角`(a,b)`到右下角`(c,d)`这个范围的累加和， $sum[c][d]-sum[c][b-1]-sum[a-1][d]+sum[a-1][b-1]$

3. 实际过程中可以补上第`0`行和第`0`列来减少条件判断


问题描述：一开始二维矩阵 `(0,0)` 到 `(n,m)` 区域上的数字都是 `0`。接下来一共有 `k` 个操作。每次操作：`(a,b)` 到 `(c,d)` 的区域上依次加上数值 `V`，最终二维矩阵 `(0,0)` 到 `(n,m)` 区域上的每个数字都要正确得到。

过程：
1. 每次操作调用 `add` 方法
2. 所有操作完成后在 `arr` 上生成二维前缀和，即调用 `build` 方法
3. 真实数据用一圈 `0` 包裹起来，可以减少条件的判断

`add` 方法：

```python
def add(a, b, c, d, k):
    arr[a][b] += k
    arr[a][d+1] -= k
    arr[c+1][b] -= k
    arr[c+1][d+1] += k
```

`build` 方法：

```python
def build():
    # 用了一圈 0 包裹着真实数据
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j]+=arr[i][j-1]+arr[i-1][j]-arr[i-1][j-1]
```

#### 双指针

#### 二分答案法



## 数据结构

### 链表

实现见：`linkedlist.py`

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

实现见：`heap.py`

### 布隆过滤器/位图

$$m=-\frac{n*ln{p}}{(ln{2})^{2}}$$

$$k=ln{2}*\frac{m}{n}$$

$$p_{1}=(1-e^{-\frac{n*k_{1}}{m_{1}}})^{k_{1}}$$

其中：

m 是 bitarray 的大小，n 是样本数量，p 是预计失误率，k 是哈希函数的个数

实现见：`bitset.py` 和 `bloomfilter.py`

### 树

#### 二叉搜索树

二叉搜索树，也称有序二叉树、排序二叉树，是指一棵空树或者具有下列性质的二叉树：

1. 左子树上**所有结点**的值均小于它的根结点的值；
2. 右子树上**所有结点**的值均大于它的根节点的值；
3. 以此类推：左、右子树也分别为二叉查找树。

中序遍历：升序排列

实现见：`tree.py`

#### 前缀树

每个样本都从头节点开始根据**前缀字符**或者**前缀数字**构建出来的一棵树，如图：

![image.png](./images/trie1.png)

1. 使用场景：根据前缀信息来查询的场景
2. 前缀树的优点：根据前缀信息选择树上的分支，可以节省大量时间
3. 前缀树的缺点：比较浪费空间，和总字符数量、字符的总类有关
4. 定制：`path`, `end` 等信息


#### 平衡二叉树

实现见：`tree.py`


### 图

## 数学

### 等差数列求和公式

$$sum=n*a_{1} + \frac{(n-1)*n}{2}*d$$

### 等比数列求和公式

$$sum=\frac{a_{1}*(1-q^{n})}{1-q}$$

### 最大公约数

辗转相除法，见 `problemset/878. 第 N 个神奇数字.py`

### 同余定理

和差积的余数等于余数的和差积

## 缓存

### 最近最少使用缓存（LRUCache）

### 最不经常使用缓存（LFUCache）

## 对数器

验证算法正确性的一种方法

1. 你想要测的方法 A
2. 实现复杂度不好但是容易实现的方法 B【往往是暴力解】
3. 实现一个随机样本产生器【长度和值都是随机的】
4. 把方法 A 和方法 B 跑相同的输入样本，看看得到的结果是否一样
5. 如果有一个随机样本使得对比结果不一致，打印这个出错样本，并使用这个出错样本对方法 A 和方法 B 进行调试
6. 当很多样本在这两个方法的对比下依然正确，可以确定方法 A 已经正确

### 对数器打表找规律的技巧

1. 可以用最暴力的实现求入参不大清楚下的答案，往往只需要最基本的递归能力
2. 打印入参不大清楚下的答案，然后观察规律
3. 把规律变成代码，就是最优解