import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

/**
 * @Class ConfigPanel
 *
 * This is a JPanel that setups the grid and starts the game
 */
public class ConfigPanel extends JPanel {
    final MainFrame frame;
    JLabel label;
    JSpinner spinnerCol;
    JSpinner spinnerRow;
    Game game;
    JButton createGameButton = new JButton("Create");
    private int cols, rows;

    /**A
     * The constructor that builds everything
     * @param frame the MainFrame of the application
     */
    public ConfigPanel(MainFrame frame){
        this.frame = frame;
        this.cols = 10;
        this.rows = 10;
        this.game = new Game(this.rows, this.cols);

        // TODO: Add the players from interface...
        try {
            Player red = new Player(Color.RED, "zaBogdan");
            Player blue = new Player(Color.BLUE, "JavaMaster");

            this.game.addPlayer(red);
            this.game.addPlayer(blue);
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        init();
    }

    /**
     * Initialize the buttons, spinner and game
     */
    private void init() {
        label = new JLabel("Grid size: ");
        spinnerCol = new JSpinner(new SpinnerNumberModel(10,2,100,1));
        spinnerRow = new JSpinner(new SpinnerNumberModel(10, 2, 100, 1));
        add(label);
        add(spinnerCol);
        add(spinnerRow);
        add(createGameButton);
        this.game.initialize();

        createGameButton.addActionListener(this::createGame);
    }

    /**
     * Load the game from a game file stored locally
     */
    public void loadGame() {
        this.frame.canvas.redraw();
        this.frame.repaint();
    }

    /**
     * Create a new game when Create button is pressed
     * @param e button event
     */
    public void createGame(ActionEvent e) {
        this.setCols(this.spinnerCol.getValue().hashCode());
        this.setRows(this.spinnerRow.getValue().hashCode());
        this.frame.canvas.redraw();
        this.frame.repaint();
        this.game.initialize(this.rows, this.cols);
    }

    /**
     * Get the columns
     * @return cols
     */
    public int getCols() {
        return cols;
    }

    /**
     * Set the columns
     * @param cols
     */
    public void setCols(int cols) {
        this.cols = cols;
    }

    /**
     * Get the rows
     * @return rows
     */
    public int getRows() {
        return rows;
    }

    /**
     * Set the rows
     * @param rows
     */
    public void setRows(int rows) {
        this.rows = rows;
    }

    /**
     * Get the game instance
     * @return game
     */
    public Game getGame() {
        return game;
    }

    /**
     * Set the game instance
     * @param game
     */
    public void setGame(Game game) {
        this.game = game;
    }
}
