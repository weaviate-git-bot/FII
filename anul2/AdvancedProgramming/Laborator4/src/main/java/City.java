import java.util.*;
import org.jgrapht.Graph;
import org.jgrapht.alg.spanning.PrimMinimumSpanningTree;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleWeightedGraph;


public class City {
    private List<Street> streets;
    private Set<Intersection> intersections;
    private CustomGraph city;

    /**
     * The constructor of the City class
     * @param streets
     * @param intersections
     */
    public City(List<Street> streets, Set<Intersection> intersections) {
        this.streets = new LinkedList<Street>(streets);
        this.intersections = new HashSet<Intersection>(intersections);
        this.city = new CustomGraph(this.intersections.size());
        this.createCityNetwork();
    }

    /**
     * Creating the graph from the streets and intersections
     */
    private void createCityNetwork(){
        for(Street street: this.streets) {
            this.city.addEdge(street.getLeftIntersection(), street);
            this.city.addEdge(street.getRightIntersection(), street);
        }
        System.out.println(city);
    }

    /**
     *
     * @param minStreetLength the minimum length of a street
     * @throws IllegalArgumentException if the minStreetLength is <0
     */
    public void displayStreetsWithAtLeast3IntersectionsBiggerThan(int minStreetLength) {
        if(minStreetLength <= 0) {
            throw new IllegalArgumentException("The length of a street must be greater then 0");
        }

        this.city.getNodes().stream().map(node -> {
            List<Street> streetsForNode = this.city.getAdjacencyList(node);
            // here the degree should be 3 + 1 (the current street) -> 4
            if(streetsForNode.size() > 3) {
                return streetsForNode;
            }
            return null;
        }).forEach(streets -> {
            if(streets != null) {
                streets.stream().forEach(edge -> {
                    if(edge.getLength() >= minStreetLength) {
                        System.out.println(edge);
                    }
                });
            }
        });
    }

    /**
     * Solving how to install the data cables (on which streets) such as the total cost is minimum.
     */
    public void minimumDataCableLength() {
        Graph<Intersection, DefaultWeightedEdge> graph = new SimpleWeightedGraph<>(DefaultWeightedEdge.class);

        for (Intersection node : this.intersections) {
            graph.addVertex(node);
        }

        for (Street street : this.streets) {
            graph.addEdge(street.getLeftIntersection(), street.getRightIntersection());
            graph.setEdgeWeight(street.getLeftIntersection(), street.getRightIntersection(), street.getLength());
        }

        PrimMinimumSpanningTree<Intersection, DefaultWeightedEdge> tree = new PrimMinimumSpanningTree<>(graph);

        System.out.println("The minimum spanning tree is: ");
        for (var edge : tree.getSpanningTree().getEdges()) {
            System.out.println("(" + graph.getEdgeSource(edge).getName() + " : " + graph.getEdgeTarget(edge).getName() + ")");
        }
    }
    /**
     * Getting the streets from the city
     * @return streets
     */
    public List<Street> getStreets() {
        return streets;
    }

    /**
     * Setting the streets within the city
     * @param streets
     */
    public void setStreets(List<Street> streets) {
        this.streets = streets;
    }

    /**
     * Getting the intersections from the city
     * @return intersections
     */
    public Set<Intersection> getIntersections() {
        return intersections;
    }

    /**
     * Setting the intersection within the city
     * @param intersections
     */
    public void setIntersections(Set<Intersection> intersections) {
        this.intersections = intersections;
    }
}
