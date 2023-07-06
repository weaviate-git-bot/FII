package com.pa;

import java.time.LocalTime;
import java.util.Arrays;

/**
 * @Class An extension of Algorithm class that solves the Timetable problem using a greedy approach
 */
public class GreedyAlgorithm extends Algorithm {
    private Event[] sortedEvents;

    /**
     * Constructor of the class, setting the problem instance
     * @param pb the problem that we want to solve
     */
    public GreedyAlgorithm(Problem pb) {
        this.pb = pb;
        this.sortedEvents = new Event[pb.getEventCounter()];

    }

    /**
     * Checking it two events are happening at the same time
     * @param e1 index of first event
     * @param e2 index of second event
     * @return true if two event are overlapping, false otherwise
     */
    private boolean areEventsOverlapping(int e1, int e2) {
        LocalTime startTime1 = pb.getEvents()[e1].getStartTime();
        LocalTime finishTime1 =  pb.getEvents()[e1].getEndTime();
        LocalTime startTime2 = pb.getEvents()[e2].getStartTime();
        LocalTime finishTime2 = pb.getEvents()[e2].getEndTime();

        if(startTime1.isBefore(finishTime2)  && startTime2.isBefore(finishTime1)) {
            return true;
        }
        return false;
    }

    /**
     * Solving the problem using greedy coloring algorithm
     * @return a Solution
     */
    public Solution solve() {
        System.out.println("Starting to solve the problem");
        Solution sol = new Solution(this.pb.getEvents());
        int numberOfVertex = pb.getEventCounter();
        Graph matching = new Graph(numberOfVertex);

        // drawing edges between nodes
        for(int idx = 0; idx < numberOfVertex - 1; ++idx) {
            for (int it = idx + 1; it < numberOfVertex; ++it) {
                if(this.areEventsOverlapping(it,idx)) {
                    matching.addEdge(it, idx);
                }
            }
        }
//        matching.print();

        // running the coloring algorithm
        int numberOfColors =  pb.getRoomCounter();
        boolean colors[] = new boolean[numberOfColors];
        int result[] = new int[numberOfVertex];

        Arrays.fill(result, -1);
        // assigning the first room
        for(int room = 0; room < numberOfColors; ++room) {
            if(pb.getRooms()[room].getCapacity() >= pb.getEvents()[0].getSize()) {
                result[0] = room;
                sol.setAssignment(0, pb.getRooms()[room]);
            }
        }

        Arrays.fill(colors, true);

        for(int vertex = 1 ; vertex < numberOfVertex; ++vertex)   {

            // getting the current neighbours of this event
            boolean[] row = matching.getRow(vertex);

            for(int width = 0; width < numberOfVertex; ++width) {
                // if the events have an edge and the color is not assigned we flag it as unavailable
                if(row[width] && result[width] != -1) {
                    colors[result[width]] = false;
                }
            }

            int room;
            // assign the color based on availability and room capacity
            for(room = 0; room < numberOfColors; ++room) {
                if(colors[room] && pb.getRooms()[room].getCapacity() >= pb.getEvents()[vertex].getSize()) {
                    break;
                }
            }
            if(room >= numberOfColors) {
                throw new IllegalArgumentException("Failed to color this graph");
            }
            result[vertex] = room;
            sol.setAssignment(vertex, pb.getRooms()[room]);
            Arrays.fill(colors, true);
        }

//        for(int i=0; i < numberOfVertex; ++i) {
//            System.out.format("%s has room %s\n", pb.getEvents()[i].getName(), pb.getRooms()[result[i]].getName());
//        }
        System.out.println("Problem solved successfully");

        return sol;
    }
}
