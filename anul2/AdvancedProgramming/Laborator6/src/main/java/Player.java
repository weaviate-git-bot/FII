import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import java.awt.*;
import java.io.Serializable;

/**
 * @class Player
 * A player class that adds some customization options
 */
@JsonIgnoreProperties(value = { "color" })
public class Player {
    private Color color;
    private String ign;

    public Player() {

    }
    /**
     * A constructor that sets the color and name of the player
     * @param color
     * @param ign
     */
    public Player(Color color, String ign) {
        this.color = color;
        this.ign = ign;
    }

    /**
     * Getting the color of the player
     * @return color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Setting the color of the player
     * @param color
     */
    public void setColor(Color color) {
        this.color = color;
    }

    /**
     * Getting the name of the player
     * @return ign
     */
    public String getIgn() {
        return ign;
    }

    /**
     * Setting the name of the player
     * @param ign
     */
    public void setIgn(String ign) {
        this.ign = ign;
    }
}
