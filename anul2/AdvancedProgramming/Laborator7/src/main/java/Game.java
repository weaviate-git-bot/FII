import java.util.ArrayList;
import java.util.List;

public class Game {
    private final Bag bag = new Bag();
    private final Board board = new Board();
    private final Dictionary dictionary = new MockDictionary();
    private final List<Player> players = new ArrayList<>();
    private Thread timekeeper;
    private long startTime = 0;
    private int activePlayer = 0;


    public static void main(String args[]) {
        Game game = new Game();

        game.addPlayer(new Player("Player 1"));
        game.addPlayer(new Player("Player 2"));
        game.addPlayer(new Player("Player 3"));

        game.play();
    }

    /**
     * Add a new player to our game
     * @param player
     */
    public void addPlayer(Player player) {
        players.add(player);
        player.setGame(this);
    }

    /**
     * Start the game and the threads for each player
     */
    public void play() {
        startTime = System.nanoTime();

        timekeeper = new Thread(new Timekeeper());
        timekeeper.setDaemon(true);
        timekeeper.start();


        for (Player player : players) {
            // start a new Thread representing the player;
            new Thread(player).start();
        }
    }

    /**
     * This function will be called by the player who runs out of tiles
     */
    public void calculateWinner() {
        System.out.println("Game has ended!");

        int maxScore = 0;
        Player winner = new Player("none");

        for(Player p : this.getPlayers()) {
            if(p.getScore() > maxScore) {
                maxScore = p.getScore();
                winner = p;
            }
            p.stop();
            synchronized (this) {
                this.nextPlayer();
                this.notifyAll();
            }
        }

        System.out.println("The winner of this game is: " + winner.getName());
    }


    /**
     * Getting the current duration of the game
     * @return
     */
    public long getDuration() { return (System.nanoTime() - startTime) / 1_000_0000; }

    /**
     * Getting the bag
     * @return bag
     */
    public Bag getBag() {
        return bag;
    }

    /**
     * Getting the board
     * @return board
     */
    public Board getBoard() {
        return board;
    }

    /**
     * Getting the dictionary
     * @return dictionary
     */
    public Dictionary getDictionary() {
        return dictionary;
    }

    /**
     * Getting the player
     * @return players
     */
    public List<Player> getPlayers() {
        return players;
    }

    /**
     * Moving to the next player in line
     */
    public void nextPlayer() {
        ++activePlayer;

        if(activePlayer >= players.size())
            activePlayer = 0;
    }

    /**
     * Getting current active player
     * @return activePlayer
     */
    public int getActivePlayer() {
        return activePlayer;
    }

    /**
     * Getting the timekeeper thread
     * @return timekeeper
     */
    public Thread getTimekeeper() {
        return timekeeper;
    }

    /**
     * A random number generator
     * @param min
     * @param max
     * @return a number in the given interval
     */
    public static int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
    }
}