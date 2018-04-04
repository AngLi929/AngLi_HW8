import Parameters as P
import HW6Classes as Cls
import SupportSteadyState as Support

cohortFair = Cls.SetOfGames(
    id=1,
    prob_head=P.Prob_Head,
    n_games=P.SIM_Game)
# simulate the cohort
FairOutcome = cohortFair.simulation()


cohortUnfair = Cls.SetOfGames(
    id=2,
    prob_head=P.Prob_Head_Unfair,
    n_games=P.SIM_Game)
# simulate the cohort
UnfairOutcome = cohortUnfair.simulation()

# print comparative outcomes
Support.print_comparative_outcomes(UnfairOutcome, FairOutcome)