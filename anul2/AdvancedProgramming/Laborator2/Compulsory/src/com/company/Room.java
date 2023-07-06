package com.company;

/**
 * @Class Room representing a room in which an event can be held.
 */
public class Room {
    private String name;
    private RoomType type;
    private int capacity;

    /**
     * The constructor for the class
     * @param name the name of the room
     * @param type the type of the room
     * @param capacity the capacity of the room
     */
    public Room(String name, RoomType type, int capacity) {
        this.name = name;
        this.type = type;
        this.capacity = capacity;
    }

    /**
     * Getting the name
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * Setting the name
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getting the type
     * @return type
     */
    public RoomType getType() {
        return type;
    }

    /**
     * Setting the type
     * @param type
     */
    public void setType(RoomType type) {
        this.type = type;
    }

    /**
     * Getting the capacity
     * @return capacity
     */
    public int getCapacity() {
        return capacity;
    }

    /**
     * Setting the capacity. It must be greater then 0.
     * @param capacity
     */
    public void setCapacity(int capacity) {
        if(capacity < 0) {
            throw new IllegalArgumentException("The capacity of the room must be greater then 0");
        }
        this.capacity = capacity;
    }

    /**
     * Getting the type of the room as a string
     * @return a custom string based on type of the room
     */
    public String getStringFromType() {
        switch (this.type) {
            case LABORATORY: return "lab";
            case LECTURE_HALL: return "lecture hall";
            default: return "unknown";
        }
    }

    /**
     * Getting the class attributes using a custom format
     * @return a custom format string for the class
     */
    @Override
    public String toString() {
        return name+"(" +
                "cap=" + capacity +
                ", type=" + this.getStringFromType() +
                ')';
    }
}
