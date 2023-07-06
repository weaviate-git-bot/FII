package server;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Player {
    private String name;
    private List<Player> friends = new ArrayList<>();
    private List<String> messagesToRead = new ArrayList<>();

    public Player(String name) {
        this.name = name;
    }

    public void addFriend(Player p) {
        this.friends.add(p);
    }

    public void newMessage(String msg) {
        this.messagesToRead.add(msg);
    }

    public void markMessageAsRead(String msg) {
        this.messagesToRead.removeIf(x -> x.compareTo(msg) == 0);
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Player> getFriends() {
        return friends;
    }

    public void setFriends(List<Player> friends) {
        this.friends = friends;
    }

    public List<String> getMessagesToRead() {
        return messagesToRead;
    }

    public void setMessagesToRead(List<String> messagesToRead) {
        this.messagesToRead = messagesToRead;
    }

    @Override
    public String toString() {
        return "Player{" +
                "name='" + name + '\'' +
                '}';
    }
}
