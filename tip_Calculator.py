print("________TIP-CALCULATOR_________")

def tipCalculate():
    billAmount=float(input("Enter the bill Amount: "))
    tipPercentage=float(input("Enter the tip percentage: "))
    noOfPeoples=int(input("Enter the no. of persons: "))
    print("")
    print("______Bill Details________ ")
    bill="Bill Amount : {}"
    print(bill.format(billAmount))
    
    tipPercent="Tip Percentage : {}"
    print(tipPercent.format(tipPercentage))

    peoples="No. of Peoples : {}"
    print(peoples.format(noOfPeoples))
    
    tip=tipPercentage/100
    totalTip=billAmount*tip
    totalAmount=billAmount+totalTip
    totalPerPerson=round((totalAmount/noOfPeoples),2)

    total="Total Amount: {}"
    print(total.format(totalAmount))

    totalForEach="Total per person: {}"
    print(totalForEach.format(totalPerPerson))

tipCalculate()   