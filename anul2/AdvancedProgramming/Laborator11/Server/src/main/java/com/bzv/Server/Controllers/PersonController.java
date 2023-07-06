package com.bzv.Server.Controllers;

import com.bzv.Server.Models.PersonModel;
import com.bzv.Server.Response.Response;
import com.bzv.Server.Services.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/person")
public class PersonController {
    @Autowired
    private PersonService personService;

    @GetMapping
    public List<PersonModel> getPerson() {
        return personService.getListOfPerson();
    }

    @PostMapping(consumes = "application/json")
    public ResponseEntity<Response<PersonModel>> createPerson(@RequestBody PersonModel person) {
        try {
            return new ResponseEntity<>(new Response<>("Successfully added user to database", personService.create(person)), HttpStatus.CREATED);
        } catch(Exception e) {
            return new ResponseEntity<>(new Response<>("Failed to add user to the database: "+ e.getMessage(), null), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping(consumes = "application/json")
    public ResponseEntity<Response<PersonModel>> updatePerson(@RequestParam String name, @RequestBody PersonModel newName) {
        try {
            return new ResponseEntity<>(new Response<>("Successfully updated user from database", personService.update(name, newName)), HttpStatus.OK);
        } catch(Exception e) {
            return new ResponseEntity<>(new Response<>("Failed to update user with name "+name+". Error: "+ e.getMessage(), null), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping
    public ResponseEntity<Response<PersonModel>> deletePerson(@RequestParam String name) {
        try {
            personService.delete(name);
            return new ResponseEntity<>(new Response<>("Successfully removed user from database", null), HttpStatus.OK);
        } catch(Exception e) {
            return new ResponseEntity<>(new Response<>("Failed to delete user with name "+name+". Error: "+ e.getMessage(), null), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
