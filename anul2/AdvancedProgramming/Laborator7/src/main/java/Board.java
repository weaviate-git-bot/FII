import java.util.ArrayList;
import java.util.List;

/**
 * @class That emulates the current list of created words
 */
public class Board {
    private final List<String> words = new ArrayList<>();

    /**
     * Adding a word for a specific player
     * @param player
     * @param word
     */
    public synchronized void addWord(Player player, String word) {
        words.add(word);
        System.out.println(player.getName() + ": " + word);
    }

    /**
     * Getting the string version of the word
     * @return word
     */
    @Override
    public String toString() {
        return words.toString();
    }
}