package cmds;

import io.cmds.OutputCommand;
import server.Player;
import server.SimpleServer;

import java.util.List;

public class SendCommand implements ICommand {

    public OutputCommand execute(SimpleServer s, Player p, List<String> args) {
        OutputCommand out = new OutputCommand();
        if(p == null) {
            out.setCommand("error");
            out.setMessage("You are not logged in");
            return out;
        }
        StringBuilder sb = new StringBuilder("");
        for(var arg: args) {
            sb.append(arg+" ");
        }
        sb.deleteCharAt(sb.length() -1);
        String message = sb.toString();
        for(var friend : p.getFriends()) {
            synchronized (friend) {
                friend.newMessage(message);
            }
        }

        out.setCommand("display");
        out.setMessage("Successfully sent message '"+message+"' to all your friends");

        return out;
    }
}
