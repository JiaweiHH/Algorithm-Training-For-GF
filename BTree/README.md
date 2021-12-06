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

