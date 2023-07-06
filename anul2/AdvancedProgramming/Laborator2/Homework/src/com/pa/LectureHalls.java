package com.pa;

/**
 * @Class LectureHalls
 * A class that extends Room
 */
public class LectureHalls extends Room{
    private boolean videoProjector;

    /**
     * The constructor for the class
     * @param name the name of the room
     * @param type the type of the room
     * @param capacity the capacity of the room
     */
    public LectureHalls(String name, int capacity, boolean videoProjector) {
        this.name = name;
        this.type = "Lecture Hall";
        this.capacity = capacity;
        this.videoProjector = videoProjector;
    }

    /**
     * Getting the video projector property of the class
     * @return true if the class has a video projector, false otherwise
     */
    public boolean isVideoProjector() {
        return videoProjector;
    }

    /**
     * Setting the video projector attribute of the class
     * @param videoProjector
     */
    public void setVideoProjector(boolean videoProjector) {
        this.videoProjector = videoProjector;
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
     * Getting the type of the room as a string
     * @return a custom string based on type of the room
     */

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
