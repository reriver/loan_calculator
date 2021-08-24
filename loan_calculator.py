import math
import sys

args_dict = {}
n = len(sys.argv)

for i in range(1, n):
    a = sys.argv[i].split("=")
    if a[0] not in args_dict.keys():
        args_dict[a[0]] = a[1]
    else:
        print("Incorrect parameters: argument duplication")
        exit()

# check if no type specified
if '--type' not in args_dict.keys():
    print("Incorrect parameters no type")
    exit()

# check if no interest specified
if '--interest' not in args_dict.keys():
    print("Incorrect parameters no interest")
    exit()

interest_year = float(args_dict['--interest'])
# print('interest year', interest_year)
month_interest = interest_year / (12 * 100)

if args_dict['--type'] == 'diff':
    # --type=diff

    # principal for diff not allowed
    if '--principal' not in args_dict.keys():
        print("Incorrect parameters: no principal")
        exit()
    principal = int(args_dict['--principal'])
    # print('principal', principal)

    if '--periods' not in args_dict.keys() and '--payment' in args_dict.keys():
        payment = float(args_dict['--payment'])
        print('payment', payment)
        # input --interest
        # input --principal
        # input --payment
        # output --periods
        print("diff periods")
        diff_payment = 0

    elif '--payment' not in args_dict.keys() and '--periods' in args_dict.keys():
        periods = int(args_dict['--periods'])
        # print('periods', periods)
        # input --interest
        # input --principal
        # input --periods
        # output --payment
        principal_interest = 0
        for i in range(1, periods + 1):
            diff_payment = math.ceil(principal / periods + month_interest * (principal - ((principal * (i - 1)) / periods)))
            principal_interest += diff_payment
            print("Month", i, ": payment is", diff_payment)
        print("\nOverpayment =", principal_interest - principal)


elif args_dict['--type'] == 'annuity':
    # --type=annuity

    if '--periods' not in args_dict.keys() and '--principal' in args_dict.keys() and '--payment' in args_dict.keys():
        principal = int(args_dict['--principal'])
        # print('principal', principal)
        payment = float(args_dict['--payment'])
        # print('payment', payment)
        # input --interest
        # input --principal
        # input --payment
        # output --periods
        periods = math.log(payment / (payment - month_interest * principal), 1.0 + month_interest)
        years = int(math.ceil(periods) / 12)
        months_remains = math.ceil(periods - years * 12)
        # print('years', years)
        # print('months_remains', months_remains)

        if months_remains == 0:
            print('It will take', years, 'years to repay this loan!')
        else:
            print('It will take', years, 'years and', months_remains, 'months to repay this loan!')
        principal_interest = int(math.ceil(periods) * math.ceil(payment))
        # print('principal_interest', principal_interest)
        print("Overpayment = ", math.ceil(principal_interest - principal))

    elif '--payment' not in args_dict.keys() and '--principal' in args_dict.keys() and '--periods' in args_dict.keys():
        principal = int(args_dict['--principal'])
        # print('principal', principal)
        periods = int(args_dict['--periods'])
        # print('periods', periods)
        # input --interest
        # input --principal
        # input --periods
        # output --payment
        power_cached = math.pow(1 + month_interest, periods)
        payment = principal * (month_interest * power_cached) / (power_cached - 1)
        print('Your monthly payment = {}!'.format(math.ceil(payment)))
        principal_interest = int(periods * math.ceil(payment))
        print("Overpayment = ", math.ceil(principal_interest - principal))

    elif '--principal' not in args_dict.keys() and '--payment' in args_dict.keys() and '--periods' in args_dict.keys():
        payment = int(args_dict['--payment'])
        # print('payment', payment)
        periods = int(args_dict['--periods'])
        # print('periods', periods)
        # input --interest
        # input --payment
        # input --periods
        # output --principal
        power_cached = math.pow(1.0 + month_interest, periods)
        pow_1 = power_cached - 1.0
        up_cached = payment * pow_1
        down_cache = month_interest * power_cached
        principal = up_cached / down_cache
        print("Your loan principal = %i!" % principal)
        principal_interest = int(periods * math.ceil(payment))
        print("Overpayment = ", math.ceil(principal_interest - principal))

    else:
        print("annuity: Incorrect parameters")
        exit()

elif args_dict['--type'] != 'annuity' and args_dict['--type'] != 'diff':
    print("Incorrect parameters: unknown type")
    exit()
    # unknown --type

