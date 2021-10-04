// insertion in binary tree
public class BinarySearchTree {

    public class Node {
        
        public int data;
        public Node left;
        public Node right;

        //constructor
        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }

    }
    // instance variable
    public Node root;

    // constructor for initialise the root to null BYDEFAULT
    public BinarySearchTree() {
        this.root = null;
    }
    
    // insert method to insert the new Date
    public void insert(int newData) {
        this.root = insert(root, newData);
    }

    public Node insert(Node root, int newData) {
        // Base Case: root is null or not
        if (root == null) {
            // Insert the new data, if root is null.
            root = new Node(newData);
            // return the current root to his sub tree
            return root;
        }
       
        else if (root.data >= newData) {
            // if current root data is greater than the new data then now process the left sub-tree
            root.left = insert(root.left, newData);
        } else {
            // if current root data is less than the new data then now process the right sub-tree
            root.right = insert(root.right, newData);
        }
        return root;
    }

    //Traversal
    public void preorder() {
        preorder(root);
    }

    public void preorder(Node root) {
        if (root == null) {
            return;
        }
        System.out.print(root.data + " ");
        preorder(root.left);
        preorder(root.right);

    }
    public static void main(String[] args) {
        // Creating the object of BinarySearchTree class
        BinarySearchTree bst = new BinarySearchTree();
        // call the method insert
        bst.insert(2);
        bst.insert(4);
        bst.insert(1);
        bst.insert(3);
        bst.insert(5);
        bst.preorder();
    }
    
}