# 2022Fall_projects

# Fishing Monte Carlo Simulation<br>
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

## Scenario-1<br>

* The average fish length in winter is greater than the fish caught in summer.<br>
* Set fish stats (common, lgth, wgt) based on different season.<br>
* Winter: Jan 1 to Mar 31<br>
* Summer: Jul1 to Sep 30<br>
Run the simulation for 1000 times<br>
![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Sceniro1.png)<br><img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Scenario1.1.png" width="500" height="250">

## Conclusion
* Average length for fish caught in winter is 439.08mm <br>
* Average length for fish caught in summer is 426.76mm <br>
* Winter is the winner.<br>
* According to the simulation result, hypothesis 1 is verified.<br>
#### The output dataframe and final result is written to record.txt file.





## Scenario-2<br>
### If you wanna More Species in a long-trip<br>
### Assumption:
1. fish distribution vary in different regions(with vary appear probability) <br>
2. angler can catch fish in each laying rod <br>
3. angler took trip in single area <br>
#### Running simulation of single region fishing for 500 times<br>
#### region:<br>
4   = North Atlantic (ME; NH; MA; RI; CT) <br>
5   = Mid-Atlantic (NY; NJ; DE; MD; VA) <br>
6   = South Atlantic (NC; SC; GA; EFL)<br>
7   = Gulf of Mexico (WFL; AL; MS; LA) <br>
8   = West Pacific (HI)<br>
11 = U. S. Caribbean (Puerto Rico and Virgin Islands<br>
![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Scenario2.png)<br>

### Results: The South Atlantic-region6 has the most species <br>
then the Gulf of Mexico - region 7, the Mid-Atlantic - region 5, and the North Atlantic - region 4 has the fewest. <br>
The total species is 38.(After filtering the prob < 0.5%) <br>

Based on Results of simulation of single region fishing trip:  <br>
New Assumption: <br>

* fish distribution vary in different regions(with vary appear probability) <br>
* angler can catch fish in each laying rod <br>
* angler took trip for more species(35) only in region 5, region 6 and region 7 (because the three regions can cover the number 35) <br>

#### Running simulation of single region fishing for unknown times <br>
[INSERT PIC] <br>
#### Conclusion: There should be the shortest time in printing lines. Which around 180 times, with the times in each region separately. <br>
## Scenario-3<br>
### Effects of different baits on species richness and structural number of fishing
* According to probability, all fish are divided into three categories: rare (47 species), advanced (46 species), and common (46 species).<br>
* There are three types of bait, no-bait, shrimp (regular bait), mackerel (premium bait)<br>
* Shrimp (normal bait) can raise rare fish probability to advanced fish probability<br>
* mackerel (premium bait) can raise the probability of rare fish to common fish probability<br>

#### The base probability of the fish caught<br>
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/Base%20Probability%20.png)<br> -->
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Base%20Probability%20.png" height="455">


#### Changes in fish species
* Catch 100 fish at a time and check out the different species
* Loop 100 times
<!-- ![image](https://github.com/yibow5/2022Fall_projects/blob/main/Images/NoLure_abundant.png)<br> -->
### No bait abundant <br>
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/NoLure_abundant.png" height="455"> <br>
### Shrimp abundant  <br>
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Shrimp_abundant.png" height="455"> <br>
### Mackerel abundant<br>
<img src="https://github.com/yibow5/2022Fall_projects/blob/main/Images/Mackerel_abundant.png" height="455"><br>



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

## Conclusion
* The variability that can arise in a sampling program using different types of baits. A total of 139 fish species were recorded. Fish assemblage structure and richness varied significantly between different baits.<br>
* In terms of richness, the improvement of premium bait (mackerel) is the most obvious, with 57 different species in 100 fish, followed by common bait (shrimp), with an average of 44 different species in 100 fish.<br>
* For the structure change of fish quantity, premium bait or common bait has little effect on rare fish, but the structure change of common fish is larger. It is speculated that because the probability of rare fish and high-level fish increases, they are easier to be caught When it arrives, the number of common fish will be relatively reduced.











