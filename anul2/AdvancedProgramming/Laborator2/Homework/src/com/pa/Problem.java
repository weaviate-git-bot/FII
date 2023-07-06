package com.pa;

/**
 * @Class Problem - a class that describes Room Assignment Problem 
 */
public class Problem {
    private Event[] events;
    private Room[] rooms;
    private int roomCounter = 0, eventCounter = 0;

    /**
     * Constructor which initializes the events and rooms arrays
     */
    public Problem() {
        this.events = new Event[150];
        this.rooms = new Room[150];
    }

    /**
     * Adding a new room to the problem. Note that we don't allow adding the same room twice.
     * @param newRoom
     */
    public void addRoom(Room newRoom) {
        for(int i = 0; i < this.roomCounter; ++i) {
            if(this.rooms[i].equals(newRoom) == true) {
                throw new IllegalArgumentException("You can't have two rooms with the same name!");
            }
        }
        this.rooms[this.roomCounter] = newRoom;
        ++this.roomCounter;
    }

    /**
     * Adding a new event to the problem. Note that we don't allow adding the same event twice.
     * @param newEvent
     */
    public void addEvent(Event newEvent) {
        for(int i = 0; i < this.eventCounter; ++i) {
            if(this.events[i].equals(newEvent) == true) {
                throw new IllegalArgumentException("You can't have two events with the same name!");
            }
        }

        this.events[this.eventCounter] = newEvent;
        ++this.eventCounter;
    }

    /**
     * Getting all events of this problem
     * @return Event[] events
     */
    public Event[] getEvents() {
        return this.events;
    }

    /**
     * Getting all rooms of this problem
     * @return Room[] rooms
     */
    public Room[] getRooms() {
        return this.rooms;
    }

    public int getRoomCounter() {
        return this.roomCounter;
    }

    public  int getEventCounter() {
        return this.eventCounter;
    }
}
