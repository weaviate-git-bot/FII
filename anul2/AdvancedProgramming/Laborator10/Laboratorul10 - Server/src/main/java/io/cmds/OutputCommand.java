package io.cmds;

import java.util.ArrayList;
import java.util.List;

public class OutputCommand {
    private String command, message;
    private List<String> args = new ArrayList<>();

    public OutputCommand(String message, String command, List<String> args) {
        this.message = message;
        this.command = command;
        this.args = args;
    }

    public OutputCommand(String message) {
        this.message = message;
        this.command = "display";
    }

    public OutputCommand() {
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
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

    @Override
    public String toString() {
        return "OutputCommand{" +
                "command='" + command + '\'' +
                ", message='" + message + '\'' +
                ", args=" + args +
                '}';
    }
}
