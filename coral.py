while True:
  print("Do you want to turn on your location?\n ")
  ask_usr = input('(1) Yes \t or \t (0) No : ')
  if ask_usr == '1' :
    print ('\n You got a message')
    s_y=input("\n Wanna open it?\n (1) Yes\tor\t (0) No :  ")
    if s_y=='1':
      print("\nEnter your option to know the details about ''Coral Reefs''-->")
      t_u=(input("\n (1) Present Condition of Coral Reefs\n (2) What we have to do? \n\n Enter your choice : "))
      if t_u=='1':
        print("")
        r_u=(input("1. The Pacific Ocean\n2. The Indian Ocean\n3. The Caribbean Sea\n4. The Red Sea\n5. The Persian Gulf\n\n Enter your choice :  "))
        if r_u=='1':
          print("\n==> In December 2014 wide spread coral bleaching was reported for the Marshall Islands, Guam, Northern Mariana Islands, The North West Hawaiian Islands and Kiribati potentially causing wide-spread coralmortalities in these regions. Coral bleaching occurs when stressed corals expel their zooxanthellae(Symbiptic algae that give corals give their distictive corals colors) resulting in the white coral skeleton being exposed.While bleached, corals are susceptible to damage and prolonged bleaching can result in the death of the coral.For example, in 2005 co bleaching was responsible for loss of half of the corals in the US's Caribbean waters.   ")
          break
        elif r_u=='2':
          print("\n==> Reefs in the Chagos Archipelago, central Indian Ocean, suffered severe bleaching and mortality in 2015 following a7.5 maximum degree heating weeks (DHWs) thermal anomaly, causing a 60% coral cover decrease from 30% cover in 2012 to 12% in April 2016.Mortality was taxon specific, with Porites becoming the dominant coral genus post-bleaching because of an 86% decline in Acroporafrom 14 to 2% cover. Spatial heterogeneity in Acropora mortality across the Archipelago was significantly negativelycorrelated with variation in DHWs and with chlorophyll-a concentrations.In 2016, a 17.6 maximum DHWs thermal anomaly caused further damage, with 68% of remaining corals bleaching in May 2016,and coral cover further declining by 29% at Peros Banhos Atoll (northern Chagos Archipelago)from 14% in March 2016 to 10% in April 2017. We therefore document back-to-back coral bleaching and mortality events for two successive years in the remote central Indian Ocean")
          break
        elif r_u=='3':
          print("\n==> A new study, published Feb. 20 in the journal Proceedings of the Royal Society B, uses environmental, socioeconomic and management data from 30 Caribbean islands to identify which communities may be most at risk from the social and ecological effects of coral bleaching, which occurs when warm water causes coral polyps to expel algae living in their tissues, resulting in the corals turning white.")
          break
        elif r_u == '4':
          print("\n==> In the Gulf of Aqaba/Eilat, the situation seems to be somewhat different: research has shown that the coral reefs of the northern Red Sea are unusually resilient to climatic changes, and are likely to survive even harsher conditions in the future. Israeli scientists agree the coral reef of Eilat, the northernmost coral reef in the world, is unique and needs to be protected and preserved.Recently, it was found that the northern Red Sea corals are not only adaptable to changing environmental conditions but also continue to produce offspring at the same rate and quality, which could ensure reef survival for many years to come, provided we humans do not interfere.")
          break
        elif r_u =="5":
          print("\n==> In Kish Island, where coral reefs are more exposed to temperature rise due to gentle slopes of the reefs corals are more exposed to bleaching while in Faror and Khark Islands it is less likely for the corals to lose color.Some species of corals are adapted to the new climatic conditions, but others, such as staghorn corals, are not as adaptable and are dying, ISNA news agency quoted Rezaei as saying on May 6.In the year 1378 (March 1999-March 2000) only 23 percent of the corals in Shidvar Island were alive and currently the amount decreased to 13 percent, he regretted, adding that staghorn corals are totally extinct in the area")
          break
        else :
          print("\nWrong Input!! Please Try again using option 1 to 5..\n\tLocation turned off\n")


      elif t_u=='2':
        print ('\n♦ Use mineral sunscreen\n♦ Avoid organic sunscreen\n♦ Use Ultraviolate Protection Factor (UPF) Sun wear')
        break
      else:
        print("\nWrong Input!! Please Try again using 1 or 2\n\tLocation turned off\n")
        

      
    elif s_y == '0':
      print('\nLocation turned off and Notification closed successfully.\n\tHave a nice day!')
      break
    else:
      print("\nWrong Input!! Please Try again using 1 or 0\nLocation turned off\n")
      
     
     
			
			
	
  
  elif ask_usr == '0':
    print ('\n\tHave a nice day!')
    
    break
  else :
    print("\nWrong Input!! Please Try again using 1 or 0\n")
