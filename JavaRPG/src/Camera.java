/*
 * RPG Game Engine
 * Author: Lachlan Grant
 */

import org.newdawn.slick.SlickException;

/** Represents the camera that controls our viewpoint.
 */
public class Camera
{
    /** Camera variables
     * @param unitFollow The unit that the camera is following
     * @param xPos The current x position of the camera, in pixels relative to the map
     * @param yPos The current y position of the camera, in pixels relative to the map
     * @param tileSize The constant size of each tile in pixels
     */
    private Player unitFollow;
    private double xPos;
    private double yPos;
    private final int tileSize;

    /** Create a new World object. */
    public Camera(Player player, int tileSize)
    {
    	/** Define which player to follow */
    	this.unitFollow = player;
    	/** Define the tile size of the camera */
    	this.tileSize = tileSize;
    	/** Define the x and y positions of the Camera */
    	this.xPos = unitFollow.getXPos();
    	this.yPos = unitFollow.getYPos();
    }

    /** Update the game camera to re-center it's viewpoint around the player
     */
    public void update()
    throws SlickException
    {
    	this.xPos = unitFollow.getXPos();
    	this.yPos = unitFollow.getYPos();
    }

    /* Getters and setters for camera position */
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

    /** Returns the minimum x value on screen
     */
    public double getMinX() {
        return xPos - RPG.screenwidth/2;
    }

    /** Returns the maximum x value on screen
     */
    public double getMaxX() {
        return xPos + RPG.screenwidth/2;
    }

    /** Returns the minimum y value on screen
     */
    public double getMinY() {
    	return yPos - RPG.screenheight/2;
    }

    /** Returns the maximum y value on screen
     */
    public double getMaxY() {
        return yPos + RPG.screenheight/2;
    }

    /** Returns the starting map pixels to render
     */
    public int getStartingXPixel() {
    	return -((int)(getMinX())%tileSize);
    }

    public int getStartingYPixel() {
    	return -((int)(getMinY())%tileSize);
    }

    /** Returns the starting X tile in the camera
     */
    public int getStartTileX() {
    	return (int)(getMinX()/tileSize);
    }
    /** Returns the starting Y tile in the camera
     */
    public int getStartTileY() {
    	return (int)(getMinY()/tileSize);
    }

    /** Tells the camera to follow a given unit.
     */
    public void followUnit(Player unitFollow)
    throws SlickException
    {
    	this.unitFollow = unitFollow;
    }
}
