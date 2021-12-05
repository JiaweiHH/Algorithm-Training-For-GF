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

