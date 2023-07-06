/**
 * @class Represeting a Tile
 */
public class Tile {
    private final char letter;
    private final int points;

    /**
     * Give the character and the number of points it has
     * @param letter
     * @param points
     */
    public Tile(char letter, int points) {
        this.letter = letter;
        this.points = points;
    }

    /**
     * Gett the letter
     * @return letter
     */
    public char getLetter() {
        return letter;
    }

    /**
     * Get the points
     * @return points
     */
    public int getPoints() {
        return points;
    }

    /**
     * Get the tile in a string format
     * @return
     */
    @Override
    public String toString() {
        return letter + "= " + points + "p";
    }
}
