import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_comparative_outcomes(sim_output_unfair, sim_output_fair):

    increase = Stat.DifferenceStatIndp(
        name='Increase in rewards',
        x=sim_output_unfair.get_rewards(),
        y_ref=sim_output_fair.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average increase in reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in rewards',
        x=sim_output_unfair.get_rewards(),
        y_ref=sim_output_fair.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage increase in reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)