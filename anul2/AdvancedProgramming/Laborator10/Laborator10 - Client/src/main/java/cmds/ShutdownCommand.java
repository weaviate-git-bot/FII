package cmds;

import io.cmds.OutputCommand;

import java.io.IOException;
import java.net.Socket;

public class ShutdownCommand implements ICommand{
    private Socket socket = null;

    public ShutdownCommand setSocket(Socket s) {
        this.socket = s;
        return this;
    }

    public String execute(OutputCommand data) {
        if(socket == null) {
            throw new IllegalArgumentException("You should set the socket before using it!");
        }
        try {
            socket.close();
        } catch (Exception e) {

        }
        return "Have a great day. Bye!\n";
    }
}
