package com.pa;

import java.util.Arrays;

/**
 * @Class Solution
 * A class that containes the solution of Room Assignment Problem
 */
public class Solution {
    private Room[] assignment;
    private Event[] events;

    /**
     * The constructor of the class that initializes the attributes.
     */
    public Solution(Event[] events) {
        this.assignment = new Room[150];
        this.events = new Event[150];
        this.events = events;
    }

    /**
     * Adding the solution to the event
     * @param idx the event id
     * @param room the room object
     */
    public void setAssignment(int idx, Room room) {
        this.assignment[idx] = room;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("");
        for(int idx = 0; idx < events.length; ++idx) {
            if(events[idx] != null && this.assignment[idx] != null) {
                sb.append(events[idx].getName() + " -> " + assignment[idx].getName() + "\n");
            }
        }
        return sb.toString();
    }
}
