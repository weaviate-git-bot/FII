import java.util.*;

/**
 * @Class class that represens a graph data structure using a matrix
 */
public class CustomGraph {
    private int vertex;
    private Map<Intersection, List<Street>> adj;

    /**
     * The construction
     * @param vertex maximum number of vertexes
     */
    public CustomGraph(int vertex) {
        this.vertex = vertex;
        this.adj = new HashMap<Intersection, List<Street>>();
    }

    /**
     * Add a new edge in an undirected graph
     * @param v first vertex
     * @param w second vertex
     */
    public void addEdge(Intersection inter, Street str){
        List<Street> currentStreets =  this.adj.get(inter);
        if(!(currentStreets instanceof ArrayList<Street>)) {
            currentStreets = new ArrayList<Street>();
        }
        currentStreets.add(str);
        this.adj.put(inter, currentStreets);
    }

    /**
     * Prim algorithm for Minimum spanning tree on the graph
     */
    public void MST() {
        //to be added
    }

    /**
     * Getting the adjacency list for each intersection
     * @param node
     * @return the adjacency list
     */
    public List<Street> getAdjacencyList(Intersection node) {
        return this.adj.get(node);
    }

    /**
     * Getting all nodes from the list
     * @return keySey of adjacency list
     */
    public Set<Intersection> getNodes() {
        return new HashSet<Intersection>(this.adj.keySet());
    }

    /**
     * Display the entire graph data structure.
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Intersections are: \n");
        for(Intersection inter : this.adj.keySet()) {
            sb.append("-> ");
            sb.append(inter.getName());
            sb.append(": ");
            for(Street str: this.adj.get(inter)) {
                sb.append(str.getName());
                sb.append(",");
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}