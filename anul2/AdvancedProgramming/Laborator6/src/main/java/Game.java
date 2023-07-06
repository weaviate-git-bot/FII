import java.awt.*;
import java.util.*;

/**
 * @class Game
 * A class that models the actual game
 */
public class Game {
    private int directions[] = {-1, 1, 1, -1 };
    private int rows, columns;
    private Graph sticksMap;
    private Player redPlayer, bluePlayer;
    private boolean playerAdded = false;
    private boolean isRed = true;

    /**
     * A default constructor for Serializable
     */
    public Game() {

    }

    /**
     * The constructor that's used for initialization
     * @param rows
     * @param columns
     */
    public Game(int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        this.sticksMap = new Graph(rows * columns);
    }

    /**
     * A way to initialize the game after the constructor (if needed to reinitialize)
     * @param rows
     * @param columns
     */
    public void initialize(int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        this.initialize();
    }

    /**
     * Validating the sticks generator
     * @param left the current select node
     * @param right the node we want to select
     * @return true if all conditions are met, false otherwise
     */
    private boolean validateGeneration(int left, int right) {
        if(right < 0 || right > this.rows * this.columns)
            return false;
        if(this.sticksMap.pairExists(left, right))
            return false;

        // checking for diagonal drawings
        if(right % this.rows == 0 && left == right - 1)
            return false;

        if(left % this.rows == 0 && left == right + 1)
            return false;
        return true;
    }

    /**
     * A random number generator
     * @param min
     * @param max
     * @return a number in the given interval
     */
    public int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
    }

    /**
     * Initializing the game and drawing the sticks
     */
    public void initialize() {
        // first we should update the directions vector
        directions[0] = -1 * this.rows;
        directions[2] = this.rows;

        int sticksCounter = 2 * this.rows * this.columns;
        this.sticksMap.reinitializeGraph();

        System.out.format("Sticks that will be added: %d\n", sticksCounter);
        int value = getRandomNumber(0, this.rows * this.columns - 1);
        this.sticksMap.createNode(value);

        Queue<Integer> queue = new LinkedList<>();
        queue.add(value);

        int idx = 0;
        while (idx <= sticksCounter && !queue.isEmpty()) {
            int current = queue.poll();
            int added = 0;
            for(int i = 0; i < 4; ++i) {
                int newNode = current + this.directions[i];
                if(validateGeneration(current, newNode)) {
                    queue.add(newNode);
                    this.sticksMap.createNode(newNode);
                    this.sticksMap.createPair(newNode, current);
                    added++;
                }
            }
            idx += added;
        }

        System.out.println("Finished drawing");

    }

    /**
     * Add a new player to the game
     * @param p
     * @throws InvalidGame when you add more than two players
     */
    public void addPlayer(Player p) throws InvalidGame {
        if(playerAdded == true) {
            throw new InvalidGame("You can have up to two players!");
        }
        if (this.redPlayer == null) {
            this.redPlayer = p;
        } else {
            this.bluePlayer = p;
            playerAdded = true;
        }
    }

    /**
     * Starting the game, doing all pre-checks
     * @throws InvalidGame
     */
    public void start() throws InvalidGame {
        if(playerAdded == false) {
            throw new InvalidGame("You must have two players added to this game");
        }
    }

    /**
     * Validating a player move
     * @param x
     * @param y
     * @return true if the player move is valid, false otherwise
     */
    public boolean validate(int x, int y) {
        // reverse engineer the location
        int location = x / this.rows + y % this.rows;
        System.out.println(location);
        return true;
    }

    /**
     * Get current player color
     * @return color of the current player
     */
    public Color colorOfCurrentPlayer() {
        if (isRed)
            return this.redPlayer.getColor();
        return this.bluePlayer.getColor();
    }

    /**
     * Getting the rows
     * @return rows
     */
    public int getRows() {
        return rows;
    }

    /**
     * Setting the rows
     * @param rows
     */
    public void setRows(int rows) {
        this.rows = rows;
    }

    /**
     * Getting the columns
     * @return columns
     */
    public int getColumns() {
        return columns;
    }

    /**
     * Setting the columns
     * @param columns
     */
    public void setColumns(int columns) {
        this.columns = columns;
    }

    /**
     * Getting the stick map
     * @return sticksMap
     */
    public Graph getSticksMap() {
        return sticksMap;
    }

    /**
     * Setting the stick map
     * @param sticksMap
     */
    public void setSticksMap(Graph sticksMap) {
        this.sticksMap = sticksMap;
    }

    /**
     * Player added
     * @return playerAdded
     */
    public boolean isPlayerAdded() {
        return playerAdded;
    }

    /**
     * Setting if the players were added
     * @param playerAdded
     */
    public void setPlayerAdded(boolean playerAdded) {
        this.playerAdded = playerAdded;
    }

    /**
     * Getting red player
     * @return redPlayer
     */
    public Player getRedPlayer() {
        return redPlayer;
    }

    /**
     * Setting the red player
     * @param redPlayer
     */
    public void setRedPlayer(Player redPlayer) {
        this.redPlayer = redPlayer;
    }

    /**
     * Getting the blue player
     * @return bluePlayer
     */
    public Player getBluePlayer() {
        return bluePlayer;
    }

    /**
     * Setting the blue player
     * @param bluePlayer
     */
    public void setBluePlayer(Player bluePlayer) {
        this.bluePlayer = bluePlayer;
    }

    /**
     * Getting current player
     * @return isRed
     */
    public boolean isRed() {
        return isRed;
    }

    /**
     * Setting current player
     * @param red
     */
    public void setRed(boolean red) {
        isRed = red;
    }
}
