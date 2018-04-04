import Parameters as P
import HW6Classes as Cls
import SupportTransientState as Support

multiCohortFair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),
    prob_head=P.Prob_Head,
    n_games_in_a_set=P.REAL_Game_SIZE)

# simulate all cohorts
multiCohortFair.simulation()


multiCohortUnfair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    prob_head=P.Prob_Head_Unfair,
    n_games_in_a_set=P.REAL_Game_SIZE)

# simulate all cohorts
multiCohortUnfair.simulation()

# print comparative outcomes
Support.print_comparative_outcomes(multiCohortUnfair, multiCohortFair)