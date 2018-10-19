print("This program will calculate total rainfall and average")
print("monthly rainfall for a period of  one year.")

jan = int(input("How much rain fell during the month of January?"))
feb = int(input("How much rain fell during the month of February?"))
march = int(input("How much rain fell during the month of March?"))
april = int(input("How much rain fell during the month of April?"))
may = int(input("How much rain fell during the month of May?"))
june = int(input("How much rain fell during the month of June?"))
july = int(input("How much rain fell during the month of July?"))
aug = int(input("How much rain fell during the month of August?"))
sep = int(input("How much rain fell during the month of September?"))
octo = int(input("How much rain fell during the month of October?"))
nov = int(input("How much rain fell during the month of November?"))
dec = int(input("How much rain fell during the month of December"))
list_of_months = [['January', jan], ['Febuary', feb], ['March', march], ['April', april], ['May', may], ['June', june], ['July', july], ['August', aug], ['September', sep], ['October', octo], ['Novemeber', nov], ['December', dec]]
total = jan + feb + march + april + may + june + july + aug + sep + octo + nov + dec
print('The total rainfall for the year was', total, "inches")
month_list = [jan, feb, march, april, may, june, july, aug, sep, oct, nov, dec]
print('the average rainfall was', (total / len(month_list)), 'inches.')
print('The maximum rainfall was', max(list_of_months), 'inches.')
print('The minimum rainfall was', min(list_of_months), 'inches.')
