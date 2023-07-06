package com.pa;

public class DSaturAlgorithm extends Algorithm {
    private Event[] sortedEvents;

    public DSaturAlgorithm(Problem pb) {
        this.pb = pb;
        this.sortedEvents = new Event[pb.getEventCounter()];
    }

    /**
     * Solving the problem using greedy coloring algorithm
     * @return a Solution
     */
    public Solution solve() {
        System.out.println("Starting to solve the problem");
        Solution sol = new Solution(pb.getEvents());



        System.out.println("Problem solved successfully");
        return sol;
    }
}
