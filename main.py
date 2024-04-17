import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):

    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    else:
        if S[0] == T[0]:
            return MED(S[1:], T[1:])
        else:
            return 1 + min(MED(S, T[1:]),  # Insertion
                            MED(S[1:], T),  # Deletion
                            MED(S[1:], T[1:]))  # Substitution

def fast_MED(S, T, memo=None):

    """
    NOTE -> I Renamed my variable MED to memo because I was getting confused
    between whether I was calling the MED function or accessing the memo dict

    I also initialized memo to None initially, then initialize it in the function.
    I did this to simplify function calls

    I did the same in the next function 

    Sorry for any confusion
    """

    #Initialized memo dict (for my implementation)
    if memo is None:
        memo = {}

    #Case 1 -> Solution already computed for this case  
    if (S, T) in memo:
        return memo[(S, T)]
    
    #Case 2 -> S/T is empty
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    
    #Case 3 -> First letters match
    if S[0] == T[0]:
        memo[(S, T)] = fast_MED(S[1:], T[1:], memo)
    
    #Case 4 -> Non-precomputed difference
    else:
        memo[(S, T)] = 1 + min(fast_MED(S, T[1:], memo),  # Insertion
                                fast_MED(S[1:], T, memo),  # Deletion
                                fast_MED(S[1:], T[1:], memo))  # Substitution
    return memo[(S, T)]




