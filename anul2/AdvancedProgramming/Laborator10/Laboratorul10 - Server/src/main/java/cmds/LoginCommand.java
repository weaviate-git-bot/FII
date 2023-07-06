package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

public class LoginCommand implements ICommand {
    private Player player;

    public Player getPlayer() {
        return player;
    }

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        this.player = p;
        if(this.player != null) {
            out.setCommand("error");
            out.setMessage("You are already logged in");
            return out;
        }

        synchronized (s) {
            this.player = s.getDb().getPlayerByName(args.get(0));

            if(player == null) {
                out.setCommand("error");
                out.setMessage("Username doesn't exist in our database");
            } else {
                out.setCommand("display");
                out.setMessage("Successfully logged in");
            }
        }

        return out;
    }
}
