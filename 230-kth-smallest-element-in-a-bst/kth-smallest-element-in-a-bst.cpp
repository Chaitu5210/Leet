/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        if(root==NULL){
            return NULL;
        }
        vector<int> temp_arr;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* first_node=q.front();
            temp_arr.push_back(first_node->val);
            q.pop();
            if(first_node->left!=NULL){
                q.push(first_node->left);
            }
            if(first_node->right!=NULL){
                q.push(first_node->right);
            }
        }
        sort(temp_arr.begin(), temp_arr.end());
        return temp_arr[k-1];
    }
};