package database;

import server.Player;

public interface IDatabase {
    void addPlayer(Player p);
    void removePlayer(Player p);
    Player getPlayerByName(String name);
}
