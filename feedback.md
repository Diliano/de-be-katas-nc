# Feedback

### Testing
I'm seeing a lot of 'returns' in your tests - remember that you are testing the behaviours rather than the return value. This will ensure that you are focusing on what is the function is supposed to be doing. 

I think perhaps your test suite contains too many tests for Exceptions - primarily because they aren't quite necessary for this unit testing - it's fine to take the 'happy path' only rule for unit testing. _Integration_ testing is where you would check whether the user has done something incorrectly or not, because a user would never have access straight to a function.

### Solutions
You've clearly incremented and followed TDD, as I can see where you've used a guard clause at the start of your function. I'd like to emphasise the importance of refactoring to remove clauses like this that no longer _need_ to be in your code. Have a look at how you could trim down `sum_consecutive_duplicates` :) 


### Overall

Great work again from you. When you return to these katas, it wouldbe great to see you refactoring some of your code - you have full test suites, so it would be nice to see katas refactored and reimplemented.
