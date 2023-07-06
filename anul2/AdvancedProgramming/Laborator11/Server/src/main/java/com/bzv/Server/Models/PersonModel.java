package com.bzv.Server.Models;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class PersonModel implements Comparable {
    private String name;
    private String email;
    private Set<PersonModel> friends = new HashSet<>();
    private List<String> messages = new ArrayList<>();

    public PersonModel() {
    }

    public PersonModel(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public int compareTo(Object o){
        if (o == null) throw new NullPointerException();
        if (!(o instanceof PersonModel person))
            throw new ClassCastException("Uncomparable objects!");
        return Integer.compare(this.friends.size(), person.friends.size());
    }

    public void addFriend(PersonModel p) {
        this.friends.add(p);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Set<String> getFriendsName() {
        Set<String> friendsName = new HashSet<>();
        friends.forEach(x -> friendsName.add(x.getName()));
        return friendsName;
    }

    public List<String> getMessages() {
        return messages;
    }

    public void setMessages(List<String> messages) {
        this.messages = messages;
    }
}
