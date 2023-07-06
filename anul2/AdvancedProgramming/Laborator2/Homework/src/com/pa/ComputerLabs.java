package com.pa;

public class ComputerLabs extends Room{
    private String computerOS;

    /**
     * The constructor for the class
     * @param name the name of the room
     * @param type the type of the room
     * @param capacity the capacity of the room
     */
    public ComputerLabs(String name, int capacity, String computerOS) {
        this.name = name;
        this.type = "Laboratory";
        this.capacity = capacity;
        this.computerOS = computerOS;
    }

    /**
     * Getting the computer os
     * @return a string representing computer os
     */
    public String getComputerOS() {
        return computerOS;
    }

    /**
     * Set the computer os for this lab class
     * @param computerOS a string representing computer os
     */
    public void setComputerOS(String computerOS) {
        this.computerOS = computerOS;
    }

    /**
     * Getting the name
     * @return name
     */
    @Override
    public String getName() {
        return name;
    }

    /**
     * Setting the name
     * @param name
     */
    @Override
    public void setName(String name) {
        this.name = name;
    }


    /**
     * Getting the capacity
     * @return capacity
     */
    @Override
    public int getCapacity() {
        return capacity;
    }

    /**
     * Setting the capacity. It must be greater then 0.
     * @param capacity
     */
    @Override
    public void setCapacity(int capacity) {
        if(capacity < 0) {
            throw new IllegalArgumentException("The capacity of the room must be greater then 0");
        }
        this.capacity = capacity;
    }

    /**
     * Checking if two classes have equal parameters
     * @param o an object
     * @return true if the objects have the same name and are from same class type, false otherwise
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Room room = (Room) o;

        return this.getName().equals(room.getName());
    }

    /**
     * Getting the class attributes using a custom format
     * @return a custom format string for the class
     */
    @Override
    public String toString() {
        return name+"(" +
                "cap=" + capacity +
                ", type=" + this.type +
                ')';
    }
}
