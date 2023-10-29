#compare list
# == , is
#== comparing value or element same or not
#is comparing memory location same or not
name1=['anik','adnan']
name2=['anik','biswas']
name3=['anik','adnan']
print(name1 == name2) #false
print(name1 == name3) #ture
print(name1 is name3) #false because memory location is not same
#so always use == comparing list value