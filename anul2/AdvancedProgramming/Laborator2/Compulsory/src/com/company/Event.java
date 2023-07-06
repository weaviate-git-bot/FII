package com.company;

/**
 * @Class The event type
 *
 */
public class Event {
    private String name;
    private int size;
    private int startTime;
    private int endTime;

    /**
     * The constructor of the class
     * @param name name of the Event
     * @param size the maximum amount of people allowed to this specific event
     * @param startTime the start of the event
     * @param endTime the end of the event
     */
    public Event(String name, int size, int startTime, int endTime) {
        this.name = name;
        this.size = size;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    /**
     * Getting the name of the event
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * Setting the name of the event
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getting the size of the event
     * @return size
     */
    public int getSize() {
        return size;
    }

    /**
     * Setting the size of the event. It must be greater then 0
     * @param size
     */
    public void setSize(int size) {
        if (size < 0) {
            throw new IllegalArgumentException("Size must be greater then 0.");
        }
        this.size = size;
    }

    /**
     * Getting the start time of the event
     * @return startTime
     */
    public int getStartTime() {
        return startTime;
    }

    /**
     * Setting the start time of the event
     * @param startTime
     */
    public void setStartTime(int startTime) {
        this.startTime = startTime;
    }

    /**
     * Getting the end time of the event
     * @return endTime
     */
    public int getEndTime() {
        return endTime;
    }

    /**
     * Setting the end time of the event
     * @param endTime
     */
    public void setEndTime(int endTime) {
        if(this.endTime < this.startTime) {
            throw new IllegalArgumentException("End time must be greater then start time");
        }
        this.endTime = endTime;
    }

    /**
     * Getting the class attributes using a custom format
     * @return a custom format string for the class
     */
    @Override
    public String toString() {
        return name + "(" +
                "size=" + size +
                ", start=" + startTime +
                ", end=" + endTime +
                ')';
    }
}
