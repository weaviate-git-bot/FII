package io.cmds;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InputCommand {
    private String command;
    private List<String> args = new ArrayList<String>();

    public InputCommand() {
        command = "";
    }

    public InputCommand(String str) {
        String[] parts = str.split(" ");
        if(parts.length < 1) {
            throw new IllegalArgumentException("You must enter at least the command!");
        }
        this.command = parts[0];
        this.args = parseArguments(parts);
    }

    private List<String> parseArguments(String[] parts) {
        // TODO: Here you can add support for things like "Hello World" to be 1 param not 2
        return Arrays.asList(parts).subList(1, parts.length);
    }

    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }

    public List<String> getArgs() {
        return args;
    }

    public void setArgs(List<String> args) {
        this.args = args;
    }
}
