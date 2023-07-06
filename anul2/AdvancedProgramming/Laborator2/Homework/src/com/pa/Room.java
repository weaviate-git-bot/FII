package com.pa;

/**
 * @Class Room representing a room in which an event can be held.
 */
public abstract class Room {
    protected String name;
    protected String type;
    protected int capacity;

    abstract public String getName();
    abstract public void setName(String name);
    abstract public int getCapacity();
    abstract public void setCapacity(int capacity);
}
