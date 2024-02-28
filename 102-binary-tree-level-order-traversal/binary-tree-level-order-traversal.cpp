class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) {
            return vector<vector<int>>();
        }

        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;

            for (int i = 0; i < levelSize; ++i) {
                TreeNode* currentNode = q.front();
                q.pop();

                currentLevel.push_back(currentNode->val);

                if (currentNode->left != NULL) {
                    q.push(currentNode->left);
                }

                if (currentNode->right != NULL) {
                    q.push(currentNode->right);
                }
            }

            result.push_back(currentLevel);
        }

        return result;
    }
};
