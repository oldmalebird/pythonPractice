
def realAnnualizedReturn(nominalPricipal, couponRate, month, nominalAnnualizedReturn):
    '''
    realPricipal：实际本金 = 名义本金 * （ 1 - 代金券抵扣比例 ）
    realInterest：实际利息 = 名义本金 * 名义年化收益率 / 12 * 投资周期（月）
    realReturn: 实际收益 = 代金券抵扣金额 + 实际利息
    realAnnualizedReturn：实际年化收益率 = 实际收益 / 实际本金 / month * 12

    month：投资周期，以月为单位

    couponRate：代金券抵扣比例
    couponValue: 代金券金额 = 名义本金 * 代金券抵扣比例

    nominalPricipal：名义本金
    nominalAnnualizedReturn：名义年化收益率
    '''
    couponValue = nominalPricipal * couponRate
    realPricipal = nominalPricipal * (1 - couponRate)
    realInterest = month / 12 * nominalPricipal * nominalAnnualizedReturn
    realReturn = couponValue + realInterest
    realAnnualizedReturn = realReturn / realPricipal / month * 12
    print('名义本金：', nominalPricipal)
    print('代金券抵扣比例:', couponRate * 100, '%')
    print('投资周期:', month, '个月')
    print('名义年化收益率:', nominalAnnualizedReturn * 100, '%')
    print('代金券抵扣金额:', couponValue)
    print('实际本金:', realPricipal)
    print('实际利息:', realInterest)
    print('实际收益 = 代金券抵扣金额 + 实际利息:', realReturn)
    print('实际年化收益率:', realAnnualizedReturn * 100, '%')
    print(' ')

realAnnualizedReturn(10000, 0.01, 12, 0.115)
realAnnualizedReturn(10000, 0.01, 12, 0.125)
realAnnualizedReturn(10000, 0.005, 12, 0.115)
realAnnualizedReturn(10000, 0.005, 12, 0.125)

realAnnualizedReturn(10000, 0.01, 12, 0.135)
realAnnualizedReturn(10000, 0.01, 12, 0.13)

realAnnualizedReturn(10000, 0.01, 3, 0.085)
realAnnualizedReturn(5000, 0.01, 3, 0.085)

realAnnualizedReturn(15000, 0.0112, 6, 0.1)
realAnnualizedReturn(10000, 0.0112, 6, 0.1)
