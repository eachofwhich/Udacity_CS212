"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating 
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    >>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

"""


class Bowling:


    def __init__(self):
        pass



    def play(self, balls):
        self._total_score = 0
        self._current_frame = 1
        self._ball_index = 0
        self._bonus_map = dict((ball, 0) for ball in xrange(len(balls)))


        while balls:
            self._play_frame(balls)

        return self._total_score




    def _play_frame(self, balls):
        this_frame = self._current_frame
        ball_count = 0
        balls_left = 3 if this_frame is 10 else 2
        current_score = 0


        while balls_left and balls:

            this_ball = balls.pop(0)
            balls_left -= 1
            ball_count += 1


            self._add_bonuses(this_ball)

            # 10 score on first ball.
            if this_ball is 10 and ball_count is 1:

                current_score = 10

                if this_frame is not 10:
                    self._bonus_map[self._ball_index + 1] += 1
                    self._bonus_map[self._ball_index + 2] += 1
                    balls_left = 0


            else:

                if ball_count is 1:
                    current_score += this_ball

                else:
                    current_score += this_ball

                    # Spare
                    if self._current_frame is not 10:
                        if current_score >= 10:
                            current_score = 10
                            if this_frame is not 10:
                                self._bonus_map[self._ball_index + 1] += 1


            self._ball_index += 1



        self._total_score += current_score
        self._current_frame += 1

        # print 'Frame: {}, Total: {}, Ball Index: {} Bonus Q: {}, Current: {}'.format(
            # this_frame, self._total_score, self._ball_index, self._bonus_map, current_score)



    def _add_bonuses(self, ball):
        """Add all bonuses of the current ball."""
        while self._bonus_map[self._ball_index]:
            self._bonus_map[self._ball_index] -= 1
            self._total_score += ball





def bowling(balls):
    "Compute the total score for a player's game of bowling."

    bowl = Bowling()
    return bowl.play(balls)



            



 






def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)

    result = bowling([9,1] * 10 + [9])
    assert 190 == result, result

    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])

   

def test():
    
    balls = [8, 2, 7, 1]
    result = bowling(balls)
    assert result == 25, 'Failed: {} != {}'.format(result, 25)

    balls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    result = bowling(balls)
    assert result == 300, 'Failed: {} != {}'.format(result, 300)

    test_bowling()


    print 'All good.'



test()