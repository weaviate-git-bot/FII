package com.bzv.Server.Services;

import com.bzv.Server.Database.MockDatabase;
import com.bzv.Server.Models.PersonModel;
import org.springframework.stereotype.Service;

import java.security.InvalidKeyException;
import java.util.List;

@Service
public class PersonService {
    private MockDatabase db = MockDatabase.getInstance();

    public List<PersonModel> getListOfPerson() {
        return db.getAll();
    }

    public PersonModel create(PersonModel p) throws InvalidKeyException, Exception{
        var user = db.getByName(p.getName());
        if(user != null) {
            throw new InvalidKeyException("User already exist in our database");
        }
        if(!db.create(p)) {
            throw new Exception("Failed to create the user");
        }
        return p;
    }

    public PersonModel update(String name, PersonModel newName) throws Exception{
        if(!db.update(name, newName.getName())) {
            throw new Exception("Failed to update the user");
        }
        return null;
    }

    public boolean delete(String name) throws Exception{
        var user = db.getByName(name);
        if(user == null) {
            throw new Exception("User doesn't exist in our database");
        }
        if(!db.delete(name)) {
            throw new Exception("Failed to delete the user");
        }
        return true;
    }
}
