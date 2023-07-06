package com.pa;

public class Main {

    public static void main(String[] args) {
        Problem pb = new Problem();

        // adding all user events that we want to calculate
        pb.addEvent(new Event("C1",100,"08:00","10:00"));
        pb.addEvent(new Event("C2",100,"10:00","12:00"));
        pb.addEvent(new Event("L1",30,"08:00","10:00"));
        pb.addEvent(new Event("L2",30,"08:00","10:00"));
        pb.addEvent(new Event("L3",30,"10:00","12:00"));

        // adding all rooms with their capacity
        pb.addRoom(new ComputerLabs("401", 30, "ubuntu"));
        pb.addRoom(new ComputerLabs("403", 30, "windows"));
        pb.addRoom(new ComputerLabs("405", 30, "centos"));
        pb.addRoom(new LectureHalls("309", 100, true));

        // solving the problem using greedy algorithm
        Algorithm greedy = new GreedyAlgorithm(pb);
        // making sure we can actually solve the problem
        try {
            Solution sol = greedy.solve();
            System.out.println(sol.toString());
        } catch (Exception e) {
            System.err.println("Couldn't find a valid solution!");
        }

    }
}
