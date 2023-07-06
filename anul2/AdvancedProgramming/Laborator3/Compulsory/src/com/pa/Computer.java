package com.pa;

/**
 * @Class Computer
 * A class that represents a computer extending Node abstract class, implementing Identifiable and Storage interfaces
 */
public class Computer extends Node implements IIdentifiable, IStorage{
    private String address;
    private int storageCapacity;

    /**
     * Constructor of the class
     * @param name
     * @param MAC
     * @param location
     * @param address
     * @param storageCapacity
     */
    public Computer(String name, String MAC, String location, String address, int storageCapacity) {
        this.name = name;
        this.MAC = MAC;
        this.location = location;
        this.address = address;
        this.storageCapacity = storageCapacity;
    }

    /**
     * Getting the address of this computer
     * @return address
     */
    @Override
    public String getAddress() {
        return this.address;
    }

    /**
     * Setting the address
     * @param address
     */
    public void setAddress(String address) {
        this.address = address;
    }

    /**
     * Getting the storage capacity of the computer
     * @return the storage capacity
     */
    @Override
    public int getStorageCapacity() {
        return this.storageCapacity;
    }

    /**
     * Setting the storage capacity
     * @param capacity setting the storage capacity
     */
    public void  setStorageCapacity(int capacity) {
        this.storageCapacity = capacity;
    }

    /**
     * Adding a custom format for the toString class containing both the address and storageCapacity
     * @return
     */
    @Override
    public String toString() {
        return name+'(' +
                "address='" + address + '\'' +
                ", storageCapacity=" + storageCapacity +
                ", MAC='" + MAC + '\'' +
                ", location='" + location + '\'' +
                ')';
    }
}
