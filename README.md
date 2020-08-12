# data-structure
The learning materials of the data structure, using python development

### Linked list
[Linked list(鏈結串列)](https://github.com/pili2026/data-structure/blob/master/link_list.py)是一種常見的資料結構，其使用**node**(**節點**)來記錄、表示、儲存資料(data)，並利用每個**node**中的**pointer**指向下一個**node**，藉此將多個**node**串連起來，形成**Linked list**，並以<font color="#dd0000">NULL</font>來代表Linked list的終點。
![](https://i.imgur.com/FEucZan.png)

通常在面對一個Linked list時，能夠公開存取(access)的node只有「第一個node」，以<font color="#dd0000">ListNode *first</font>表示，不過因為node中有**pointer**記錄下一個node的記憶體位置，便能夠讀取下一個node的**data**與**pointer**，換句話說，有了node中的**pointer**就可以在Linked list中「移動(**traversal**)」，更進一步，便能進行諸如「新增節點」、「刪除節點」、「印出Linked list」等等的資料處理。

參考網站:
* [Linked List: Intro](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
* [Reverse Linked List](https://algorithm.yuanbin.me/zh-tw/linked_list/reverse_linked_list.html)

### 堆疊(Stack)
[Stack(堆疊)](https://github.com/pili2026/data-structure/blob/master/stack.py)具有「**Last-In-First-Out**」(LIFO)的資料結構(可以想像成一種裝資料的容器)，「最晚進入**Stack**」的資料會「最先被取出」，「最早進入**Stack**」的資料則「最晚被取出」。
**Stack**是一個抽象的概念，只要符合「**Last-In-First-Out**」的資料結構，都可以視為**Stack**。

一般的**Stack**，會有以下幾個處理資料結構的功能：
* **Push(data)**：把資料放進Stack。
    * 把書放進箱子。
* **Pop**：把「最上面」的資料從Stack中移除。
    * 把位於箱子「最上面」的書拿出來。
* **Top**：回傳「最上面」的資料，不影響資料結構本身。
    * 確認目前位於箱子「最上面」的是哪本書。
* **IsEmpty**：確認Stack裡是否有資料，不影響資料結構本身。
    * 確認箱子裡面有沒有書。
* **getSize**：回傳Stack裡的資料個數，不影響資料結構本身。
    * 記錄目前箱子已經裝了多少本書。
    
---
![Stack](https://i.imgur.com/oxPkLic.png)

* 一開始Stack是空的
* 當<font color="#dd0000">Push(6)</font>後，便把6放入Stack。並用一個稱為<font color="#dd0000">top</font>的變數，記錄Stack最上面的資料為何，在此即為6。
* 當<font color="#dd0000">Push(3)、Push(7)</font>後，便把3、7放入Stack。並更新<font color="#dd0000">top</font>，使其記錄7。
* 當<font color="#dd0000">Pop()</font>後，便把Stack中「最上面」的資料(7)給移除，所以Stack中剩下6、3，並更新<font color="#dd0000">top</font>記錄3。
* 當<font color="#dd0000">Push(14)、Push(8)</font>後，便把14、8放入Stack。並更新<font color="#dd0000">top</font>，使其記錄8。
* 在以上的任何階段，只要Stack有資料，使用函式<font color="#dd0000">Top()</font>會回傳變數<font color="#dd0000">top</font>所記錄的資料。
* 在以上的任何階段，使用<font color="#dd0000">IsEmpty()</font>便能判斷Stack裡是否有存放資料。
* 在以上的任何階段，使用<font color="#dd0000">getSize()</font>會回傳Stack中的資料個數。

Stack還有一項重要的特徵：

* 除了最上面的資料可以使用<font color="#dd0000">Top()</font>來讀取，無法得知Stack裡面還有其餘哪些資料。要知道Stack裡的所有資料，只能靠<font color="#dd0000">Pop()</font>，把資料一個一個拿出來檢查。

#### Stack的應用
Stack最主要的功能是「記得先前的資訊」，所以時常用來處理需要「回復到先前的狀態」的問題，也稱為Back-Tracking問題，例如：

* 編輯器(如word、sublime等等)中的undo
* 網頁瀏覽器的「回到前一頁」功能
* 任何遞迴(recursion)形式的演算法，都可以用Stack改寫，例如Depth-First Search(DFS，深度優先搜尋)
* 於記憶體管理(memory management)中的Call Stack。

參考網站:
* [Stack](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)

### 佇列(Queue)
[Queue](https://github.com/pili2026/data-structure/blob/master/queue.py)是具有「**First-In-First-Out**」的資料結構，如同排隊買車票的隊伍即可視為**Queue**，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。

如同普遍認知的排隊隊伍，**Queue**也具有以下特徵：

1. 隊伍有前方(以**front**表示)以及後方(以**back**表示)之分。
1. 若要進入隊伍(**Push**)，一定是從**back**進入。
1. 若要離開隊伍(**Pop**)，一定是從**front**離開。

以下圖為例，由front(隊伍前方)和back(隊伍後方)可以判斷，進入隊伍的順序應該是23、1、3、35。
![](https://i.imgur.com/hUzCJhe.png)

一般的Queue，會有以下幾個處理資料結構的功能：

![](https://i.imgur.com/E9hKzy4.gif)

* **Push(data)**：把資料從Queue的「後面」放進Queue，並更新成新的back。在Queue中新增資料又稱為enqueue。
* **Pop**：把front所指向的資料從Queue中移除，並更新front。從Queue刪除資料又稱為dequeue。
* **getFront**：回傳front所指向的資料。
* **getBack**：回傳back所指向的資料。
* **IsEmpty**：確認Queue裡是否有資料。
* **getSize**：回傳Queue裡的資料個數。
