/*
 * RPG Game Engine
 * Author: Lachlan Grant
 */

import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.tiled.TiledMap;

/** Represents the entire game world.
 * (Designed to be instantiated just once for the whole game).
 */
public class World
{
	/** World variables
	 * @param player The player within the game
	 * @param camera The camera that acts as a viewport of the game
	 * @param background The TiledMap object, holding the map
	 **/
	private Player player;
	private Camera camera;
	private TiledMap background;

	/* Define the size of each tile in pixels */
    private static final int tileSize = 72;

	/* Define the rate of movement in pixels */
	private static final double MOVEMENT_RATE = 0.25;

	/* Define the map size */
	private static final int mapSize = 6912;

	/* Define the number of tiles on the screen */
	private static final int NUM_X_TILES = 13;
	private static final int NUM_Y_TILES = 10;

	/* Define initial x and y positions in pixels */
	private static final int INITIAL_XPOS = 756;
	private static final int INITIAL_YPOS = 684;

	/* Create a new World object. */
    public World() throws SlickException
    {
    	/* Create the TiledMap background object */
    	background = new TiledMap("assets/map.tmx", "assets");
    	/* Create the new player with starting coordinates */
    	player = new Player(INITIAL_XPOS, INITIAL_YPOS);
    	/* Create the camera
    	 * The screen dimensions come from RPG
    	 */
    	camera = new Camera(player, tileSize);
    }

    /* Returns the next X Tile */
    public int getNextTileX(double newXPos) {
    	return (int)(newXPos/tileSize);
    }

    /* Returns the next Y Tile */
    public int getNextTileY(double newYPos) {
    	return (int)(newYPos/tileSize);
    }

    /* Returns a boolean on whether or not a tile is available */
    public boolean tileClear(double newXPos, double newYPos) {
    	int tileId;
    	tileId = background.getTileId(getNextTileX(newXPos), getNextTileY(newYPos), 0);
    	return (background.getTileProperty(tileId, "block", "0") == "0");
    }
    /** Update the game state for a frame.
     * @param dir_x The player's movement in the x axis (-1, 0 or 1).
     * @param dir_y The player's movement in the y axis (-1, 0 or 1).
     * @param delta Time passed since last frame (milliseconds).
     */
    public void update(double dir_x, double dir_y, int delta) throws SlickException
    {
    	/* Define the new x and y positions */
    	double newXPos = player.getXPos() + delta*MOVEMENT_RATE*dir_x;
    	double newYPos = player.getYPos() + delta*MOVEMENT_RATE*dir_y;
    	/* Update the players current position*/
    	if(newXPos > 0 && newXPos < mapSize && newYPos > 0 && newYPos < mapSize) {
    		if(tileClear(newXPos, newYPos)) {
            	player.update(newXPos, newYPos);
            }
    	}
        /* Adjust the camera to place the player at the center */
    	camera.update();
    }

    /** Render the entire screen, so it reflects the current game state.
     * @param g The Slick graphics object, used for drawing.
     */
    public void render(Graphics g) throws SlickException
    {
    	/** Render the background
    	 *  The first pair of arguments set the x and y positions on the screen
    	 *  The second pair tell us which tiles on the TiledMap (background) to render
    	 *  The third pair describe the height of each tile
    	 */
    	background.render(camera.getStartingXPixel(), camera.getStartingYPixel(),
    			camera.getStartTileX(), camera.getStartTileY(),
    			NUM_X_TILES, NUM_Y_TILES);
    	/** Draw the player on the screen */
    	player.drawPlayer();
    }
}
