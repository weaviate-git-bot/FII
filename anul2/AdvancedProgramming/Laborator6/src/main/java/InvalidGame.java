/**
 * @class InvalidGame
 * A custom exception that is thrown when certain game settings are invalid
 */
public class InvalidGame extends Exception{
    public InvalidGame(String message) {
        super(message);
    }
}
