package io.cmds;

import java.util.ArrayList;
import java.util.List;

public class OutputCommand {
    private String command = "";
    private String message = "";
    private List<String> args = new ArrayList<>();

    public OutputCommand() {
    }

    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public List<String> getArgs() {
        return args;
    }

    public void setArgs(List<String> args) {
        this.args = args;
    }
}
