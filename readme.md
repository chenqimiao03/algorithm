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

### 链表类题目注意点

1. 如果笔试中空间不要求，直接使用容器来解决链表问题
2. 如果笔试中空间要求严格、或者在面试中面试官强调空间优化，需要使用额外空间复杂度O(1)的方法
3. 最常用的技巧：**快慢指针**
4. 链表类题目往往都是很简单的算法问题，核心考察点也并不是算法设计，而是 coding 能力