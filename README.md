# 2022Fall_projects

# Monte Carlo Simulation<br>
Atlantic Coastline Fishing<br>
![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/FishGraph.png)

## Background<br>
* The Atlantic Ocean coastline has rich fishery resources<br>
* Good quality dataset to explore (Published by NOAA)<br>
* Fishing simulation is a compelling topic<br>
Link to dataset download https://www.fisheries.noaa.gov/recreational-fishing-data/recreational-fishing-data-downloads<br>

NOAA Fish-Level Dataset<br>
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/DataSet.png" width="512" height="455">
* Fish-level Length and Weight Dataset includes fish-level length and weight data and variables required for estimation. <br>
* Gathered by the Access Point Angler Intercept Survey.<br>
* Used columns are year, common, length, weight, and date. <br>

## Project Scenario<br>
1.The average fish length in winter is greater than the fish caught in summer.<br>
2.Based on simulation of fish vary varieties in north, mid, south area of Atlantic and Gulf Mexico area respectively, simulate further about fishing strategy. <br>
3.The use of lures will affect the abundant of fish species and structure of fish caught<br>

### Scenario-1<br>

* The average fish length in winter is greater than the fish caught in summer.<br>
* Set fish stats (common, lgth, wgt) based on different season.<br>
* Winter: Jan 1 to Mar 31<br>
* Summer: Jul1 to Sep 30<br>
Run the simulation for 1000 times<br>
![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Sceniro1.png)<br><img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Scenario1.1.png" width="500" height="250">





### Scenario-2<br>
* If you wanna More Species in a long-trip<br>
4   = North Atlantic (ME; NH; MA; RI; CT) <br>
5   = Mid-Atlantic (NY; NJ; DE; MD; VA) <br>
6   = South Atlantic (NC; SC; GA; EFL)<br>
7   = Gulf of Mexico (WFL; AL; MS; LA) <br>
8   = West Pacific (HI)<br>
11 = U. S. Caribbean (Puerto Rico and Virgin Islands<br>
![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Scenario2.png)<br>

### Scenario-3<br>
* Species richness can be affected by the use of superior baits<br>
* Each fish has a chance of catching with normal bait<br>
* Premium baits increase the chance of catching some fish<br>

#### The base probability of the fish caught<br>
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Base%20Probability%20.png)<br> -->
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Base%20Probability%20.png" height="455">


#### Changes in fish species
* Catch 100 fish at a time and check out the different species
* Loop 100 times
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/NoLure_abundant.png)<br> -->
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/NoLure_abundant.png" height="455">


#### Average change in fish species<br>
* The average species per 100 times<br>
* Loop 20 times to see the change<br>
* Three different kinds of bait<br>
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Bait_abundant.png)<br> -->
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Bait_abundant.png" width="565" height="415">


#### Changes in the number of fish structures<br>
The common fish with a high probability changed more, and the rare fish changed less<br>
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Bait_structure.png)<br> -->
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Bait_structure.png" height="455">












