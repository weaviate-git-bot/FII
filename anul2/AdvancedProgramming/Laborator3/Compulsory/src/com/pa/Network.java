package com.pa;

import java.util.*;

/**
 * @class Network
 * A class that simulates a computer network containing multiple nodes
 */
public class Network {
    private List<Node> nodes;

    /**
     * Constructor that initializes the nodes
     */
    Network() {
        this.nodes = new ArrayList<>();
    }

    /**
     * Getting the nodes from the network
     * @return a list of nodes
     */
    public List<Node> getNodes() {
        return nodes;
    }

    /**
     * Getting a  specific node from the network
     * @param idx
     * @return the node at located at the given index
     */
    public Node getNode(int idx) {
        if(idx < 0 || idx > this.nodes.size()) {
            throw new IllegalArgumentException("The given index is outside the range");
        }
        return this.nodes.get(idx);
    }

    /**
     * Get the network map for the current network
     * @return a weighted graph representing the network map of the current network
     */
    public Graph getNetworkMap() {
        Graph currentMap = new Graph(this.getNetworkSize() + 1);
        for (Node node: this.nodes) {
            for(Map.Entry<Node, Integer> entry : node.getCost().entrySet()) {
                currentMap.addEdge(node.getPositionInNetwork(), entry.getKey().getPositionInNetwork(), entry.getValue());
            }
        }

        return currentMap;
    }

    /**
     * Get the node with the specified network possition
     * @param networkPosition the possition of the node in the network
     * @return Node with the specified position
     * @throws IllegalArgumentException if the networkPosition couldn't be found
     */
    public Node getNodeWithPosition(int networkPosition) {
        // check the best case scenario
        if(this.nodes.get(networkPosition).getPositionInNetwork() == networkPosition) {
            return this.nodes.get(networkPosition);
        }

        // if we didn't find it at first it means the array was sorted
        for(int idx = 0; idx < this.getNetworkSize(); ++ idx) {
            if(this.nodes.get(idx).getPositionInNetwork() == networkPosition)
                return this.nodes.get(idx);
        }

        // invalid position
        throw new IllegalArgumentException("Node with invalid network possition");
    }

    /**
     * Getting the size of the network
     * @return nodes.size();
     */
    public int getNetworkSize() {
        return this.nodes.size()-1;
    }

    /**
     * Setting the nodes list
     * @param nodes a list of all network nodes
     */
    public void setNodes(List<Node> nodes) {
        this.nodes = nodes;
    }

    /**
     * Add a new node to the end of the array
     * @param node
     */
    public void addNode(Node node) {
        node.setPositionInNetwork(this.nodes.size());
        this.nodes.add(node);
    }

    /**
     * Displays the nodes that are identifiable in the network sorted by address
     * @return List<Node> a list of nodes that are identifiable, sorted by address
     */
    public List<Node> getIdentifiableNodes() {
        List<Node> identifiableNodes = new ArrayList<Node>();

        for(int idx = 0; idx < this.nodes.size(); ++idx) {
            Node n = this.nodes.get(idx);
            if (n instanceof IIdentifiable) {
                identifiableNodes.add(n);
            }
        }

        Collections.sort(identifiableNodes, this::compareIdentifiable);

        return identifiableNodes;
    }

    /**
     * Compare two Identifiable nodes by address
     * @param other a node paramater that is also identifiable
     * @return 0 if they have the same address, 1 if the current node address is bigger, -1 if o address is bigger
     * @throws NullPointerException if either name is  null
     * @throws IllegalArgumentException if either name is not instanceof IIdentifiable
     */
    public int compareIdentifiable(Node n1, Node n2) {
        if(!(n1 instanceof IIdentifiable) || !(n2 instanceof IIdentifiable)) {
            throw new IllegalArgumentException("You can only compare IIdentifiable nodes!");
        }

        if(((IIdentifiable) n1).getAddress() == null || ((IIdentifiable) n1).getAddress() == null) {
            throw new NullPointerException();
        }

        return ((IIdentifiable) n1).getAddress().compareTo(((IIdentifiable) n2).getAddress());
    }

    /**
     * Get the class information as a string value
     * @return a formatted string containing all node sorted by name
     */
    @Override
    public String toString() {
        this.nodes.sort(Node::compareTo);
        return "Network{" +
                "nodes=" + this.nodes.toString() +
                '}';
    }
}
