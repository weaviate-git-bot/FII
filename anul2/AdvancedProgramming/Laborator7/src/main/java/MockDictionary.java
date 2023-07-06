import java.io.BufferedReader;
import java.io.FileReader;

/**
 * @class Emulating a fake dictionary
 */
public class MockDictionary extends Dictionary {
    private final Trie dictionary = new Trie();
    private final String pathToDictionary = "./dictionary.txt";

    /**
     * Reading the given dictionary and building a Trie out of him
     */
    public MockDictionary() {
        try (BufferedReader br = new BufferedReader(new FileReader(pathToDictionary))) {
            String line;
            while ((line = br.readLine()) != null) {
                if(line.length() > 4) {
                    dictionary.insert(line.toLowerCase());
                }
            }
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }


    /**
     * Checking if a given string is a word in the dictionary
     * @param str
     * @return true if the string is in the word can be found in the dictionary, false otherwise
     */
    @Override
    public boolean isWord(String str) {
        return dictionary.search(str);
    }
}
