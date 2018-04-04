import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P

def print_comparative_outcomes(multi_cohort_unfair, multi_cohort_fair):

    increase = Stat.DifferenceStatIndp(
        name='Increase in mean reward',
        x=multi_cohort_unfair.get_all_total_rewards(),
        y_ref=multi_cohort_fair.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)