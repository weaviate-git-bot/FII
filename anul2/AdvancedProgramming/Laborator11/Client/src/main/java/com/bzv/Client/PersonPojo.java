package com.bzv.Client;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.HashSet;
import java.util.Set;

public class PersonPojo {
    @JsonProperty("email")
    public String email;

    @JsonProperty("name")
    public String name;

    @JsonProperty("friendsName")
    public Set<String> friends = new HashSet<>();

    @Override
    public String toString() {
        return "PersonPojo{" +
                "email=" + email +
                ", name='" + name + '\'' +
                ", friends=" + friends +
                '}';
    }
}
