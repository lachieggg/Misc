/*
 * RPG Game Engine
 * Author: Lachlan Grant
 */

import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;

/** Represents the player and controls position,
 *  and rendering of the player icon
 *
 */
public class Player {
	/** Player variables
     * @param xPos The current x position of the player, in pixels relative to the map
     * @param yPos The current y position of the player, in pixels relative to the map
     * @param playerIcon The Image object, which is rendered to the screen center
     */
	private double xPos;
	private double yPos;


	private Image playerIcon;

	Player(double xPos, double yPos) throws SlickException {
		/* Define the x and y coordinates of the player */
		this.xPos = xPos;
		this.yPos = yPos;
		/* Define the player icon as an image */
		playerIcon = new Image("assets/units/player.png");
	}
	/** Update the x and y positions
	 */
	public void update(double newXPos, double newYPos) {

		this.xPos = newXPos;
		this.yPos = newYPos;
	}

	/** Draws the player to the screen
	 */
	public void drawPlayer() {
		playerIcon.drawCentered(RPG.screenwidth/2, RPG.screenheight/2);
	}

	/* Getters and setters of the players position */
	public double getXPos() {
		return xPos;
	}

	public double getYPos() {
		return yPos;
	}

	public void setXPos(double xPos) {
		this.xPos = xPos;
	}

	public void setYPos(double yPos) {
		this.yPos = yPos;
	}

}
