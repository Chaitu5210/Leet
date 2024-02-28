class Solution {
    bool validateBst(TreeNode* root, long min, long max) {
        if (root == NULL)
            return true;

        if (root->val <= min || root->val >= max)
            return false;

        return validateBst(root->left, min, root->val) &&
               validateBst(root->right, root->val, max);
    }

public:
    bool isValidBST(TreeNode* root) {
        if (root == NULL)
            return true;
        return validateBst(root, LONG_MIN, LONG_MAX);
    }
};