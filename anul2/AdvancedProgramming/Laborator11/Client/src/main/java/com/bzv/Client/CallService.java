package com.bzv.Client;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.util.List;

public class CallService {
    final Logger log = (Logger) LoggerFactory.getLogger(CallService.class);

    public List<PersonPojo> call(String path) {
        String uri = String.format("http://localhost:1337%s",path);
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<List<PersonPojo>> response = restTemplate.exchange(
                uri, HttpMethod.GET, null,
                new ParameterizedTypeReference<>() {
                });
        List<PersonPojo> result = response.getBody();
        System.out.println(result);
        assert result != null;
        result.forEach(p -> log.info(p.toString()));
        return result;
    }
}
