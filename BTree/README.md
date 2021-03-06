## 二叉树

### 2021-12-5

[226. 翻转二叉树 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/invert-binary-tree/)

1. 理解递归代码
2. 思考这个代码的时间和空间复杂度（在题解里面标明）
3. 考虑非递归的实现方式

参考代码

```c++
class Solution {
public:
  TreeNode* invertTree(TreeNode* root) {
    if(root == nullptr)
      return nullptr;
    auto left = invertTree(root->left);
    auto right = invertTree(root->right);
    TreeNode *node = root->left;
    root->left = root->right;
    root->right = node;
    return root;
  }
};
```

非递归形式的关键代码，考虑用队列进行层序遍历，从上到下对于每一个节点交换左右节点

```c++
while (!queue.empty()) {
	TreeNode *node = queue.front();
  queue.pop();
  auto tmp = node->left;
  node->left = node->right;
  node->right = tmp;
  if (node->left != nullptr)
    queue.push(node->left);
 	if (node->right != nullptr)
    queue.push(node->right);
}
```



### 2021-12-6

[94. 二叉树的中序遍历 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

要求：

1. 理解栈的使用，做到能自己写出非递归版本，最好自己使用一棵简单的二叉树画出来模拟一下
2. 在理解了非递归版本之后，尝试写出 [226. 翻转二叉树 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/invert-binary-tree/) 的非递归实现

参考代码

```c++
vector<int> inorderTraversal(TreeNode* root) {
  std::vector<int> ans;
  std::stack<TreeNode *> stack;
  TreeNode *p = root;
  while (p || !stack.empty()) {
    while (p) {
      stack.push(p);
      p = p->left;
    }
    TreeNode *node = stack.top();
    stack.pop();
    ans.push_back(node->val);
    if (node->right)
      p = node->right;
  }
  return ans;
}
```

### 2021-12-8

[144. 二叉树的前序遍历 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

要求：

1. 同样理解前序遍历中栈的使用，做到自己能写出非递归版本，手动模拟能够加深理解

参考代码

```c++
vector<int> preorderTraversal(TreeNode* root) {
  std::vector<int> result;
  if(root == nullptr)
    return result;
  std::stack<TreeNode *> sp;
  while(!(sp.empty()) || root) {
    while(root) {
      result.push_back(root->val);
      sp.push(root);
      root = root->left;
    }
    TreeNode *node = sp.top();
    sp.pop();
    root = node->right;
  }
  return result;
}
```

### 2021-12-9

[102. 二叉树的层序遍历 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

任务要求：

- 理解广度优先搜索（BFS）
- 用 BFS 或者说是层序遍历的方式完成 2021.12.5 的题目 

BFS 代码框架

```c++
std::vector<int> bfs(TreeNode *root) {
  std::vector<int> res;
  if (root == nullptr)
    return res;
  std::queue<TreeNode *> queue;
  queue.push(root);
  while (!(queue.empty())) {
    TreeNode *node = queue.front();
    queue.pop();
    res.push_back(node->val);
    if (node->left)
      queue.push(node->left);
    if (node->right)
      queue.push(node->right);
  }
}
```

### 2021-12-10

[107. 二叉树的层序遍历 II - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

提示：

- 虽然题目要求是自底向上一层一层遍历，但是能不能转换为常规自顶向下的遍历方式

想通这种转换这题就没有什么问题了，尽量先自己想想，然后再看参考代码

> 难度：中等

关键部分代码参考

```c++
while(!(queue.empty())) {
  std::vector<int> tmp;
  int n = 0;  /* 记录下一层次的长度 */
  for (int i = 0; i < len; ++i) {
    TreeNode *node = queue.front();
    queue.pop();
    tmp.push_back(node->val);

    if (node->left) {
      queue.push(node->left);
      ++n;
    }
    if (node->right) {
      queue.push(node->right);
      ++n;
    }
  }
  len = n;
  res.push_back(tmp);
}
```

### 2021-12-11

[103. 二叉树的锯齿形层序遍历 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

层序遍历应用

> 不给参考代码啦

### 2021-12-11

[230. 二叉搜索树中第K小的元素 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)

- 中序遍历
- 非递归 + 递归实现
- 最后可以看一下官方题解里面题解二的方法

### 2021-12-13

[129. 求根节点到叶节点数字之和 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

回顾之前深度优先搜索、广度优先搜索的使用，最好做到：

1. 使用非递归 DFS 实现
2. 使用递归 DFS 实现
3. 使用 BFS 实现

提示：可以考虑使用两个队列或者两个栈，每个队列或者栈记录遍历到当前元素的时候组成的数字，每次从两个队列或者栈中都弹出一个元素，然后当发现某一个元素是叶节点时就将该数字累加到最后结果

### 2021-12-15

[113. 路径总和 II - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/path-sum-ii/)

要求：

1. 使用递归的 DFS 实现
2. 使用 BFS 实现
3. 使用非递归的 DFS 实现**（重点）**

> BFS 和非递归的 DFS 思路同昨天的题目类似，看一下昨天是怎么实现的，然后仿照着做出来
