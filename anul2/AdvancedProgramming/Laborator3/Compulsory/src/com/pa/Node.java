package com.pa;

import java.util.HashMap;
import java.util.Map;

/**
 * @class Node
 * An abstract class that simulates  a node in the network
 */
public abstract class Node implements Comparable<Node> {
    protected String name;
    protected String MAC;
    protected String location;
    protected int positionInNetwork;
    private Map<Node, Integer> cost = new HashMap<>();


    /**
     * Get the position of the node inside a network
     * @return positionInNetwork
     */
    public int getPositionInNetwork() {
        return positionInNetwork;
    }

    /**
     * Set the node position in netowkr
     * @param positionInNetwork
     */
    public void setPositionInNetwork(int positionInNetwork) {
        this.positionInNetwork = positionInNetwork;
    }

    /**
     * Get the cost map from current node to other nodes in the network
     * @return cost
     */
    public Map<Node, Integer> getCost() {
        return cost;
    }


    /**
     * Getting the name of the node
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * Setting the name of the node
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getting the  MAC address of the node
     * @return MAC address
     */
    public String getMAC() {
        return MAC;
    }

    /**
     * Setting the MAC address of the node
     * @param MAC the mac address
     */
    public void setMAC(String MAC) {
        this.MAC = MAC;
    }

    /**
     * Get all the time costs from current node to all other nodes with which we have a link
     * @return a map between node and integer
     */
    public Map<Node, Integer> getTimeCosts() {
        return this.cost;
    }

    /**
     * Getting the location of the node
     * @return location
     */
    public String getLocation() {
        return location;
    }

    /**
     * Setting the lcoation of the node
     * @param location
     */
    public void setLocation(String location) {
        this.location = location;
    }

    /**
     * Set cost between two nodes in the network
     * @param node the value of the node
     * @param value the actual cost
     */
    public void setCost(Node node, int value) {
        cost.put(node, value);
    }


    /**
     * Returning the elements  of the class in a custom string format
     * @return a formatted string
     */
    @Override
    public String toString() {
        return name+"(" +
                "MAC='" + MAC + '\'' +
                ", location='" + location + '\'' +
                ')';
    }

    /**
     * Comparing two nodes by name
     * @param other the node that we want to compare with
     * @return 0 if they have the same name, 1 if the current node is bigger, -1 if o is bigger
     * Throws a NullPointerException if either name is  null
     */
    @Override
    public int compareTo(Node other) {
        if(this.name == null || other.name == null) {
            throw new NullPointerException();
        }
        return  this.name.compareTo(other.name);
    }
}
