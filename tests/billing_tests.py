import unittest

class BillingTests(unittest.TestCase):    
   '''
    def assertEvaluate(self, secret: list, guess: list, wellplaced: int, misplaced: int, message: str):
        mastermind = MastermindGame()      
        self.assertEqual(mastermind.guess(secret, guess), GuessResult(wellplaced, misplaced), message)
        
    def testEvalute(self):
        self.assertEvaluate(['blue'], ['red'], 0, 0, 'test one secret color one bad guess')
        self.assertEvaluate(['blue'], ['blue'], 1, 0, 'test one secret color one correct guess')
        self.assertEvaluate(['blue', 'red'], ['black', 'red'], 1, 0, 'test two secret colors one correct guess')    
        self.assertEvaluate(['blue', 'red'], ['blue', 'red'], 2, 0, 'test two secret colors two correct guesses')
        self.assertEvaluate(['blue', 'red'], ['green', 'blue'], 0, 1, 'test two secret colors one misplaced guess')
        self.assertEvaluate(['yellow', 'blue', 'green', 'red'], ['green', 'blue', 'yellow', 'red'], 2, 2, 'two correct guesses two misplaced')
        self.assertEvaluate(['yellow', 'yellow', 'black', 'green', 'yellow'], ['yellow', 'yellow', 'green', 'yellow', 'yellow'], 3, 1, 'complex test case')

'''
if __name__ =='__main__':
    unittest.main()