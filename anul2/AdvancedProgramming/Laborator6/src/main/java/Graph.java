import java.io.Serializable;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * @class Graph
 * A class that models a graph
 */
public class Graph {
    private Map<Integer, List<Integer>> adjacency = new HashMap<>();
    private int nodes;

    /**
     * Added a constructor to be Serializable
     */
    public Graph() {

    }

    /**
     * The constructor that require the amount of nodes for initialization
     * @param nodes
     */
    public Graph(int nodes) {
        this.nodes = nodes;
    }

    /**
     * Checking if a pair already exissts
     * @param left the node that we are sure it's added
     * @param right the node we want to check against
     * @return true if the node exists, false otherwise
     */
    public boolean pairExists(int left, int right) {
        return this.adjacency.get(left).stream().filter(i -> i == right).collect(Collectors.toList()).size() == 1;
    }

    /**
     * Reinitialize the graph
     */
    public void reinitializeGraph() {
        this.adjacency.clear();
    }

    /**
     * Create a new  node in the graph
     * @param node
     */
    public void createNode(int node) {
        this.adjacency.put(node, new LinkedList<>());
    }

    /**
     * Add a new pair
     * @param left
     * @param right
     */
    public void createPair(int left, int right) {
        this.adjacency.get(left).add(right);
        this.adjacency.get(right).add(left);
    }

    /**
     * Get the Adjacency list of the graph
     * @return adjacency
     */
    public Map<Integer, List<Integer>> getAdjacency() {
        return adjacency;
    }

    /**
     * Set the adjacency list of the graph
     * @param adjacency
     */
    public void setAdjacency(Map<Integer, List<Integer>> adjacency) {
        this.adjacency = adjacency;
    }

    /**
     * Get the node counter
     * @return nodes
     */
    public int getNodes() {
        return nodes;
    }

    /**
     * Set the node counter
     * @param nodes
     */
    public void setNodes(int nodes) {
        this.nodes = nodes;
    }
}
