package com.pa;

/**
 * @class Switch
 * A class that simulates a switch as a node from a network
 */
public class Switch extends Node {

    /**
     * The constructor of the switch taking the following paramters
     * @param name
     * @param MAC
     * @param location
     */
    public Switch(String name, String MAC, String location) {
        this.name = name;
        this.MAC = MAC;
        this.location = location;
    }

}
