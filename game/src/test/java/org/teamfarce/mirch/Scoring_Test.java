package org.teamfarce.mirch;

import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.assertEquals;

/**
 * Tests for scoring
 */
public class Scoring_Test extends GameTest {
    
    GameSnapshot gameSnapshot;
    
    @Before
    public void init_tests()
    {
        
        gameSnapshot = new GameSnapshot(null, null, null, 0, 0);
        
    }
    
    
    @Test
    public void test_modifyScore_Addition(){
        int currentScore;
        int inc = 20;
        int newScore;
        currentScore = gameSnapshot.getScore();
        gameSnapshot.modifyScore(inc);
        newScore = gameSnapshot.getScore();
        assertEquals(newScore, currentScore + inc);
    }

    @Test
    public void test_modifyScore_Subtraction(){
        int currentScore;
        int inc = -20;
        int newScore;
        currentScore = gameSnapshot.getScore();
        gameSnapshot.modifyScore(inc);
        newScore = gameSnapshot.getScore();
        assertEquals(newScore, currentScore - inc);
    }

    @Test
    public void test_updateScore_no_decrease(){
        int currentScore;
        float delta = 0.25f;
        int newScore;
        currentScore = gameSnapshot.getScore();
        gameSnapshot.updateScore(delta);
        newScore = gameSnapshot.getScore();
        assertEquals(newScore, currentScore);
    }

    @Test
    public void test_updateScore_has_decrease(){
        int currentScore;
        float delta = 1.00f;
        int newScore;
        currentScore = gameSnapshot.getScore();
        gameSnapshot.updateScore(delta);
        newScore = gameSnapshot.getScore();
        assertEquals(newScore, currentScore - 1);
    }
}
