#counties=['Arapahoe','Denver','Jefferson']
#if counties[1]=='Denver':
#    print(counties[1])


counties=["Arapahoe","Denver","Jefferson"]

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is NOT the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")


#get KEYS in a dictionary
#for county in counties:
#    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#    print(county)

#for county in counties_dict.keys():
#    print(county)

#for county in counties:
#    print(county)


#get VALUES in a dictionary
#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])

#or county in counties_dict:
#    print(counties_dict.get(county))


#get key value pairs of a dictionary
#for county, voters in counties_dict.items():
#    print(county, voters)

#for county in counties_dict:
#   print(county + " county has " + str(counties_dict[county]) + " registered voters.")
#    print(county + " county has " + str(counties_dict.get(county)) + " registered voters.")
for county, voters in counties_dict:
        print(county + " county has " + voters + " registered voters.")