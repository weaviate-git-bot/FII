import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.io.File;
import java.io.IOException;

/**
 * A class for loading and saving the Game
 */
public class GameUtil {
    /**
     * Saving a catalog in a JSON format
     * @param game
     * @param path
     * @throws IOException
     */
    public static void save(Game game, String path) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);
        mapper.writeValue(new File(path), game);
    }

    /**
     * Loading the game class
     * @param path the path to the file
     * @return a new game class loaded from the file
     * @throws IOException
     */
    public static Game load(String path) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Game game = mapper.readValue(new File(path), Game.class);
        return game;
    }
}