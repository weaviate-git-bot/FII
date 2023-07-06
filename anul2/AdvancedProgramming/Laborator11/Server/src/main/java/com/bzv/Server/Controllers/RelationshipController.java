package com.bzv.Server.Controllers;

import com.bzv.Server.Database.MockDatabase;
import com.bzv.Server.Models.PersonModel;
import com.bzv.Server.Response.Response;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;

@RestController
@RequestMapping("/relationship")
public class RelationshipController {
    private MockDatabase db = MockDatabase.getInstance();

    @GetMapping("/popular/{k}")
    public ResponseEntity<Response<List<PersonModel>>> getPopularPeople(@PathVariable int k) {
        var people = db.getAll();
        Collections.sort(people);
        List<PersonModel> popularPeople = new ArrayList<>();

        int length = people.size() - 1;
        for (int i = 0; i < k; i++)
            popularPeople.add(people.get(length - i));
        return new ResponseEntity<>(new Response<>("This are the first "+ k + " most popular people!", popularPeople), HttpStatus.OK);
    }

    @PostMapping("/{userName}/{friendName}")
    public ResponseEntity<Response<String>> insertRelationship(@PathVariable String userName, @PathVariable String friendName) {
        try {
            PersonModel person = db.getByName(userName);
            PersonModel friend = db.getByName(friendName);

            if (person == null) {
                throw new Exception("Person not found");
            }
            if (friend == null) {
                throw new Exception("Friend not found");
            }

            person.addFriend(friend);
            friend.addFriend(person);

            return new ResponseEntity<>(new Response<>("Friendship added succesfully", null), HttpStatus.GONE);
        } catch (Exception e) {
            return new ResponseEntity<>(new Response<>("Failed to update friendship: "+ e.getMessage(), null), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/{name}")
    public ResponseEntity<Response<Set<String>>> readRelationship(@PathVariable String name) {
        PersonModel person = db.getByName(name);

        if (person == null)
            return new ResponseEntity<>(new Response<>("This person doesn't exist", null), HttpStatus.OK);
        return new ResponseEntity<>(new Response<>("Successfully fetched friends.", person.getFriendsName()), HttpStatus.OK);
    }
}
