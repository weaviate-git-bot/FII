package com.bzv.Server.Response;

public class Response<Model> {
    private String message;
    private Model data;

    public Response(String message, Model data) {
        this.message = message;
        this.data = data;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Model getData() {
        return data;
    }

    public void setData(Model data) {
        this.data = data;
    }
}
