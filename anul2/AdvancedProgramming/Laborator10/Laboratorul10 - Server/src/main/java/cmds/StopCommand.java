package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.net.Socket;
import java.util.List;

public class StopCommand implements ICommand {
    private Socket socket = null;

    public StopCommand setSocket(Socket socket) {
        this.socket = socket;
        return this;
    }

    public OutputCommand execute(SimpleServer server, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(this.socket == null) {
            throw new IllegalArgumentException("You must set the socket before executing this command");
        }
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You must be logged in to take administrative actions");
            return out;
        }
        server.setRunning(false);
        out.setCommand("shutdown");
        out.setMessage("Server stopped successfully");
        return out;
    }
}
