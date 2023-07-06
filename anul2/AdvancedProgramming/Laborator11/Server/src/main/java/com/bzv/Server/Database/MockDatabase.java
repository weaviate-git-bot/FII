package com.bzv.Server.Database;

import com.bzv.Server.Models.PersonModel;

import java.util.ArrayList;
import java.util.List;

public class MockDatabase implements Database<PersonModel> {
    private List<PersonModel> users = new ArrayList<>();
    private static MockDatabase db = null;

    private MockDatabase() {
        users.add(new PersonModel("BZV", "bzv@bd.ro"));
        users.add(new PersonModel("DAN", "dan@bd.ro"));
        users.add(new PersonModel("GDT", "gdt@bd.ro"));
        users.add(new PersonModel("BTE", "bte@bd.ro"));
    }

    public static MockDatabase getInstance() {
        if(db == null) {
            db = new MockDatabase();
        }
        return db;
    }
    public boolean create(PersonModel m) {
        if(this.getByName(m.getName()) != null)
            return false;
        this.users.add(m);
        return true;
    }

    public List<PersonModel> getAll() {
        return this.users;
    }

    public PersonModel getByName(String name) {
        System.out.println("get user by name");
        for(var user : users) {
            System.out.println(user.getName());
            if(user.getName().equals(name))
                return user;
        }
        System.out.println("get user by name");

        return null;
    }
    public boolean update(String name, String newName) {
        for(var user : this.getAll()) {
            if(user.getName().equals(name)) {
                user.setName(newName);
                return true;
            }
        }
        return false;
    }
    public boolean delete(String name) {
        var user = this.getByName(name);
        if(user == null)
            return false;
        this.users.remove(user);
        return true;
    }
}
