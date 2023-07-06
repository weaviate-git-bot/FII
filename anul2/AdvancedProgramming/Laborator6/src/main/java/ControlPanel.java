import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

/**
 * @class ControlPanel
 * The class that controls the bottom panel
 * This class is responsible with loading, saving, screenshotting the game and exiting
 */
public class ControlPanel extends JPanel {
    final MainFrame frame;
    JButton loadBtn = new JButton("Load");
    JButton saveBtn = new JButton("Save");
    JButton screenShootBtn = new JButton("Screenshot");
    JButton exitBtn = new JButton("Exit");

    /**
     * The contractor that initializes the Panel
     * @param frame the MainFrame of the app
     */
    public ControlPanel(MainFrame frame) {
        this.frame = frame;

        init();
    }

    /**
     * A function that renders all the buttons and adds the listener functions
     */
    private void init() {
        setLayout(new GridLayout(1,3));

        add(this.loadBtn);
        add(this.saveBtn);
        add(this.screenShootBtn);
        add(this.exitBtn);


        exitBtn.addActionListener(this::exitGame);
        saveBtn.addActionListener(this::saveGame);
        loadBtn.addActionListener(this::loadGame);
        screenShootBtn.addActionListener(this::screenShot);
    }

    /**
     * Taking a screenshot of the current game
     * @param e
     */
    private void screenShot(ActionEvent e) {
        this.frame.canvas.saveBoard();
    }

    /**
     * Loading a previous game
     * @param e
     */
    private void loadGame(ActionEvent e) {
        try {
            Game loaded = GameUtil.load(Main.GAME_PATH + "/game.json");
            this.frame.configPanel.setGame(loaded);
            this.frame.configPanel.spinnerCol.setValue(loaded.getColumns());
            this.frame.configPanel.spinnerRow.setValue(loaded.getRows());
            this.frame.configPanel.loadGame();
        } catch (Exception exception) {
            System.err.println(exception.getMessage());
        }
    }

    /**
     * Saving the current game
     * @param e
     */
    private void saveGame(ActionEvent e) {
        try {
            GameUtil.save(this.frame.configPanel.getGame(), Main.GAME_PATH+ "/game.json");
        } catch (Exception exception) {
            System.err.println(exception.getMessage());
        }
    }

    /**
     * Exiting the application
     * @param e
     */
    private void exitGame(ActionEvent e) {
        frame.dispose();
    }
}
