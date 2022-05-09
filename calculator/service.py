from calculator.apps import CalculatorConfig
from taxinfo.models import Taxinfo
# taxAmounts = [350000,100000,200000,1350000]
# taxRates = [1, 10, 20, 30, 36]
def get_tax_info(marital_status = 'S'):
    taxAmounts = []
    taxRates = []
    if marital_status == 'M':
        records = CalculatorConfig.taxInfoMarried
    else:
        records = CalculatorConfig.taxInfoSingle
    for record in records:
        taxRates.append(record.taxRate)
        taxAmounts.append(record.taxableIncome)
    return taxAmounts, taxRates

def apply_tax_rates(amount,marital_status = 'S'):
    taxAmounts, taxRates = get_tax_info(marital_status)
    taxes =[]
    for i in range(len(taxAmounts)-1):
        remaining = amount - taxAmounts[i]
        if remaining <= 0:
            tax = (amount*taxRates[i])/100
            taxes.append(tax)
            amount = 0
            break
        else:
            tax = (taxAmounts[i]*taxRates[i])/100
            taxes.append(tax)
            amount = remaining
    if amount > 0:
        tax = (amount*taxRates[-1])/100
        taxes.append(tax)
    total_tax = 0
    for tax in taxes:
        total_tax += tax
    return total_tax, taxes


def calculate_tax(model,marital_status = 'S'):
    allIncome=(model.monthlySalary*12 +
               model.housingRentAllowance*12 +
               model.costOfLivingAllowance*12 +
               model.transportationAllowance*12 +
               model.bonus +
               model.overTimePayment)
    allDed= model.medicalInsurance+model.lifeInsurance
    taxableIncome = allIncome - allDed
    print(allIncome)
    print(allDed)
    print(taxableIncome)
    total, taxes = apply_tax_rates(taxableIncome,marital_status)
    print(taxes)
    return total
