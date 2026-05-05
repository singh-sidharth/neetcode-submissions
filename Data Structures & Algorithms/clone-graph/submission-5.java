

/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/


class Solution {

    Node getNewNode(int val){
        return new Node(val, new ArrayList<Node>());
    }
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }

        // also acts as seen node
        Map<Node, Node> visited = new HashMap<>();

        Deque<Node> st = new ArrayDeque<>();
        st.push(node);
        visited.put(node, getNewNode(node.val));

        while (!st.isEmpty()) {
            Node curr = st.pop();
            Node currClone = visited.get(curr);

            for (Node nei : curr.neighbors) {
                if (!visited.containsKey(nei)) {
                    visited.put(nei, getNewNode(nei.val));
                    st.push(nei);
                }
                // add neighbors if already cloned before
                // don't re-clone
                currClone.neighbors.add(visited.get(nei));
            }
        }
        return visited.get(node);
    }
}