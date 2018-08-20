
def is_valid_play(play, curr_trick, hand):
    
    if curr_trick:
        lead_suit=curr_trick[0][1]
        if play[1]==lead_suit:
            return True
        
        else:
            for card in hand:
                if card[1]==lead_suit:
                    return False
    else:
        return True
        
    
