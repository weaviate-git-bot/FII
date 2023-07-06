import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Thread.sleep;

public class Player implements Runnable {
    private String name;
    private Game game;
    private boolean running;
    final private int tilesToExtract = 7;
    private int score = 0;
    public Player(String name) { this.name = name; this.running = true; }

    private void wordLogic(List<Tile> extracted) {
        List<Tile> cExtracted = new ArrayList<>(extracted);

        String word = null;
        int points = 0;

        while(true) {
            extracted = new ArrayList<>();
            extracted.addAll(cExtracted);

            System.out.println("[!] The tiles that you have are: " + extracted);
            System.out.print("[>] Input: ");
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            points = 0;

            try {
                word = reader.readLine();
                word.toLowerCase();
            } catch (Exception e) {
                e.printStackTrace();
            }

            boolean allCharsFound = true;

            for(char c : word.toCharArray()) {

                boolean found = false;
                for(Tile t: extracted) {
                    if(c == t.getLetter()) {
                        found = true;
                        extracted.remove(t);
                        points += t.getPoints();
                        break;
                    }
                }

                if(found == false) {
                    allCharsFound = false;
                    System.out.println("You must use all tiles!");
                    break;
                }

            }

            if(allCharsFound) {
                break;
            }
        }

        System.out.println("Trying to search the word: " + word);

        if(game.getDictionary().isWord(word)) {
            game.getBoard().addWord(this, word);
            points = points * word.length();
        } else {
            points = 0;
        }
        score += points;
        System.out.println("This your you got +"+points+"p!");
        System.out.println("Your score is: "+score+"p!");

    }

    private void submitWord() {
        List<Tile> extracted = game.getBag().extractTiles(tilesToExtract);
        if (extracted.isEmpty()) {
            System.out.println("No more tiles left. Ending game");
            running = false;
        } else {
            wordLogic(extracted);
        }

        System.out.println("Submitted");

        try {
            sleep(50);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    //    implement the run method;
    @Override
    public void run() {
        while(running) {
            waitTurn(game.getPlayers().indexOf(this));

            System.out.format("\nIt's time for %s to submit a word!\n", this.name);
            if (running) {
                this.submitWord();
            }

            if (game.getTimekeeper().isAlive()) {
                System.out.println("Time spent: " + game.getDuration() / 1_000 + "s");
                game.nextPlayer();
            } else {
                System.out.println("Time limit has been reached.");
                running = false;
            }
        }

        synchronized (game) {
            game.calculateWinner();
        }
    }

    public void stop() {
        this.running = false;
    }

    private void waitTurn(int currentPlayer) {
        synchronized (game) {
            game.notifyAll();

            while(game.getActivePlayer() != currentPlayer) {
                try {
                    game.wait();
                } catch(InterruptedException e) {
                    System.err.println(e.getMessage());
                }
            }
        }
    }

    public int getScore() {
        return score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

    public boolean isRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }
}