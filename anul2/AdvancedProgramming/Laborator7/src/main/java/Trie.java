import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;

/**
 * @class A class that simulates a Trie data structure
 */
public class Trie {
    private static final int ALPHABET_SIZE = 26;

    private boolean isLeaf;
    private List<Trie> children = null;

    /**
     * Initializing default values
     */
    Trie()
    {
        isLeaf = false;
        children = new ArrayList<>(Collections.nCopies(ALPHABET_SIZE, null));
    }

    /**
     * Insert a normalized word (all letters are lower case)
     * @param key
     */
    public void insert(String key)
    {
        Trie curr = this;
        key = key.toLowerCase();
        for (char c: key.toCharArray())
        {
            if (curr.children.get(c - 'a') == null) {
                curr.children.set(c - 'a', new Trie());
            }

            curr = curr.children.get(c - 'a');
        }

        curr.isLeaf = true;
    }

    /**
     * Doing an iterative search to find if the word exists or not
     * @param key
     * @return true if the key is in the Trie, false otherwise
     */
    public boolean search(String key)
    {
        Trie curr = this;

        for (char c: key.toCharArray())
        {
            curr = curr.children.get(c - 'a');

            if (curr == null) {
                return false;
            }
        }

        return curr.isLeaf;
    }
}
