aVro=int(input("Do you want to turn on your location?\n (1) Yes\tor\t (0) No : "))

if aVro==1:
	print("\nYou got a notification")
	s_y=int(input("\n Wanna click on the notification?\n (1) Yes\tor\t (0) No:  "))
	if s_y==1:
		print("\nEnter your option to know the details about ''Coral Reefs''-->")
		t_u=int(input("\n (1) Present Condition of Coral Reefs\n (2) What we have to do? \n Enter your choose : "))
		if t_u==1:
			print("")
			r_u=int(input("1. The Pacific Ocean\n2 . The Indian Ocean\n3 . The Caribbean Sea\n4. The Red Sea\n5 . The Persian Gulf\n Enter your choose :  "))
			if r_u==1:
				print("\n==> In December 2014 wide spread coral bleaching was reported for the Marshall Islands, Guam, Northern Mariana Islands, The North West Hawaiian Islands and Kiribati potentially causing wide-spread coralmortalities in these regions. Coral bleaching occurs when stressed corals expel their zooxanthellae(Symbiptic algae that give corals give their distictive corals colors) resulting in the white coral skeleton being exposed.While bleached, corals are susceptible to damage and prolonged bleaching can result in the death of the coral.For example, in 2005 co bleaching was responsible for loss of half of the corals in the US's Caribbean waters.   ")
			elif r_u==2:
				print("\n==> Reefs in the Chagos Archipelago, central Indian Ocean, suffered severe bleaching and mortality in 2015 following a7.5 maximum degree heating weeks (DHWs) thermal anomaly, causing a 60% coral cover decrease from 30% cover in 2012 to 12% in April 2016.Mortality was taxon specific, with Porites becoming the dominant coral genus post-bleaching because of an 86% decline in Acroporafrom 14 to 2% cover. Spatial heterogeneity in Acropora mortality across the Archipelago was significantly negativelycorrelated with variation in DHWs and with chlorophyll-a concentrations.In 2016, a 17.6 maximum DHWs thermal anomaly caused further damage, with 68% of remaining corals bleaching in May 2016,and coral cover further declining by 29% at Peros Banhos Atoll (northern Chagos Archipelago)from 14% in March 2016 to 10% in April 2017. We therefore document back-to-back coral bleaching and mortality events for two successive years in the remote central Indian Ocean")
			elif r_u==3:
				print("\n==> A new study, published Feb. 20 in the journal Proceedings of the Royal Society B, uses environmental, socioeconomic and management data from 30 Caribbean islands to identify which communities may be most at risk from the social and ecological effects of coral bleaching, which occurs when warm water causes coral polyps to expel algae living in their tissues, resulting in the corals turning white.")
			elif r_u==4:
				print("\n==> In the Gulf of Aqaba/Eilat, the situation seems to be somewhat different: research has shown that the coral reefs of the northern Red Sea are unusually resilient to climatic changes, and are likely to survive even harsher conditions in the future. Israeli scientists agree the coral reef of Eilat, the northernmost coral reef in the world, is unique and needs to be protected and preserved.Recently, it was found that the northern Red Sea corals are not only adaptable to changing environmental conditions but also continue to produce offspring at the same rate and quality, which could ensure reef survival for many years to come, provided we humans do not interfere.")
			elif r_u==5:
				print("\n==> In Kish Island, where coral reefs are more exposed to temperature rise due to gentle slopes of the reefs corals are more exposed to bleaching while in Faror and Khark Islands")
			
			
		else:
			print("\n♦Use mineral sunscreen\n♦Avoid organic sunscreen\n♦Use Ultraviolate Protection Factor (UPF) Sun wear")
		
	else:
		print("\nOk\nHave a nice day!")
	
else:
	print("\nOk\nHave a nice day!")
	
