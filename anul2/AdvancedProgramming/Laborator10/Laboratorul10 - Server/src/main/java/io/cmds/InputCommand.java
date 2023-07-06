package io.cmds;

import java.util.ArrayList;
import java.util.List;

public class InputCommand {
    private String command;
    private List<String> args = new ArrayList<>();

    public InputCommand(String command, List<String> args) {
        this.command = command;
        this.args = args;
    }

    public InputCommand() {
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
        return "InputCommand{" +
                "command='" + command + '\'' +
                ", args=" + args +
                '}';
    }
}
