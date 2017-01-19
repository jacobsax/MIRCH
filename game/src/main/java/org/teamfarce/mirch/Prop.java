package org.teamfarce.mirch;

import java.util.ArrayList;

import com.badlogic.gdx.math.Vector2;

/**
 * Creates an individual prop entity, extends from the MapEntity class.
 *
 * @author Jacob Wunwin
 */
public class Prop extends MapEntity {
    ArrayList<Clue> clue;
    Vector2 roomPosition;
    Room currentRoom;

    /**
     * Initialises the object.
     */
    Prop(String filename, Room room, Vector2 position) {
    	this.roomPosition = position;
    	this.currentRoom = room;
    	this.filename = filename;
    }

    /**
     * Returns a Clue ArrayList of all clues attached to this prop.
     *
     * @return The list of clues
     */
    ArrayList<Clue> takeClue() {
        return this.clue;
    }
}

