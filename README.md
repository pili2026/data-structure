# data-structure


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

* 參考網站:
[Queue](http://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)

### 樹(Tree)
[Tree(樹)](https://github.com/pili2026/data-structure/blob/master/tree.py) 是用以描述具有階層結構(hierarchical structure)的問題的首選，階層結構意味著明確的先後次序，例如，若要印出ABC三個字母的所有排列組合(permutation)，直覺反射的圖像會是：
![](https://i.imgur.com/kLq1HnE.png) ![](https://i.imgur.com/alkqtHy.png)
* **視R為樹根(root)，每一個選擇狀態視為node，此即為樹的結構。**

上圖的邏輯為：從起點R開始，先決定第一個字母，再依序決定第二、第三個字母，並且，在每一次選擇字母時，可能有不止一個可供選擇的字母。最後一共走出六條路徑，得到六種排列組合，而且這六種排列方式只能經由一種唯一的選擇方式(唯一的路徑)產生。
若將起點R視為樹根(root)，每一個字母選擇的狀態(例如：A、C、BC、CAB)都視為一個node，這樣的結構便能夠視為一棵樹。

#### 用以描述一棵樹的元素
針對**node / vertex**：

* **degree(分歧度)**：一個node擁有的subtree(子樹)的個數。
    * 下圖，A的degree為3，F的degree為2，N的degree為0。
* **root(樹根)**：樹中最上層的node，也是唯一一個其parent為NULL的node。
    * 下圖，A即為root。
* **leaf**：沒有child/subtree的node稱為leaf node。
    * 下圖，G、H、J、K、L、M、N皆為leaf node。
* **external node**：沒有child的node。因此，leaf node與external node同義。
* **internal node**：至少有一個child的node，稱為internal node。
    * 下圖，A、B、C、D、E、F、I皆為internal node。
![](https://i.imgur.com/IyB6OEM.png)

針對**樹**
* **parent <--> child**：以pointer說明，被指向者(pointed)為child，指向者(point to)為parent。
    * 下圖，A為C的parent，C為A的child；E為K的parent，K為E的child。
* siblings：擁有相同parent的node們，互相稱兄道弟。
    * 下圖，B、C、D共同的parent為A，那麼B、C、D即為彼此的sibling。
* **descendant(子嗣)**：下圖中，站在A，所有能夠以「parent指向child」的方式找到的node，皆稱為A的descendant，因此整棵樹除了A以外皆為A的descendant。
    * 站在F，能夠以「parent指向child」找到的node有L、M，則稱L、M為F的descendant。
* **ancestor(祖先)**：下圖中，站在K，所有能夠以「尋找parent」的方式找到的node，皆稱為K的ancestor，因此，E、B、A皆為K的ancestor。
* **path(路徑)**：由descendant與ancestor關係連結成的edge，例如A-B-E-K、A-C-F-N。
* **level**：定義root的level為1，其餘node的level為其parent的level加一。
* **height of node**：某一node與其最長path上之descendant leaf node之間的edge數。
    * 例如，F的height為1，D的height為2，leaf node的height為0。
* **height of tree**：樹的height即為root的height。
    * 下圖中，樹的height為A的height，等於3。
* **depth**：某一node與root之間的edge數。
    * 例如，F的depth為2，L的depth為3。

可以想像的是，在樹中的**traversal**(尋訪)之時間複雜度(time complexity)會與**height**(樹高)有關。

#### 定義
以下列出兩種互相等價的Tree(樹)的定義：
* Tree(樹)是由一個或多個節點所組成的有限集合，並且滿足：

1. 存在且只有一個稱為root(樹根)的節點；
1. 其餘的節點可以分割成任意正整數個(包含零個)互斥(disjoint)的集合：T1、...、Tn，其中每一個集合也都滿足樹的定義，這些集合又稱為這棵樹的subtree(子樹)。
* Tree(樹)是由一個或多個nodes/vertices以及edge所組成，而且沒有cycle的集合(set)。

參考網站: 
* [Tree:Intro](http://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)
* [Data Structures Tutorial In Python #7 - Tree (General Tree)](https://www.youtube.com/watch?v=4r_XR9fUPhQ&t)

### 二元樹(Binary Tree)
[二元樹(Binary tree)](https://github.com/pili2026/data-structure/blob/master/binary_tree.py)，最廣義的樹(Tree)對於樹上的node之child數目沒有限制，因此，每個node可以有多個child。
![This is a tree](https://i.imgur.com/8ipgHy3.png)

若限制node只能有兩個child，等價於「樹上的每一個node之degree(分歧度)皆為2」，此即稱為**Binary Tree**(二元樹)，並稱兩個child pointer為**left child**和**right child**。

![](https://i.imgur.com/YdPgeiH.png)

#### Full & Complete Binary Tree
有兩類Binary Tree十分常見，分別為**Full Binary Tree**以及**Complete Binary Tree**。

**1. Full Binary Tree**
如下圖所示，一棵**Full Binary Tree**(或稱作Perfect Binary Tree)具有以下性質：

* 所有internal node都有兩個subtree(也就是兩個child pointer)
* 所有leaf node具有相同的level(或相同的height)
![](https://i.imgur.com/Aes05kv.png)

由以上性質能夠推論出：

* 若一棵Full Binary Tree的leaf node之level為n，整棵樹共有$2^n−1$個node。
* 例如，若leaf node的level為4， 整棵樹共有15個node。

並且，每個node與其child有以下關係：

* 第$i$個node的left child之index為 $2i$；
* 第$i$個node的right child之index為 $2i+1$；
* 除了root之parent為NULL之外，第i個node的parent之index為 [$i/2$] 。

**2. Complete Binary Tree**
若一棵樹的node按照Full Binary Tree的次序排列(由上至下，由左至右)，則稱此樹為**Complete Binary Tree**。

下圖的樹共有10個node，且這十個node正好填滿Full Binary Tree的前十個位置，則此樹為Complete Binary Tree。
![](https://i.imgur.com/Ve0PCDE.png)

下圖的樹共有11個node，但是第11個node(K)應該要是第5個node(E)的child，因此，此樹**並非**Complete Binary Tree。
![](https://i.imgur.com/kuNQzRp.png)


#### Binary Tree的應用
* Binary Search Tree(BST)：在某些資料經常要增加、刪除的應用中，BST常用來做搜尋，例如許多程式語言的Library中的<font color="#dd0000">map</font>和<font color="#dd0000">set</font>。
* Binary Space Partition：應用於幾乎所有的3D電玩遊戲以決定哪些物件需要rendered。
* Binary Tries：應用於大多數high-bandwidth router(高頻寬路由器)以儲存router-tables。
* Heaps：用以實現高效率的priority queues(優先權佇列)，許多作業系統用來安排工作程序。

#### 二元樹走訪(Binary Tree: Traversal)
Traversal(尋訪)有「站在A地，往所有與A地相連的地方移動」的意思：

* 以Graph(圖)的語言來說，站在vertex(A)上，有一條edge連結vertex(A)與vertex(B)，若能夠由A往B移動，此即可視為traversal；
* 在以pointer實現之Linked list和Tree中，站在node(A)上，並且node(A)具有指向node(B)之pointer，便能夠由A往B移動，此即可視為traversal。

移動到特定的node之後，通常伴隨著其他行為，例如print out(顯示資料)、assign(賦值)、刪除資料等等，這些操作又稱作**Visiting**。

Binary Tree的Node具有兩個指向child的pointer，traversal以「當前所在的node」為參考點，所能夠進行的行為有三種：

* **V**：Visiting，對當前所在的node進行print、assign或其他操作。
* **L**：移動到left child。
* **R**：移動到right child。

![](https://i.imgur.com/g4Ttkg8.png)
**CurrentNode位在A，leftchild與rightchild分別為B與C。**

以上圖為例，假設現在CurrentNode位在A，leftchild與rightchild分別為B與C，並加上一項限制：「L一定在R之前」，便能產生三種相對關係：
![](https://i.imgur.com/N9Kp5Ko.png)
<center>
依序為： (a)pre-order：VLR、(b)in-order：LVR、(c)post-order：LRV
</center>

#### 深度優先搜尋(Depth-First-Search，DFS)
一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。

深度優先搜尋法屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，通常以遞迴的方式呈現。

* [pre-order(VLR)](https://github.com/pili2026/data-structure/blob/master/dfs/pre_order_traversal.py)：當CurrentNode移動到A時，會先對A進行Visiting，接著前往left child進行Visiting，再前往right child進行Visiting。(若child指向NULL則忽略。)

* [in-order(LVR)](https://github.com/pili2026/data-structure/blob/master/dfs/in_order_traversal.py)：當CurrentNode移動到A時，會先對A的left child(B)進行Visiting，接著回到A進行Visiting，再前往right child( C )進行Visiting。(若child指向NULL則忽略。)

* [post-order(LRV)](https://github.com/pili2026/data-structure/blob/master/dfs/post_order_traversal.py)：當CurrentNode移動到A時，會先對A的left child(B)進行Visiting，再前往right child( C )進行Visiting，接著回到A進行Visiting。(若child指向NULL則忽略。)

現有一棵樹如圖一(a)，欲進行**post-order traversal**，並將Visiting用作print(顯示資料)，流程如下：
![](https://i.imgur.com/JbowrN3.png)
<center>
圖一(a)。
</center>


一開始，CurrentNode進到A(root)，按照post-order的順序規則(LRV)，先檢查left child：B是否為NULL，若不是，則先將CurrentNode移動到B(L)：
![](https://i.imgur.com/R404fXn.png)
<center>
圖一(b)：scope內：A(V)、B(L)、C( R )。
</center>


當CurrentNode移動到B，再一次執行post-order的順序規則(LRV)，檢查left child：D是否為NULL，若不是，則將CurrentNode移動到D(L)：
![](https://i.imgur.com/FOsHBap.png)
<center>
圖一(c)：scope內：B(V)、D(L)、E(R)。
</center>
當CurrentNode移動到D，再一次執行post-order的順序規則(LRV)，檢查出D的left child與right child皆為NULL，表示「LRV」的「L」與「R」都已經執行完畢，便「回到D」做Visiting，在此即印出D(print)。

接著，由於「以D為CurrentNode」形成的scope內之node已經全數Visiting完畢，便可回到「以D之parent作為CurrentNode之scope」，於是將CurrentNode移回B。

回到B的動作發生，即表示：以D為CurrentNode之迴圈或函式已經結
束。
![](https://i.imgur.com/7HHrzZZ.png)
<center>
圖一(d)：scope內：D(V)。
</center>

D已經進行過Visiting，便標上數字「1」，表示D為post-order traversal的第一站。
接著，在「以B為CurrentNode」的scope中，根據post-order規則，繼續往E(R)移動。
![](https://i.imgur.com/w2dhDJk.png)
<center>
圖一(e)：scope內：B(V)、D(L)、E(R)。
</center>
進入E後，因為E為leaf node，因此過程如圖一(d)，不會進入NULL。
在D(L)與E( R )都Visiting過後，便回到B(V)進行Visiting，並標上數字。如此便完成「以B為CurrentNode之scope」內的所有node之Visiting。

接著回到「以A為CurrentNode」的scope。
![](https://i.imgur.com/NgCflB7.png) 
<center>
圖一(f)：scope內：B(V)、D(L)、E( R )。
</center>

回到「以A為CurrentNode」的scope後，按照post-order的規則，接著往C(R )移動。

![](https://i.imgur.com/6RrtTOO.png)
<center>
圖一(g)：scope內：A(V)、B(L)、C(R)。
</center>

同樣地步驟，再從C移動至F(L)，並發現F為leaf node，於是對F進行Visiting，並標上數字。

![](https://i.imgur.com/nOoxlkV.png)
<center>
圖一(h)：scope內：C(V)、F(L)。
</center>

列出F後，發現C的right child指向NULL，於是略過right child(R)，回到C(V)，並對C進行Visiting，標上數字。

![](https://i.imgur.com/UUAIsoh.png)![](https://i.imgur.com/Jq8671Z.png)

圖一(i)-(j)：scope內：C(V)、F(L)。
最後回到「以A為CurrentNode」的scope，對A(V)進行Visiting，便完成了此次post-order traversal，並依序印出`D E B F C A`。

![](https://i.imgur.com/Aqfw3hM.png)![](https://i.imgur.com/l0xcWuP.png)
<center>圖一(k)-(l)：scope內：A(V)、B(L)、C(R)。</center>

以上說明了post-order traversal之過程，另外兩種**pre-order**與**in-order**在概念上皆相同，只要把握順序規則即可。

其中，pre-order、in-order、post-order traversal的邏輯就只是「V」、「L」、「R」誰先誰後的差別，通常以較直覺的遞迴(recursion)形式完成，不過，換成迭代(iteration)配合<font color="#dd0000">Stack(堆疊)</font>在概念上完全相同，實作上即是考慮「V」、「L」、「R」誰先push(推)進stack。

![](https://i.imgur.com/tKOCAUT.png)


#### 廣度優先搜尋(Breadth-first Search，BFS)
[Level-order](https://github.com/pili2026/data-structure/blob/master/bfs/level_order_traversal.py)是照著「level由小到大」的順序，由上而下，並在同一個level「由左至右」依序Visiting每個node。

* 以下圖為例，當CurrentNode站在A時，先對A作Visiting，接著檢查是否有left child與right child，若不為NULL，則「依序」將child pointer 推(push)進queue中，又根據<font color="#dd0000">queue「先進先出」(first-in-first-out)的特性</font>，先將B(left child)推入queue，再推入C(right child)，便能確保在下一層level時，是由左至右，先Visiting到B，才Visiting到C。

![](https://i.imgur.com/ZkD6SR7.png)


參考網站:
* [Binary Tree:Intro](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
* [Data Structures Tutorial In Python #8 - Binary Tree](https://www.youtube.com/watch?v=lFq5mYUWEBk)
* [Binary Trees in Python: Introduction and Traversal Algorithms](https://www.youtube.com/watch?v=6oL-0TdVy28&t=887s)
* [以Python實作演算法 – Algorithms Implements using Python](https://super9.space/archives/1562#%E6%B7%B1%E5%BA%A6%E5%84%AA%E5%85%88%E6%90%9C%E5%B0%8B-depth-first-search-dfs)
* [Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)