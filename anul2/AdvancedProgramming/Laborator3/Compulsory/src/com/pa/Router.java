package com.pa;

/**
 * @class Router
 * A class that represents a computer extending Node abstract class, implementing  Identifiable interface
 */
public class Router extends Node implements IIdentifiable{
    private String address;

    /**
     * A constructor for the node network
     * @param name
     * @param MAC
     * @param location
     * @param address
     */
    public Router(String name, String MAC, String location, String address) {
        this.name = name;
        this.MAC = MAC;
        this.location = location;
        this.address = address;
    }

    /**
     * Getting the address of the router
     * @return address
     */
    @Override
    public String getAddress() {
        return this.address;
    }

    /**
     * Setting the address of the router
     * @param address
     */
    public void setAddress(String address) {
        this.address = address;
    }

    /**
     * Custom formatting the class as a string containing  all parameters of the class
     * @return a custom formatted string
     */
    @Override
    public String toString() {
        return name+" (" +
                "MAC='" + MAC + '\'' +
                ", location='" + location + '\'' +
                ", address='" + address + '\'' +
                ')';
    }
}
