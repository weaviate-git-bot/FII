package com.bzv.Server.Database;

import java.util.List;

public interface Database<Model> {
    boolean create(Model m);
    List<Model> getAll();
    Model getByName(String name);
    boolean update(String name, String newName);
    boolean delete(String name);
}
