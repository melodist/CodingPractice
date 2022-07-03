/**
 * https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/
 * Using recursion
 * Make left and right tree for each node, and combine them.
/**
//1. Solution
/**
 *
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n){
        return genTrees(1,n);
    }
    public List<TreeNode> genTrees(int start, int end){
        List<TreeNode> list = new ArrayList<TreeNode>();

        if( start > end ){
            list.add(null);
            return list; 
        } 
        if( start == end ){
            list.add( new TreeNode(start));
            return list; 
        } 

        List<TreeNode> left,right;

        for(int i = start ; i<= end; i++){
            left = genTrees(start, i-1);
            right = genTrees(i+1, end);
            for(TreeNode lnode : left ){
                for(TreeNode rnode : right ){
                    TreeNode root = new TreeNode(i);
                    root.left = lnode; 
                    root.right = rnode;
                    list.add(root);
                }
            }
        }
        return list; 
    }
}
