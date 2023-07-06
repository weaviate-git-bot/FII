import com.opencsv.CSVReader;

import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

/**
 * @class that reads data from a given csv and builds Tiles
 */
public class Bag {
    private final List<Tile> tiles = new ArrayList<>();
    private final String pathToCSV = ".\\tiles.csv";

    /**
     * Reading pathToCSV file and creating the alphabet
     */
    public Bag() {
        try (CSVReader reader = new CSVReader(new FileReader(pathToCSV))) {
            String[] lineInArray;
            boolean firstLine = false;
            while ((lineInArray = reader.readNext()) != null) {
                if(firstLine == false) {
                    firstLine = !firstLine;
                    continue;
                }
                createAlphabet(lineInArray[0], lineInArray[1], lineInArray[2]);
            }
        } catch(Exception e) {
            System.err.println(e.getMessage());
        }
        System.out.println(this.tiles);
    }

    /**
     * Creating the alphabet that will be used later in the game
     * @param character
     * @param points
     * @param amount
     */
    private void createAlphabet(String character, String points, String amount) {
        Tile t = new Tile(character.toLowerCase().charAt(0), Integer.parseInt(points, 10));
        int am = Integer.parseInt(amount);
        for(int idx = 0; idx < am; ++idx) {
            this.tiles.add(t);
        }
    }

    /**
     * Randomly extracting a given number of tiles
     * @param howMany
     * @return a list of tiles having the given length
     */
    public synchronized List<Tile> extractTiles(int howMany) {
        List<Tile> extracted = new ArrayList<>();
        for (int i = 0; i < howMany; i++) {
            if (tiles.isEmpty()) {
                break;
            }

            int randomInt = Game.getRandomNumber(0, tiles.size());
            var tile = tiles.stream().skip(randomInt).findFirst().get();

            extracted.add(tile);
            tiles.remove(tile);
        }
        return extracted;
    }

}
