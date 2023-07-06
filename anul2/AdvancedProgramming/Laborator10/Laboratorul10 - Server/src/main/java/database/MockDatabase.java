package database;

import server.Player;

import java.util.ArrayList;
import java.util.List;

public class MockDatabase implements IDatabase{
    private List<Player> players;

    public MockDatabase() {
        this.players = new ArrayList<>();
    }

    public void addPlayer(Player p) {
        this.players.add(p);
    }
    public void removePlayer(Player p) {
        this.players.remove(p);
    }
    public Player getPlayerByName(String name) {
        for(var p : this.players) {
            if(p.getName().equals(name))
                return p;
        }
        return null;
    }
}
