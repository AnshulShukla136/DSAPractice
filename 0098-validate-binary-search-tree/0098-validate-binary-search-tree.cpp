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
    bool solve(TreeNode* root, long long l, long long r){
        if(!root) return true;
         if(root -> val <= l || root -> val >= r) {
            return false;
        }
        bool leftTree = solve(root -> left, l, root -> val);
        bool rightTree = solve(root -> right, root -> val, r); 
        return leftTree && rightTree;
    }
    bool isValidBST(TreeNode* root) {
        if(!root) return true;
        bool l = solve(root -> left, LLONG_MIN, root -> val);
        bool r = solve(root -> right, root -> val, LLONG_MAX);
        return l && r;
    }
};