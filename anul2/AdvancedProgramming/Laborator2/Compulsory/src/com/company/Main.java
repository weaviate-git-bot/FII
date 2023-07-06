package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        // instantiating all the Events from the input
        ArrayList<Event> events = new ArrayList<Event>();
        events.add(new Event("C1", 100, 8, 10));
        events.add(new Event("C2", 100, 10, 12));
        events.add(new Event("L1", 30, 8, 10));
        events.add(new Event("L2", 30, 8, 10));
        events.add(new Event("L3", 30, 10, 12));

        ArrayList<Room> rooms = new ArrayList<Room>();
        rooms.add(new Room("401", RoomType.LABORATORY, 30));
        rooms.add(new Room("403", RoomType.LABORATORY, 30));
        rooms.add(new Room("405", RoomType.LABORATORY, 30));
        rooms.add(new Room("309", RoomType.LECTURE_HALL, 100));

        System.out.print("Events: ");
        for (int idx = 0; idx < rooms.size(); ++idx) {
            System.out.format("%s ", events.get(idx).toString());
        }
        System.out.format("\nRooms: ");
        for (int idx = 0; idx < rooms.size(); ++idx) {
            System.out.format("%s ", rooms.get(idx).toString());
        }
        System.out.println();
    }
}
