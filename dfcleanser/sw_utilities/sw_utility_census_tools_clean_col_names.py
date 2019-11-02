"""
# sw_utility_census_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue June 6 16:00:00 2019

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_census_model as swcm


from dfcleanser.common.common_utils import (opStatus)

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Social Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def clean_ACS_17_Disability(j,colnames,newcolnames) :
    
    dtype   =   -1
    
    newcolname  =   ""
                    
    if(colnames[j].find("Total; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") >-1 ) :
        newcolname     =   colnames[j].replace("Total; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","population_")
        dtype   =   0
                    
    elif(colnames[j].find("With a disability; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") >-1 ) :
        newcolname     =   colnames[j].replace("With a disability; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","disability_population_")
        dtype   =   1
                        
    elif(colnames[j].find("Percent with a disability; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") >-1 ) :    
        newcolname     =   colnames[j].replace("Percent with a disability; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","disability_population_")
        dtype   =   2
                        
    if(dtype > -1) :
                        
        #print("newcolname",newcolname,dtype)
                        
        if(newcolname.find("White") >-1 ) :
            newcolname     =   newcolname.replace("White","white")   
        elif(newcolname.find("Black or African American ") >-1 ) :    
            newcolname     =   newcolname.replace("Black or African American ","black")
        elif(newcolname.find("American Indian and Alaska Native ") >-1 ) :    
            newcolname     =   newcolname.replace("American Indian and Alaska Native ","native_american_alaskan")
        elif(newcolname.find("Asian ") >-1 ) :    
            newcolname     =   newcolname.replace("Asian ","asian")
        elif(newcolname.find("Native Hawaiian and Other Pacific Islander ") >-1 ) :    
            newcolname     =   newcolname.replace("Native Hawaiian and Other Pacific Islander ","hawaiian_pacific")
        elif(newcolname.find("Some other race  ") >-1 ) :    
            newcolname     =   newcolname.replace("Some other race ","other")
        elif(newcolname.find("Two or more races  ") >-1 ) :    
            newcolname     =   newcolname.replace("Two or more races ","mixed")
        elif(newcolname.find("White alone, not Hispanic or Latino  ") >-1 ) :    
            newcolname     =   newcolname.replace("White alone, not Hispanic or Latino ","white_non_hispanic")
        elif(newcolname.find("Hispanic or Latino (of any race)  ") >-1 ) :    
            newcolname     =   newcolname.replace("Hispanic or Latino (of any race) ","hispanic")
        elif(newcolname.find("Some other race ") >-1 ) :    
            newcolname     =   newcolname.replace("Some other race ","other")
        elif(newcolname.find("Two or more races") >-1 ) :    
            newcolname     =   newcolname.replace("Two or more races","mixed")
                        
        newcolname     =   newcolname.replace(" alone","")
        newcolname     =   newcolname.replace("alone","")
                        
        if(dtype == 2) :
            newcolname     =   newcolname + "_percent" 
        else :
            newcolname     =   newcolname + "_total"
                
        print("newcolname",newcolname,j)
        newcolnames.append(newcolname)

    else :
        
        if(colnames[j].find("Total; Estimate; White alone, not Hispanic or Latino") >-1 ) :
            newcolname     =   "population_white_not_hispanic_total"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
        elif(colnames[j].find("With a disability; Estimate; White alone, not Hispanic or Latino") >-1 ) :
            newcolname     =   "disability_population_white_not_hispanic_total"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
        elif(colnames[j].find("Percent with a disability; Estimate; White alone, not Hispanic or Latino") >-1 ) :
            newcolname     =   "disability_population_white_not_hispanic_percent"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
        elif(colnames[j].find("Total; Estimate; Hispanic or Latino (of any race)") >-1 ) :
            newcolname     =   "population_hispanic_total"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
        elif(colnames[j].find("With a disability; Estimate; Hispanic or Latino (of any race)") >-1 ) :
            newcolname     =   "disability_population_hispanic_total"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
        elif(colnames[j].find("Percent with a disability; Estimate; Hispanic or Latino (of any race)") >-1 ) :
            newcolname     =   "disability_population_hispanic_percent"
            newcolnames.append(newcolname)
            print("newcolname",newcolname,j,3)
    
        elif(colnames[j].find("Estimate; AGE") >-1 ) :  
            dtype   =   3              
            if(colnames[j].find("Total; Estimate; AGE - ") >-1 ) :
                newcolname     =   colnames[j].replace("Total; Estimate; AGE - ","population_age_")
            elif(colnames[j].find("With a disability; Estimate; AGE - ") >-1 ) :    
                newcolname     =   colnames[j].replace("With a disability; Estimate; AGE - ","disability_age_")
                dtype   =   4
            elif(colnames[j].find("Percent with a disability; Estimate; AGE - ") >-1 ) :    
                newcolname     =   colnames[j].replace("Percent with a disability; Estimate; AGE - ","disability_age_")
                dtype   =   5
            
            newcolname     =   newcolname.replace("Under ","under_")
            newcolname     =   newcolname.replace(" to ","_to_")
            
            if(newcolname.find(" years and over") >-1 ) :
                if(dtype == 5) :
                    newcolname     =   newcolname.replace(" years and over","_and_over_years_percent")
                else :
                    newcolname     =   newcolname.replace(" years and over","_and_over_years_total")
            else : 
                if(dtype==5) :
                    newcolname     =   newcolname.replace(" years","_years_percent")
                else :    
                    newcolname     =   newcolname.replace(" years","_years_total")
                    
            print("newcolname",newcolname,j,3)
            newcolnames.append(newcolname)
                         
        else : 
            if(dtype == -1) :
                newcolnames.append(colnames[j])
                print("oldcolname",colnames[j],j)


def clean_ACS_17_Foodstamps(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if( (colnames[j].find("With one or more people in the household 60 years and over") >-1 ) or 
        (colnames[j].find("No people in the household 60 years and over") >-1 ) ):
        
        if(colnames[j].find("With one or more people in the household 60 years and over") >-1 ) :
            h60     =   "with_one_or_more_over_60_"
        else :
            h60     =   "no_people_over_60_"
        
        if(colnames[j].find("Total; Estimate; ") >-1 ) :
            newcolname  =   "households_" + h60 +"total"
        elif(colnames[j].find("Percent; Estimate") >-1 ) :    
            newcolname  =   "households_" + h60 +"percent"
        elif(colnames[j].find("Households receiving food stamps/SNAP; Estimate") >-1 ) :    
            newcolname  =   "households_receiving_food_stamps_" + h60 +"total"
        elif(colnames[j].find("Percent households receiving food stamps/SNAP; Estimate") >-1 ) :    
            newcolname  =   "households_receiving_food_stamps_" + h60 +"percent"
        elif(colnames[j].find("Households not receiving food stamps/SNAP; Estimate") >-1 ) :    
            newcolname  =   "households_not_receiving_food_stamps_" + h60 +"total"
        elif(colnames[j].find("Percent households not receiving food stamps/SNAP; Estimate") >-1 ) :    
            newcolname  =   "households_not_receiving_food_stamps_" + h60 +"percent"

        newcolnames.append(newcolname)
        print("newcolname",newcolname,j,3)
        
        return()
    
    elif(colnames[j].find("HOUSEHOLD TYPE") >-1 ):
        
        if(colnames[j].find("With children under 18 years - Other family: - Male householder, no wife present") >-1 ) :
            ftype  =   "other_male_no_wife_children_under_18_"
        elif(colnames[j].find("With children under 18 years - Other family: - Female householder, no husband present") >-1 ) :
            ftype  =   "other_female_no_husband_children_under_18_"
        elif(colnames[j].find("No children under 18 years - Married-couple family") >-1 ) :
            ftype  =   "married_no_children_under_18_"
         
        elif(colnames[j].find("No children under 18 years - Other family: - Male householder, no wife present") >-1 ) :
            ftype  =   "other_male_no_wife_no_children_under_18_"
        elif(colnames[j].find("No children under 18 years - Other family: - Female householder, no husband present") >-1 ) :
            ftype  =   "other_female_no_husband_no_children_under_18_"
    
        elif(colnames[j].find(" No children under 18 years - Other family:") >-1 ) :
            ftype  =   "other_no_children_under_18_"
        elif(colnames[j].find("No children under 18 years - Nonfamily households") >-1 ) :
            ftype  =   "non_family_no_children_under_18_"
            
        elif(colnames[j].find("No children under 18 years") >-1 ) :
            ftype  =   "no_children_under_18_"

        elif(colnames[j].find("Married-couple family") >-1 ) :
            ftype  =   "married_couple_"
        elif(colnames[j].find("With children under 18 years - Other family:") >-1 ) :
            ftype  =   "other_with_children_under_18_"
            
        elif(colnames[j].find("Other family") >-1 ) :
            ftype  =   "other_"
        elif(colnames[j].find("Male householder, no wife present") >-1 ) :
            ftype  =   "male_no_wife_"
        elif(colnames[j].find(" Female householder, no husband present") >-1 ) :
            ftype  =   "female_no_husband_"
        elif(colnames[j].find("Nonfamily households") >-1 ) :
            ftype  =   "non_family_"
        elif(colnames[j].find("With children under 18 years - Married-couple family") >-1 ) :
            ftype  =   "married_couple_with_children_under_18_"
    
        elif(colnames[j].find("With children under 18 years") >-1 ) :
            ftype  =   "children_under_18_"

    
        if(colnames[j].find("Total; Estimate; ") >-1 ) :
            newcolname  =   "households_" + ftype +"total"
        if(colnames[j].find("Percent; Estimate; ") >-1 ) :
            newcolname  =   "households_" + ftype +"percent"
        if(colnames[j].find("Households receiving food stamps/SNAP; Estimate") >-1 ) :
            newcolname  =   "households_receiving_foodstamps_" + ftype +"total"
        if(colnames[j].find("Percent households receiving food stamps/SNAP; Estimate;") >-1 ) :
            newcolname  =   "households_receiving_foodstamps_" + ftype +"percent"
        if(colnames[j].find("Households not receiving food stamps/SNAP; Estimate") >-1 ) :
            newcolname  =   "households_not_receiving_foodstamps_" + ftype +"total"
        if(colnames[j].find("Percent households not receiving food stamps/SNAP; Estimate;") >-1 ) :
            newcolname  =   "households_not_receiving_foodstamps_" + ftype +"percent"
            
        newcolnames.append(newcolname)
        print("newcolname",newcolname,j,3)
        
        return()
    
    elif(colnames[j].find("POVERTY STATUS IN THE PAST 12 MONTHS - Below poverty level") >-1 ):
    
        if(colnames[j].find("Total; Estimate; ") >-1 ) :
            newcolname  =   "households_below_poverty_level_total"
        elif(colnames[j].find("Percent; Estimate; ") >-1 ) :
            newcolname  =   "households_below_poverty_level_percent"
        elif(colnames[j].find("Households receiving food stamps/SNAP;") >-1 ) :
            newcolname  =   "households_below_poverty_level_receiving_foodstamps_total"
        elif(colnames[j].find("Percent households receiving food stamps/SNAP;") >-1 ) :
            newcolname  =   "households_below_poverty_level_receiving_foodstamps_percent"
        elif(colnames[j].find("Households not receiving food stamps/SNAP;") >-1 ) :
            newcolname  =   "households_below_poverty_level_not_receiving_foodstamps_total"
        elif(colnames[j].find("Percent households not receiving food stamps/SNAP;") >-1 ) :
            newcolname  =   "households_below_poverty_level_not_receiving_foodstamps_percent"
        elif(colnames[j].find("At or above poverty level") >-1 ) :
            newcolname  =   "households_above_poverty_level_total"

        newcolnames.append(newcolname)
        print("newcolname",newcolname,j,3)
        
        return()
            
    newcolnames.append(colnames[j])
    print("oldcolname",colnames[j],j)
 

def clean_ACS_17_Fertility(j,colnames,newcolnames) :
    
    dtype   =   -1
    poverty_found   =   False
    
    if(colnames[j].find("POVERTY STATUS") > -1) :
        poverty_found   =   True
        #print("\nfound poverty",j,colnames[j])
    
    newcolname  =   ""
    
    if( (colnames[j].find("Total; Estimate; ") > -1) and (colnames[j].find(" to ") > -1) and (not(poverty_found)) ):
        newcolname     =   colnames[j].replace("Total; Estimate; ","fertility_population_")
        newcolname     =   newcolname.replace(" to ","_to_")
        newcolname     =   newcolname.replace(" years","_years_total")
        print("newcolname",newcolname,j,10)
        newcolnames.append(newcolname)
        return()

    elif( (colnames[j].find("Women with births in the past 12 months  - Number; Estimate; ") > -1) and (colnames[j].find(" to ") > -1) and (not(poverty_found)) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Number; Estimate; ","fertility_population_births_last_year_")
        newcolname     =   newcolname.replace(" to ","_to_")
        newcolname     =   newcolname.replace(" years","_years_total")
        print("newcolname",newcolname,j,20)
        newcolnames.append(newcolname)
        return()
        
    elif( (colnames[j].find("Women with births in the past 12 months  - Percent Distribution; Estimate; ") > -1) and (colnames[j].find(" to ") > -1) and (not(poverty_found)) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Percent Distribution; Estimate; ","fertility_population_births_last_year_")
        newcolname     =   newcolname.replace(" to ","_to_")
        newcolname     =   newcolname.replace(" years","_years_percent")
        print("newcolname",newcolname,j,30)
        newcolnames.append(newcolname)
        return()
        
    elif( (colnames[j].find("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; ") > -1) and (colnames[j].find(" to ") > -1) and (not(poverty_found)) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; ","fertility_population_births_last_year_per_1000_")
        newcolname     =   newcolname.replace(" to ","_to_")
        newcolname     =   newcolname.replace(" years","_years_ratio")
        print("newcolname",newcolname,j,40)
        newcolnames.append(newcolname)
        return()
        
    elif( (colnames[j].find("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; ") > -1) and (colnames[j].find(" to ") > -1) and (not(poverty_found)) ):
        newcolname     =   colnames[j].replace("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; ","fertility_population_births_last_year_unmarried_")
        newcolname     =   newcolname.replace(" to ","_to_")
        newcolname     =   newcolname.replace(" years","_years_percent")
        print("newcolname",newcolname,j,50)
        newcolnames.append(newcolname)
        return()    
    
    elif(colnames[j].find("Total; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") > -1) :
        newcolname     =   colnames[j].replace("Total; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","fertility_population_")
        dtype = 0
    elif(colnames[j].find("Women with births in the past 12 months  - Number; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Number; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","fertility_population_births_last_year_")
        dtype = 1
    elif(colnames[j].find("Women with births in the past 12 months  - Percent Distribution; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Percent Distribution; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","fertility_population_births_last_year_")
        dtype = 2
    elif(colnames[j].find("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","fertility_population_births_last_year_")
        dtype = 3
    elif(colnames[j].find("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ") > -1) :
        newcolname     =   colnames[j].replace("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; RACE AND HISPANIC OR LATINO ORIGIN - ","fertility_population_births_last_year_unmarried_")
        dtype = 4
        
    if(dtype > -1) :
        
        #print("newcolname : inter",newcolname)
        newcolname     =   newcolname.replace("One race - White","white")
        newcolname     =   newcolname.replace("One race - Black or African American","black")
        newcolname     =   newcolname.replace("One race - American Indian and Alaska Native","native_american")
        newcolname     =   newcolname.replace("One race - Asian","asian")
        newcolname     =   newcolname.replace("One race - Native Hawaiian and Other Pacific Islander","hawaiin_and_pacific")
        newcolname     =   newcolname.replace("One race - Some other race","other")
        newcolname     =   newcolname.replace("Two or more races","mixed")
        
        newcolname     =   newcolname.replace("One race","one_race")
        
        if(dtype == 3) :
            newcolname  =   newcolname + "_ratio"
        elif(dtype == 2) :
            newcolname  =   newcolname + "_percent"
        else :
            newcolname  =   newcolname + "_total"
            
        print("newcolname",newcolname,j,60)
        newcolnames.append(newcolname)
        return()
            
    if(colnames[j].find("Total; Estimate; Hispanic or Latino origin (of any race)") > -1) :
        newcolname     =   colnames[j].replace("Total; Estimate; Hispanic or Latino origin (of any race)","fertility_population_hispanic_total")
        dtype = 0
    elif(colnames[j].find("Women with births in the past 12 months  - Number; Estimate; Hispanic or Latino origin (of any race)") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Number; Estimate; Hispanic or Latino origin (of any race)","fertility_population_hispanic_births_last_year")
        dtype = 1
    elif(colnames[j].find("Women with births in the past 12 months  - Percent Distribution; Estimate; Hispanic or Latino origin (of any race)") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Percent Distribution; Estimate; Hispanic or Latino origin (of any race)","fertility_population_hispanic_births_last_year")
        dtype = 2
    elif(colnames[j].find("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; Hispanic or Latino origin (of any race)") > -1) :
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; Hispanic or Latino origin (of any race)","fertility_population_hispanic_births_last_year")
        dtype = 3
    elif(colnames[j].find("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; Hispanic or Latino origin (of any race)") > -1) :
        newcolname     =   colnames[j].replace("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; Hispanic or Latino origin (of any race)","fertility_population_hispanic_births_last_year_unmarried")
        dtype = 4

    if(dtype > -1) :
        if(dtype == 3) :
            newcolname  =   newcolname + "_ratio"
        elif(dtype == 2) :
            newcolname  =   newcolname + "_percent"
        else :
            newcolname  =   newcolname + "_total"
            
        print("newcolname",newcolname,j,70)
        newcolnames.append(newcolname)
        return()
            
        
    if( (colnames[j].find("Total; Estimate; ") > -1) and 
        ( (colnames[j].find("alone, not") > -1) or (colnames[j].find("NATIVITY") > -1) or 
          (colnames[j].find("EDUCATIONAL ATTAINMENT") > -1) or (poverty_found) ) ):
        newcolname     =   colnames[j].replace("Total; Estimate; ","fertility_population_")
        dtype = 0

    elif( (colnames[j].find("Women with births in the past 12 months  - Number; Estimate; ") > -1) and
          ( (colnames[j].find("alone, not") > -1) or (colnames[j].find("NATIVITY") > -1) or 
            (colnames[j].find("EDUCATIONAL ATTAINMENT") > -1) or (poverty_found) ) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Number; Estimate; ","fertility_population_births_last_year_")
        dtype = 1
                
    elif( (colnames[j].find("Women with births in the past 12 months  - Percent Distribution; Estimate; ") > -1) and
          ( (colnames[j].find("alone, not") > -1) or (colnames[j].find("NATIVITY") > -1) or 
            (colnames[j].find("EDUCATIONAL ATTAINMENT") > -1) or (poverty_found) ) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Percent Distribution; Estimate; ","fertility_population_births_last_year_")
        dtype = 2
                
    elif( (colnames[j].find("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; ") > -1) and 
          ( (colnames[j].find("alone, not") > -1) or (colnames[j].find("NATIVITY") > -1) or 
            (colnames[j].find("EDUCATIONAL ATTAINMENT") > -1) or (poverty_found) ) ):
        newcolname     =   colnames[j].replace("Women with births in the past 12 months  - Rate per 1,000 women; Estimate; ","fertility_population_births_last_year_per_1000_")
        dtype = 3                
    
    elif( (colnames[j].find("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; ") > -1) and 
          ( (colnames[j].find("alone, not") > -1) or (colnames[j].find("NATIVITY") > -1) or 
            (colnames[j].find("EDUCATIONAL ATTAINMENT") > -1) or (poverty_found) ) ):
        newcolname     =   colnames[j].replace("Percent of women who had a birth in the past 12 months who were unmarried; Estimate; ","fertility_population_births_last_year_unmarried_")
        dtype = 4
                
            

    if(dtype > -1) :
        
        #print("tcolname",newcolname)
                
        newcolname     =   newcolname.replace("POVERTY STATUS IN THE PAST 12 MONTHS - Women 15 to 50 years for whom poverty status is determined","women_15_to_50_in_poverty")
        newcolname     =   newcolname.replace(" - Below 100 percent of poverty level","_below_100_percent_of_poverty_level")
        newcolname     =   newcolname.replace(" - 100 to 199 percent of poverty level","_100_to_199_percent_of_poverty_level")
        newcolname     =   newcolname.replace(" - 200 percent or more above poverty level","_200_percent_or_more_of_poverty_level")
                 
        newcolname     =   newcolname.replace("EDUCATIONAL ATTAINMENT - Graduate or professional degree","graduate_or_professional_degree")
        newcolname     =   newcolname.replace("EDUCATIONAL ATTAINMENT - Bachelor's degree","bachelor_degree")
        newcolname     =   newcolname.replace("EDUCATIONAL ATTAINMENT - Some college or associate's degree","some_college_or_associate_degree")
        newcolname     =   newcolname.replace("EDUCATIONAL ATTAINMENT - Less than high school graduate","less_than_high_school_graduate")
        newcolname     =   newcolname.replace("EDUCATIONAL ATTAINMENT - High school graduate (includes equivalency)","high_school_graduate")
 
                
                
        newcolname     =   newcolname.replace("White alone, not Hispanic or Latino","white")
        newcolname     =   newcolname.replace("NATIVITY - Native","native_american")
        newcolname     =   newcolname.replace("NATIVITY - Foreign born","foreign_born")
                 
        if(dtype==2) :
            newcolname     =   newcolname + "_percent"    
        elif(dtype==3) :
            newcolname     =   newcolname + "_ratio"    
        else :
            newcolname     =   newcolname + "_total"    
        
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()
                         
    newcolnames.append(colnames[j])
    print("oldcolname",colnames[j],j)


def clean_ACS_17_MaritalStatus(j,colnames,newcolnames) :
    
    newcolname  =   ""
    

    if(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN") >-1 ) :
        
        if(colnames[j].find("Population 15 years and over") > -1) :
            arange    =   "15_and_over_"
        
        if(colnames[j].find("One race - White") > -1) :
            race    =   "white_"
        elif(colnames[j].find("One race - Black or African American") > -1) :
            race    =   "black_"
        elif(colnames[j].find("One race - American Indian and Alaska Native") > -1) :
            race    =   "native_american_"
        elif(colnames[j].find("One race - Asian") > -1) :
            race    =   "asian_"
        elif(colnames[j].find("One race - Native Hawaiian and Other Pacific Islander") > -1) :
            race    =   "hawaiin_and_pacific_"
        elif(colnames[j].find("One race - Some other race") > -1) :
            race    =   "other_"
        elif(colnames[j].find("Two or more races") > -1) :
            race    =   "mixed_"
    
        else :
            race    =   "all_"
        
        if(colnames[j].find("Total; Estimate;") >-1 ) :
            newcolname  =   "population_" + arange + race + "total"

        elif(colnames[j].find("Now married (except separated); Estimate; ") >-1 ) :
            newcolname  =   "population_now_married_" + arange + race + "total"
        elif(colnames[j].find("Widowed; Estimate; ") >-1 ) :
            newcolname  =   "population_widowed_" + arange + race + "total"
        elif(colnames[j].find("Divorced; Estimate; ") >-1 ) :
            newcolname  =   "population_divorced_" + arange + race + "total"
        elif(colnames[j].find("Separated; Estimate; ") >-1 ) :
            newcolname  =   "population_separated_" + arange + race + "total"
        elif(colnames[j].find("Never married; Estimate; ") >-1 ) :
            newcolname  =   "population_never_married_" + arange + race + "total"

        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()

    if( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1) or 
        (colnames[j].find("White alone, not Hispanic or Latino") >-1) ):

        if(colnames[j].find("Hispanic or Latino origin (of any race)") >-1 ) :
            race    =   "hispanic_all_"
        if(colnames[j].find("White alone, not Hispanic or Latino") >-1 ) :
            race    =   "white_"

        if(colnames[j].find("Total; Estimate;") >-1 ) :
            newcolname  =   "population_" + race + "total"
        elif(colnames[j].find("Now married (except separated); Estimate;") >-1 ) :
            newcolname  =   "population_now_married_except_married_" + race + "total"
        elif(colnames[j].find("Widowed; Estimate;") >-1 ) :
            newcolname  =   "population_widowed_" + race + "total"
        elif(colnames[j].find("Divorced; Estimate;") >-1 ) :
            newcolname  =   "population_divorced_" + race + "total"
        elif(colnames[j].find("Separated; Estimate;") >-1 ) :
            newcolname  =   "separated_divorced_" + race + "total"
        elif(colnames[j].find("Never married; Estimate;") >-1 ) :
            newcolname  =   "never_married_" + race + "total"
    
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("LABOR FORCE PARTICIPATION ") >-1) :
        
        if(colnames[j].find(" Males 16 years and over - In labor force") >-1) :
            pop_tl  =   "males_16_and_over_working_"
        elif(colnames[j].find(" Males 16 years and over") >-1) :
            pop_tl  =   "males_16_and_over_"
        elif(colnames[j].find(" Females 16 years and over - In labor force") >-1) :
            pop_tl  =   "females_16_and_over_working_"
        elif(colnames[j].find(" Females 16 years and over") >-1) :
            pop_tl  =   "females_16_and_over_"
        
        if(colnames[j].find("Total; Estimate;") >-1 ) :
            newcolname  =   "population_" + pop_tl + "total"
        elif(colnames[j].find("Now married (except separated); Estimate;") >-1 ) :
            newcolname  =   "population_now_married_except_separated_" + pop_tl + "total"
        elif(colnames[j].find("Widowed; Estimate;") >-1 ) :
            newcolname  =   "population_widowed_" + pop_tl + "total"
        elif(colnames[j].find("Divorced; Estimate;") >-1 ) :
            newcolname  =   "population_divorced_" + pop_tl + "total"
        elif(colnames[j].find("Separated; Estimate;") >-1 ) :
            newcolname  =   "population_separated_" + pop_tl + "total"
        elif(colnames[j].find("Never married; Estimate;") >-1 ) :
            newcolname  =   "population_never_married_" + pop_tl + "total"
    
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()
       

    elif(colnames[j].find("AGE AND SEX ") >-1 ) :
    
        sp_15   =   ""
        
        sex = ""
        
        if(colnames[j].find("Males 15 years and over") >-1 ) :
            sex = "males_"
        if(colnames[j].find("Females 15 years and over") >-1 ) :
            sex = "females_"

        if(len(sex) > 0) :
            
            if(colnames[j].find("- 15 to 19 years") >-1 ) :
                sp_15   =   "15_to_19_"
            elif(colnames[j].find("- 20 to 34 years") >-1 ) :
                sp_15   =   "20_to_34_"
            elif(colnames[j].find("- 35 to 44 years") >-1 ) :
                sp_15   =   "35_to_44_"
            elif(colnames[j].find("- 45 to 54 years") >-1 ) :
                sp_15   =   "45_to_54_"
            elif(colnames[j].find("- 55 to 64 years") >-1 ) :
                sp_15   =   "55_to_64_"
            elif(colnames[j].find("- 65 years and over") >-1 ) :
                sp_15   =   "65_and_over_"
            else :
                sp_15   =   ""
                
        if(colnames[j].find("Total; Estimate;") >-1 ) :
            newcolname  =   "population_all_" + sp_15 + "total"
        elif(colnames[j].find("Now married (except separated); Estimate;") >-1 ) :
            newcolname  =   "population_now_married_except_separated_" + sex + sp_15 + "total"
        elif(colnames[j].find("Widowed; Estimate;") >-1 ) :
            newcolname  =   "population_widowed_" + sex + sp_15 + "total"
        elif(colnames[j].find("Divorced; Estimate;") >-1 ) :
            newcolname  =   "population_divorced_" + sex + sp_15 + "total"
        elif(colnames[j].find("Separated; Estimate;") >-1 ) :
            newcolname  =   "separated_divorced_" + sex + sp_15 + "total"
        elif(colnames[j].find("Never married; Estimate;") >-1 ) :
            newcolname  =   "never_married_" + sex + sp_15 + "total"
    
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()
    
    elif(colnames[j].find("Population 15 years and over") >-1 ) :
        
        pop_15  =   "population_15_years_and_over_"
        
        if(colnames[j].find("Now married (except separated); Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "now_married_except_married_" + "total"
        elif(colnames[j].find("Widowed; Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "widowed_" + "total"
        elif(colnames[j].find("Divorced; Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "divorced_" + "total"
        elif(colnames[j].find("Divorced; Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "divorced_" + "total"
        elif(colnames[j].find("Separated; Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "separated_" + "total"
        elif(colnames[j].find("Never married; Estimate; ") >-1 ) :
            newcolname  =   pop_15 + "never_married_" + "total"
        else :
            newcolname  =   pop_15 + "all_" + "total"
            
            
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()
    
    newcolnames.append(colnames[j])
    print("oldcolname",colnames[j],j)


def clean_ACS_17_Poverty(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if(colnames[j].find("; AGE") >-1 ) :

        if(colnames[j].find("AGE - Under 18 years - Under 5 years") > -1) :
            arange    =   "under_5_"
        elif(colnames[j].find("AGE - Under 18 years") > -1) :
            arange    =   "under_18_"
        elif(colnames[j].find("AGE - Under 18 years - Under 5 years") > -1) :
            arange    =   "under_5_"
        elif(colnames[j].find("AGE - Under 18 years - 5 to 17 years") > -1) :
            arange    =   "5_to_17_"
        elif(colnames[j].find("AGE - Under 18 years - Related children of householder under 18 years") > -1) :
            arange    =   "with_related_children_under_18"
        elif(colnames[j].find("AGE - 18 to 64 years") > -1) :
            arange    =   "18_to_64_"
        elif(colnames[j].find("AGE - 18 to 64 years - 18 to 34 years") > -1) :
            arange    =   "18_to_34_"
        elif(colnames[j].find("AGE - 18 to 64 years - 35 to 64 years") > -1) :
            arange    =   "35_to_64_"
        elif(colnames[j].find("AGE - 60 years and over") > -1) :
            arange    =   "60_and_over_"
        elif(colnames[j].find("AGE - 65 years and over") > -1) :
            arange    =   "65_and_over_"
        else :
            arange = ""
         
        
        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = ""
            
        newcolname  =   "population_" + arange + mclass  
        print("newcolname",newcolname,j,10)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("; SEX") >-1 ) :

        if(colnames[j].find("SEX - Male") >-1 ) :  
            sex = "male_"
        elif(colnames[j].find("SEX - Female") >-1 ) :  
            sex = "female_"
        else :
            sex = ""

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; SEX") > -1) :    
            mclass = "total"
        else :
            mclass = ""

        newcolname  =   "population_" + sex + mclass  
        print("newcolname",newcolname,j,20)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find(" RACE AND HISPANIC OR LATINO ORIGIN") >-1 ) :

        if(colnames[j].find("White alone") >-1 ) :  
            race = "white_"
        elif(colnames[j].find("Black or African American alone") >-1 ) :  
            race = "black_"
        elif(colnames[j].find("American Indian and Alaska Native alone") >-1 ) :  
            race = "native_american_"
        elif(colnames[j].find("Asian alone") >-1 ) :  
            race = "asian_"
        elif(colnames[j].find("Native Hawaiian and Other Pacific Islander alone") >-1 ) :  
            race = "hawaiin_and_pacific_"
        elif(colnames[j].find("Some other race alone") >-1 ) :  
            race = "other_"
        elif(colnames[j].find("Two or more races") >-1 ) :  
            race = "mixed_"

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_" + race + mclass  
        print("newcolname",newcolname,j,30)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("Hispanic or Latino origin (of any race)") >-1 ) :

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_hispanic_" + mclass  
        print("newcolname",newcolname,j,40)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("White alone, not Hispanic or Latino") >-1 ) :

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_white_" + mclass  
        print("newcolname",newcolname,j,50)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("EDUCATIONAL ATTAINMENT") >-1 ) :
        
        
        if(colnames[j].find("Population 25 years and over") > -1) :
            age = "25_and_over_"
        else :
            age = ""


        if(colnames[j].find("Less than high school graduate") > -1) :
            edu     =   "less_than_high_school_"
        elif(colnames[j].find("High school graduate (includes equivalency)") > -1) :
            edu     =   "high_school_"
        elif(colnames[j].find("Some college, associate's degree") > -1) :
            edu     =   "some_college_or_associates_degree_"
        elif(colnames[j].find("Bachelor's degree or higher") > -1) :
            edu     =   "bachelors_degree_or_higher_"
        else :
            edu = ""

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; EDUCATIONAL ATTAINMENT") > -1) :    
            mclass = "total"
        else :
            mclass = ""
            
        newcolname  =   "population_" + age + edu + mclass  
        print("newcolname",newcolname,j,60)
        newcolnames.append(newcolname)
        return()


    elif(colnames[j].find("EMPLOYMENT STATUS") >-1 ) :
        
        
        if(colnames[j].find("Civilian labor force 16 years and over") > -1) :
            age = "16_and_over_"
        else :
            age = ""


        if(colnames[j].find("- Employed") > -1) :
            emp     =   "employed_"
        elif(colnames[j].find("- Unemployed") > -1) :
            emp     =   "unemployed_"
        else :
            emp = ""
            
        if(colnames[j].find("- Male") > -1) :
            sex     =   "male_"
        elif(colnames[j].find("- Female") > -1) :
            sex     =   "female_"
        else :
            sex = ""

        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_" + age + sex + emp + mclass  
        print("newcolname",newcolname,j,70)
        newcolnames.append(newcolname)
        return()


    elif(colnames[j].find("WORK EXPERIENCE") >-1 ) :
        
        if(colnames[j].find("Population 16 years and over") > -1) :
            age = "16_and_over_"
        else :
            age = ""

        if(colnames[j].find("Worked full-time, year-round in the past 12 months") > -1) :
            emp     =   "full_time_"
        elif(colnames[j].find("Worked part-time or part-year in the past 12 months") > -1) :
            emp     =   "part_time_"
        elif(colnames[j].find("Did not work") > -1) :
            emp     =   "not_working_"
        else :
            emp = ""
            
        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; WORK EXPERIENCE") > -1) :    
            mclass = "total"
        else :
            mclass = ""
            
        newcolname  =   "population_" + age + emp + mclass  
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()


    elif(colnames[j].find("ALL INDIVIDUALS WITH INCOME BELOW THE FOLLOWING POVERTY RATIOS ") >-1 ) :
        
        if(colnames[j].find("150 percent of poverty level") > -1) :
            plev     =   "150_percent_of_poverty_level_"
        elif(colnames[j].find("50 percent of poverty level") > -1) :
            plev     =   "50_percent_of_poverty_level_"
        elif(colnames[j].find("125 percent of poverty level") > -1) :
            plev     =   "125_percent_of_poverty_level_"
        elif(colnames[j].find("185 percent of poverty level") > -1) :
            plev     =   "185_percent_of_poverty_level_"
        elif(colnames[j].find("200 percent of poverty level") > -1) :
            plev     =   "200_percent_of_poverty_level_"
        elif(colnames[j].find("300 percent of poverty level") > -1) :
            plev     =   "300_percent_of_poverty_level_"
        elif(colnames[j].find("400 percent of poverty level") > -1) :
            plev     =   "400_percent_of_poverty_level_"
        elif(colnames[j].find("500 percent of poverty level") > -1) :
            plev     =   "500_percent_of_poverty_level_"
        else :
            plev = ""
            
        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_" + plev + mclass  
        print("newcolname",newcolname,j,90)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("UNRELATED INDIVIDUALS FOR WHOM POVERTY STATUS IS DETERMINED") >-1 ) :
        
        if(colnames[j].find("- Male") > -1) :
            sex     =   "male_"
        elif(colnames[j].find("- Female") > -1) :
            sex     =   "female_"
        else :
            sex = ""
            
        if(colnames[j].find("Below poverty level;") > -1) :
            mclass = "below_poverty_level_total"
        elif(colnames[j].find("Percent below poverty level;") > -1) :    
            mclass = "below_poverty_level_percent"
        elif(colnames[j].find("Total; Estimate; AGE") > -1) :    
            mclass = "total"
        else :
            mclass = "total"
            
        newcolname  =   "population_unrelated_" + sex + mclass  
        print("newcolname",newcolname,j,100)
        newcolnames.append(newcolname)
        return()
    
    else :
        newcolnames.append(colnames[j])
        print("oldcolname",colnames[j],j)



def clean_ACS_17_Veteran_Status(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if(colnames[j].find("PERIOD OF SERVICE ") >-1 ) :
        
        if(colnames[j].find("Percent Veterans; Estimate;") > -1) :    
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate; ") > -1) :
            mclass = "veterans_total"
        else :
            mclass = ""
        
        if(colnames[j].find("Gulf War (9/2001 or later) veterans") >-1 ) : 
            period  =   "gulf_war_or_later_"
        elif(colnames[j].find("Gulf War (9/2001 or later) veterans") >-1 ) : 
            period  =   "gulf_war_2001_or_later_"
        elif(colnames[j].find("Gulf War (8/1990 to 8/2001) veterans") >-1 ) : 
            period  =   "gulf_war_1990_to_2000_"
        elif(colnames[j].find("Vietnam era veterans") >-1 ) : 
            period  =   "vietnam_"
        elif(colnames[j].find("Korean War veterans") >-1 ) : 
            period  =   "korea_"
        elif(colnames[j].find("World War II veterans") >-1 ) : 
            period  =   "world_war_II_"
        else :
            period = ""
        
        newcolname  =   "population_" + period + mclass  
        print("newcolname",newcolname,j,10)
        newcolnames.append(newcolname)
        return()
    
    elif(colnames[j].find("Estimate; SEX") >-1 ) :
   
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
    
        if(colnames[j].find("SEX - Male") > -1) :    
            sex = "male_"
        elif(colnames[j].find("SEX - Female") > -1) :
            sex = "female_"
        else :
            sex = ""
    
        newcolname  =   "population_" + sex + mclass  
        print("newcolname",newcolname,j,20)
        newcolnames.append(newcolname)
        return()
    

    elif(colnames[j].find("Estimate; AGE") >-1 ) :
        
        if(colnames[j].find("AGE - 18 to 34 years") > -1) :
            age = "18_to_34_"
        elif(colnames[j].find("AGE - 35 to 54 years") > -1) :
            age = "35_to_54_"
        elif(colnames[j].find("AGE - 55 to 64 years") > -1) :
            age = "55_to_64_"
        elif(colnames[j].find("AGE - 65 to 74 years") > -1) :
            age = "65_to_74_"
        elif(colnames[j].find("75 years and over") > -1) :
            age = "75_and_over_"
        else :
            age = ""
        
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
    
        newcolname  =   "population_" + age + mclass  
        print("newcolname",newcolname,j,30)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN ") >-1 ) :

        if(colnames[j].find(" - White alone") > -1) :
            race = "white_"
        elif(colnames[j].find("Black or African American alone") > -1) :
            race = "black_"
        elif(colnames[j].find("American Indian and Alaska Native alone") > -1) :
            race = "native_american_"
        elif(colnames[j].find("Asian alone") > -1) :
            race = "asian_"
        elif(colnames[j].find("Native Hawaiian and Other Pacific Islander alone") > -1) :
            race = "hawaiin_pacific_"
        elif(colnames[j].find("Asian alone") > -1) :
            race = "other_"
        elif(colnames[j].find("Two or more races") > -1) :
            race = "mixed_"
        else :
            race = ""
                
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
    
        newcolname  =   "population_" + race + mclass  
        print("newcolname",newcolname,j,40)
        newcolnames.append(newcolname)
        return()

        
         
    elif(colnames[j].find("EDUCATIONAL ATTAINMENT ") >-1 ) :
        
        if(colnames[j].find("Less than high school graduate") > -1) : 
            edu = "less_than_high_school_graduate_"
        elif(colnames[j].find("High school graduate (includes equivalency)") > -1) : 
            edu = "high_school_graduate_"
        elif(colnames[j].find("Some college or associate's degree") > -1) : 
            edu = "some_college_or_associate_degree_"
        elif(colnames[j].find("Bachelor's degree or higher") > -1) : 
            edu = "bachelor_degree_or_higher_"
        else :
            edu = ""

        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
 
        newcolname  =   "population_over_25_" + edu + mclass  
        print("newcolname",newcolname,j,70)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("EMPLOYMENT STATUS") >-1 ) :
        
        if(colnames[j].find("Labor force participation rate") > -1) :
            subclass = "participation_rate_"
        elif(colnames[j].find("Civilian labor force 18 to 64 years") > -1) :
            subclass = "in_labor_force_"
        else :
            subclass = ""
        
            
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
 
        newcolname  =   "population_18_to_64_" + subclass + mclass  
        print("newcolname",newcolname,j,80)
        newcolnames.append(newcolname)
        return()

    elif(colnames[j].find("Estimate; POVERTY STATUS IN THE PAST 12 MONTHS") >-1 ) :
        
        if(colnames[j].find("Income in the past 12 months below poverty level") > -1) :
            subclass = "income_below_poverty_"
        elif(colnames[j].find("Income in the past 12 months at or above poverty level") > -1) :
            subclass = "income_at_or_above_poverty_"
        else :
            subclass = ""
            
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
 
        newcolname  =   "population_" + subclass + mclass  
        print("newcolname",newcolname,j,90)
        newcolnames.append(newcolname)
        return()


    elif(colnames[j].find("Estimate; DISABILITY STATUS ") >-1 ) :
        
        if(colnames[j].find("With any disability") > -1) :
            subclass = "any_disability_"
        elif(colnames[j].find("Without a disability") > -1) :
            subclass = "without_a_disability_"
        else :
            subclass = ""
            
        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :
            mclass = "percent"
        elif(colnames[j].find("Percent Veterans; Estimate;") > -1) :
            mclass = "veterans_percent"
        elif(colnames[j].find("Veterans; Estimate") > -1) :    
            mclass = "veterans_total"
        elif(colnames[j].find("Percent Nonveterans; Estimate;") > -1) :
            mclass = "non_veterans_percent"
        elif(colnames[j].find("Nonveterans; Estimate;") > -1) :    
            mclass = "non_veterans_total"
        else :
            mclass = ""
 
        newcolname  =   "population_below_poverty_" + subclass + mclass  
        print("newcolname",newcolname,j,100)
        newcolnames.append(newcolname)
        return()
    
    newcolnames.append(colnames[j])
    print("oldcolname",colnames[j],j)



def clean_ACS_17_Languages(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if(colnames[j].find("SPEAK A LANGUAGE OTHER THAN ENGLISH") >-1 ) :
        
        if(colnames[j].find("Spanish") > -1) :    
            lang = "spanish"
        elif(colnames[j].find("Other Indo-European languages") > -1) :
            lang = "indo_european"
        elif(colnames[j].find("Asian and Pacific Island languages") > -1) :
            lang = "asian_and_pacific"
        elif(colnames[j].find("Other languages") > -1) :
            lang = "other"
        else :
            lang = ""

        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "_total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :    
            mclass = "_percent"
        else :
            mclass = ""
            
            
        if(colnames[j].find("5 to 17 years old") > -1) :    
            age = "_5_to_17"
        elif(colnames[j].find("18 to 64 years old") > -1) :    
            age = "_18_to_64"
        elif(colnames[j].find("65 years old and over") > -1) :    
            age = "_65_and_over"
        else :
            age = ""
           
        newcolname  =   "population_speak_" + lang + age + mclass  
        print("newcolname",newcolname,j,10)
        newcolnames.append(newcolname)
        return()

    if(colnames[j].find("CITIZENS 18 YEARS AND OVER") >-1 ) :
        
        if(colnames[j].find("Speak English only") > -1) : 
            lang = "_speak_english_only"
        if(colnames[j].find("Speak only English") > -1) : 
            lang = "_speak_english_only"
        elif(colnames[j].find('English  less than "very well"') > -1) :
            lang = "_speak_english_secondary"
        elif(colnames[j].find('English less than "very well"') > -1) :
            lang = "_speak_english_secondary"
    
        elif(colnames[j].find("Other languages") > -1) :
            lang = "_speak_other"
    
        elif(colnames[j].find("Speak a language other than English - Spanish") > -1) :
            lang = "_speak_spanish"
        elif(colnames[j].find("Speak a language other than English") > -1) :
            lang = "_other_than_english"
    
        else :
            lang = ""

        if(colnames[j].find("Total; Estimate;") > -1) :    
            mclass = "_total"
        elif(colnames[j].find("Percent; Estimate;") > -1) :    
            mclass = "_percent"
        else :
            mclass = ""
            
            
        if(colnames[j].find("5 to 17 years old") > -1) :    
            age = "_5_to_17"
        elif(colnames[j].find("18 to 64 years old") > -1) :    
            age = "_18_to_64"
        elif(colnames[j].find("65 years old and over") > -1) :    
            age = "_65_and_over"
        else :
            age = ""
           
        newcolname  =   "population_citizens_over_18" + lang + age + mclass  
        print("newcolname",newcolname,j,10)
        newcolnames.append(newcolname)
        return()

    newcolnames.append(colnames[j])
    print("oldcolname",colnames[j],j)


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Nativity Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""
        
def clean_ACS_17_Nativity(j,colnames,newcolnames,race) :
    
    newcolname  =   ""
    
    if(colnames[j].find("Estimate; Male:") >-1 ) :
        sex = "_male"
    elif(colnames[j].find("Estimate; Female:") >-1 ) :
        sex = "_female"
    else :
        sex = ""
        
    qual    =   "_total"
        
    if(colnames[j].find("Under 18 years:") >-1 ) :
        age = "_under_18"
    elif(colnames[j].find("18 years and over:") >-1 ) :
        age = "_over_18"
    else :
        age = ""
        
    if(colnames[j].find("Foreign born: - Naturalized U.S. citizen") >-1 ) :
        citz = "_foreign_born_naturalized_citizen"
    elif(colnames[j].find("Foreign born: - Not a U.S. citizen") >-1 ) :
        citz = "_foreign_born_not_a_citizen"
    elif(colnames[j].find("Foreign born") >-1 ) :
        citz = "_foreign_born"
    elif(colnames[j].find("- Native") >-1 ) :
        citz = "_native"
    else :
        citz = ""
        
    if((len(age)==0) and (len(citz)==0)) :
        
        if(len(sex) == 0) :
            newcolname  =   "population_" + race + qual  
        else :
            newcolname  =   "population_" + race + sex + qual  
         
    else :
        newcolname  =   "population_" + race + age + sex + citz + qual         
    
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)
    
"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Place Of Birth Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""
      
        
def clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,race) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Born in state of residence") >-1 ) :
        newcolname  =   "population_" + race + "_born_in_state_of_residence_total"
    elif(colnames[j].find("Born in other state in the United States") >-1 ) :
        newcolname  =   "population_" + race + "_born_outside_state_of_residence_total"
    elif(colnames[j].find("Native; born outside the United States") >-1 ) :
        newcolname  =   "population_" + race + "_native_born_outside_us_total"
    elif(colnames[j].find("Foreign born") >-1 ) :
        newcolname  =   "population_" + race + "_foreign_born_total"
    else :
        newcolname  =   "population_" + race + "_total"
    
     
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)
    
      
def clean_ACS_17_Place_Of_Birth_1(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Estimate; Native:") >-1 ) :
        
        pstat = "_native_born"
        bstat = ""
        area = ""
        
        if(colnames[j].find("Born in state of residence") >-1 ) : 
            bstat = "_in_state_of_residence"
            
        elif(colnames[j].find("Born in other state in the United States") >-1 ) : 
            bstat = "_in_other_state"
            if(colnames[j].find("- Northeast") >-1 ) : area = "_northeast"
            elif(colnames[j].find("Midwest") >-1 ) : area = "_midwest"
            elif(colnames[j].find("South") >-1 ) : area = "_south"
            elif(colnames[j].find("West") >-1 ) : area = "_west"
            else : area = ""
                
        elif(colnames[j].find("Native: - Born outside the United States") >-1 ) :
            bstat = "_outside_us"
            if(colnames[j].find("Puerto Rico") >-1 ) : area = "_puerto_rico"
            elif(colnames[j].find("U.S. Island Areas") >-1 ) : area = "_us_island_areas"
            elif(colnames[j].find("Born abroad of American parent(s)") >-1 ) : area = "_to_american_parents" 
            else : area = ""
                
                
    elif(colnames[j].find("Estimate; Foreign born") >-1 ) :
        
        pstat = "_foreign_born"
        bstat = ""
        area = ""
        
        if(colnames[j].find("Naturalized U.S. citizen") >-1 ) : 
            bstat = "_naturalized_citizen"    
            if(colnames[j].find("Europe") >-1 ) : area = "_europe"
            elif(colnames[j].find("Asia") >-1 ) : area = "_asia"
            elif(colnames[j].find("Africa") >-1 ) : area = "_africa"
            elif(colnames[j].find("Oceania") >-1 ) : area = "_oceania"
            elif(colnames[j].find("Latin America") >-1 ) : area = "_latin_america"
            elif(colnames[j].find("Northern America") >-1 ) : area = "_north_america"
            else : area = ""
                    
        elif(colnames[j].find("Not a U.S. citizen") >-1 ) : 
            bstat = "_not_a_citizen"    
            if(colnames[j].find("Europe") >-1 ) : area = "_europe"
            elif(colnames[j].find("Asia") >-1 ) : area = "_asia"
            elif(colnames[j].find("Africa") >-1 ) : area = "_africa"
            elif(colnames[j].find("Oceania") >-1 ) : area = "_oceania"
            elif(colnames[j].find("Latin America") >-1 ) : area = "_latin_america"
            elif(colnames[j].find("Northern America") >-1 ) : area = "_north_america"
            else : area = ""
            
    else :
        pstat = "_place_of_birth"
        bstat = ""
        area = ""
        
                
    if(j>1) :
        if(colnames[j].find("Estimate; Foreign born") >-1 ) :
            newcolname  =   "population" + pstat + area + bstat + "_total"
        else :
            newcolname  =   "population" + pstat + bstat + area + "_total"
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)
    
    
def clean_ACS_17_Place_Of_Birth_MS(j,colnames,newcolnames) :
    
    newcolname  =   ""
    mstat = ""
    res = ""
    
    if(colnames[j].find("Now married, except separated") >-1 ) : mstat = "_married"
    elif(colnames[j].find("Never married") >-1 ) : mstat = "_never_married"

    elif(colnames[j].find("Divorced") >-1 ) : mstat = "_divorced"
    elif(colnames[j].find("Separated") >-1 ) : mstat = "_separated"
    elif(colnames[j].find("Widowed") >-1 ) : mstat = "_widowed"
        
    if(colnames[j].find("Born in state of residence:") >-1 ) : res  =   "_born_in_state_of_residence"
    elif(colnames[j].find("Born in other state in the United States:") >-1 ) : res  =   "_born_in_other_state"
    elif(colnames[j].find("Native; born outside the United States:") >-1 ) :  res  =   "_born_outside_us"
    elif(colnames[j].find("Foreign born:") >-1 ) : res  =   "_foreign_born"
    else : res = ""
                
    if(j>1) :
        newcolname  =   "population" + res + mstat + "_total"
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)
    


def clean_ACS_17_Place_Of_Birth_Education(j,colnames,newcolnames) :
    
    #print("clean",j,colnames[j])
    
    newcolname  =   ""
    
    edu     =   get_education(j,colnames)

    
    if(colnames[j].find("Born in state of residence") >-1) :
        res = "_born_in_state_of_residence"
    elif(colnames[j].find("Born in other state in the United States") >-1) :
        res = "_born_outside_state_of_residence"
    elif(colnames[j].find("Native; born outside the United States") >-1) :
        res = "_native_born_outside_us"
    elif(colnames[j].find("Foreign born") >-1) :
        res = "_foreign_born"
    else :
        res = ""
    
    newcolname = "population" + res + edu + "_total"

    if(j>2) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Place_Of_Birth_Income(j,colnames,newcolnames) :
    
    #print("clean",j,colnames[j])
    
    newcolname  =   ""
    

    
    if(colnames[j].find("Born in state of residence") >-1) :
        res = "_born_in_state_of_residence"
    elif(colnames[j].find("Born in other state in the United States") >-1) :
        res = "_born_outside_state_of_residence"
    elif(colnames[j].find("Native; born outside the United States") >-1) :
        res = "_native_born_outside_us"
    elif(colnames[j].find("Foreign born") >-1) :
        res = "_foreign_born"
    else :
        res = ""
 
    if(colnames[j].find("No income") >-1) :
        inc =   "_no_income"
    elif(colnames[j].find("With income") >-1) :
        
        inc     =   get_income(j,colnames)
    else :
        inc = ""
        
    
    newcolname = "population" + res + inc + "_total"

    if(j>2) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)




def get_countries(j,colnames,newcolnames) :
    
    fixes =     {"Estimate; Total:":"population_foreign_born_total",
                 'Estimate; Africa:': 'africa', 
                 'Estimate; Africa: - Africa, n.e.c.': 'africa_n.e.c.', 
                 'Estimate; Africa: - Eastern Africa:': 'eastern_africa', 
                 'Estimate; Africa: - Eastern Africa: - Other Eastern Africa': 'eastern_africa:_other', 
                 'Estimate; Africa: - Middle Africa:': 'middle_africa', 
                 'Estimate; Africa: - Middle Africa: - Other Middle Africa': 'middle_africa_other', 
                 'Estimate; Africa: - Northern Africa:': 'northern_africa', 
                 'Estimate; Africa: - Northern Africa: - Other Northern Africa': 'northern_africa_other', 
                 'Estimate; Africa: - Southern Africa:': 'southern_africa', 
                 'Estimate; Africa: - Southern Africa: - Other Southern Africa': 'southern_africa_other', 
                 'Estimate; Africa: - Western Africa:': 'western_africa', 
                 'Estimate; Africa: - Western Africa: - Cabo Verde': 'cabo_verde', 
                 'Estimate; Africa: - Western Africa: - Other Western Africa': 'western_africa_other', 
                 'Estimate; Americas:': 'americas', 
                 'Estimate; Americas: - Latin America:': 'latin_america', 
                 'Estimate; Americas: - Latin America: - Caribbean:': 'latin_america_caribbean', 
                 'Estimate; Americas: - Latin America: - Caribbean: - Other Caribbean': 'latin_america_caribbean_other', 
                 'Estimate; Americas: - Latin America: - Caribbean: - St. Vincent and the Grenadines': 'st_vincent_and_the_grenadines', 
                 'Estimate; Americas: - Latin America: - Caribbean: - West Indies': 'west_indies', 
                 'Estimate; Americas: - Latin America: - Central America:': 'central_america', 
                 'Estimate; Americas: - Latin America: - Central America: - Other Central America': 'central_america_other', 
                 'Estimate; Americas: - Latin America: - South America:': 'south_america', 
                 'Estimate; Americas: - Latin America: - South America: - Other South America': 'south_america_other', 
                 'Estimate; Americas: - Northern America:': 'northern_america', 
                 'Estimate; Americas: - Northern America: - Other Northern America': 'northern_america_other', 
                 'Estimate; Asia:': 'asia', 
                 'Estimate; Asia: - Asia,n.e.c.': 'asia_n.e.c.', 
                 'Estimate; Asia: - Eastern Asia:': 'eastern_asia_n.e.c.', 
                 'Estimate; Asia: - Eastern Asia: - China: - Hong Kong': 'hong_kong', 
                 'Estimate; Asia: - Eastern Asia: - China: - Taiwan': 'taiwan', 
                 'Estimate; Asia: - Eastern Asia: - Korea': 'korea', 
                 'Estimate; Asia: - Eastern Asia: - Other Eastern Asia': 'eastern_asia_other', 
                 'Estimate; Asia: - South Central Asia:': 'south_central_asia', 
                 'Estimate; Asia: - South Central Asia: - Other South Central Asia': 'south_central_asia_other', 
                 'Estimate; Asia: - South Eastern Asia:': 'south_eastern_asia', 
                 'Estimate; Asia: - South Eastern Asia: - Burma': 'burma', 
                 'Estimate; Asia: - South Eastern Asia: - Laos': 'laos', 
                 'Estimate; Asia: - South Eastern Asia: - Other South Eastern Asia': 'south_eastern_asia_other',
                 'Estimate; Asia: - Western Asia:': 'western_asia', 
                 'Estimate; Asia: - Western Asia: - Other Western Asia': 'western_asia_other', 
                 'Estimate; Europe: - Eastern Europe:': 'eastern_europe', 
                 'Estimate; Europe: - Eastern Europe: - Moldova': 'moldova', 
                 'Estimate; Europe: - Eastern Europe: - Other Eastern Europe': 'eastern_europe_other', 
                 'Estimate; Europe: - Europe, n.e.c.': 'europe_n.e.c.', 
                 'Estimate; Europe: - Northern Europe:': 'northern_europe', 
                 'Estimate; Europe: - Northern Europe: - Other Northern Europe': 'northern_europe_other', 
                 'Estimate; Europe: - Northern Europe: - United Kingdom (inc. Crown Dependencies): - England': 'england', 
                 'Estimate; Europe: - Northern Europe: - United Kingdom (inc. Crown Dependencies): - Scotland': 'scotland', 
                 'Estimate; Europe: - Northern Europe: - United Kingdom (inc. Crown Dependencies): - United Kingdom, excluding England and Scotland': 'united_kingdom_other', 
                 'Estimate; Europe: - Southern Europe:': 'southern_europe', 
                 'Estimate; Europe: - Southern Europe: - Other Southern Europe': 'southern_europe_other', 
                 'Estimate; Europe: - Southern Europe: - Portugal - Azores Islands': 'portugal_and_azores', 
                 'Estimate; Europe: - Western Europe:': 'western_europe', 
                 'Estimate; Europe: - Western Europe: - Other Western Europe': 'western_europe_other', 
                 'Estimate; Oceania:': 'oceania', 
                 'Estimate; Oceania: - Australia and New Zealand Subregion: - Australia': 'australia', 
                 'Estimate; Oceania: - Australia and New Zealand Subregion: - Other Australian and New Zealand Subregion': 'australia_and_new_zealand_other', 
                 'Estimate; Oceania: - Oceania, n.e.c.': 'oceania_n.e.c.',
                 'Estimate; Asia: - South Central Asia: - Afghanistan': 'afghanistan', 
                 'Estimate; Europe: - Eastern Europe: - Albania': 'albania', 
                 'Estimate; Americas: - Latin America: - South America: - Argentina': 'argentina', 
                 'Estimate; Asia: - Western Asia: - Armenia': 'armenia', 
                 'Estimate; Oceania: - Australia and New Zealand Subregion:': 'new_zealand', 
                 'Estimate; Europe: - Western Europe: - Austria': 'austria', 
                 'Estimate; Americas: - Latin America: - Caribbean: - Bahamas': 'bahamas', 
                 'Estimate; Asia: - South Central Asia: - Bangladesh': 'bangladesh', 
                 'Estimate; Americas: - Latin America: - Caribbean: - Barbados': 'barbados', 
                 'Estimate; Europe: - Western Europe: - Belgium': 'belgium', 
                 'Estimate; Americas: - Latin America: - Central America: - Belize': 'belize', 
                     'Estimate; Americas: - Latin America: - South America: - Bolivia': 'bolivia', 
                     'Estimate; Europe: - Eastern Europe: - Bosnia and Herzegovina': 'bosnia_and_herzegovina', 
                     'Estimate; Americas: - Latin America: - South America: - Brazil': 'brazil', 
                     'Estimate; Europe: - Eastern Europe: - Bulgaria': 'bulgaria', 
                     'Estimate; Asia: - South Eastern Asia: - Cambodia': 'cambodia', 
                     'Estimate; Africa: - Middle Africa: - Cameroon': 'cameroon', 
                     'Estimate; Americas: - Northern America: - Canada': 'canada', 
                     'Estimate; Americas: - Latin America: - South America: - Chile': 'chile', 
                     'Estimate; Asia: - Eastern Asia: - China:': 'china', 
                     'Estimate; Americas: - Latin America: - South America: - Colombia': 'colombia', 
                     'Estimate; Americas: - Latin America: - Central America: - Costa Rica': 'costa_rica', 
                     'Estimate; Europe: - Eastern Europe: - Croatia': 'croatia', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Cuba': 'cuba', 
                     'Estimate; Europe: - Eastern Europe: - Czechoslovakia (includes Czech Republic and Slovakia)': 'slovakia', 
                     'Estimate; Europe: - Northern Europe: - Denmark': 'denmark', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Dominica': 'dominica', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Dominican Republic': 'dominican_republic', 
                     'Estimate; Americas: - Latin America: - South America: - Ecuador': 'ecuador', 
                     'Estimate; Africa: - Northern Africa: - Egypt': 'egypt', 
                     'Estimate; Americas: - Latin America: - Central America: - El Salvador': 'el_salvador', 
                     'Estimate; Africa: - Eastern Africa: - Eritrea': 'eritrea', 
                     'Estimate; Africa: - Eastern Africa: - Ethiopia': 'ethiopia', 
                     'Estimate; Europe:': 'Europe', 'Estimate; Oceania: - Fiji': 'fiji', 
                     'Estimate; Europe: - Western Europe: - France': 'france', 
                     'Estimate; Europe: - Western Europe: - Germany': 'germany', 
                     'Estimate; Africa: - Western Africa: - Ghana': 'ghana', 
                     'Estimate; Europe: - Southern Europe: - Greece': 'greece', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Grenada':'grenada', 
                     'Estimate; Americas: - Latin America: - Central America: - Guatemala': 'guatemala', 
                     'Estimate; Americas: - Latin America: - South America: - Guyana': 'guyana', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Haiti': 'haiti', 
                     'Estimate; Americas: - Latin America: - Central America: - Honduras': 'honduras', 
                     'Estimate; Asia: - Eastern Asia: - China: - China, excluding Hong Kong and Taiwan': 'taiwan', 
                     'Estimate; Europe: - Eastern Europe: - Hungary': 'hungary', 
                     'Estimate; Asia: - South Central Asia: - India': 'india', 
                     'Estimate; Asia: - South Eastern Asia: - Indonesia': 'indonesia', 
                     'Estimate; Asia: - South Central Asia: - Iran': 'iran', 
                     'Estimate; Asia: - Western Asia: - Iraq': 'iraq', 
                     'Estimate; Europe: - Northern Europe: - Ireland': 'ireland', 
                     'Estimate; Asia: - Western Asia: - Israel': 'israel', 
                     'Estimate; Europe: - Southern Europe: - Italy': 'italy', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Jamaica': 'jamaica', 
                     'Estimate; Asia: - Eastern Asia: - Japan': 'japan', 
                     'Estimate; Asia: - Western Asia: - Jordan': 'jordan', 
                     'Estimate; Asia: - South Central Asia: - Kazakhstan': 'kazakhstan', 
                     'Estimate; Africa: - Eastern Africa: - Kenya': 'kenya', 
                     'Estimate; Asia: - Western Asia: - Kuwait': 'kuwait', 
                     'Estimate; Europe: - Eastern Europe: - Latvia': 'latvia', 
                     'Estimate; Asia: - Western Asia: - Lebanon': 'lebanon', 
                     'Estimate; Africa: - Western Africa: - Liberia': 'liberia', 
                     'Estimate; Europe: - Eastern Europe: - Lithuania': 'lithuania', 
                     'Estimate; Europe: - Eastern Europe: - Macedonia': 'macedonia', 
                     'Estimate; Asia: - South Eastern Asia: - Malaysia': 'malaysia', 
                     'Estimate; Americas: - Latin America: - Central America: - Mexico': 'mexico', 
                     'Estimate; Africa: - Northern Africa: - Morocco': 'morocco', 
                     'Estimate; Asia: - South Central Asia: - Nepal': 'nepal', 
                     'Estimate; Europe: - Western Europe: - Netherlands': 'netherlands', 
                     'Estimate; Americas: - Latin America: - Central America: - Nicaragua': 'nicaragua', 
                     'Estimate; Africa: - Western Africa: - Nigeria': 'nigeria', 
                     'Estimate; Europe: - Northern Europe: - Norway': 'norway', 
                     'Estimate; Asia: - South Central Asia: - Pakistan': 'pakistan', 
                     'Estimate; Americas: - Latin America: - Central America: - Panama': 'panama', 
                     'Estimate; Americas: - Latin America: - South America: - Peru': 'peru', 
                     'Estimate; Asia: - South Eastern Asia: - Philippines': 'philippines', 
                     'Estimate; Europe: - Eastern Europe: - Poland': 'poland', 
                     'Estimate; Europe: - Southern Europe: - Portugal': 'portugal', 
                     'Estimate; Europe: - Eastern Europe: - Romania': 'romania', 
                     'Estimate; Europe: - Eastern Europe: - Russia': 'russia', 
                     'Estimate; Asia: - Western Asia: - Saudi Arabia': 'saudi_arabia', 
                     'Estimate; Europe: - Eastern Europe: - Serbia': 'serbia', 
                     'Estimate; Africa: - Western Africa: - Sierra Leone': 'sierra_leone', 
                     'Estimate; Asia: - South Eastern Asia: - Singapore': 'singapore', 
                     'Estimate; Africa: - Eastern Africa: - Somalia': 'somalia', 
                     'Estimate; Africa: - Southern Africa: - South Africa': 'south_africa', 
                     'Estimate; Europe: - Southern Europe: - Spain': 'spain', 
                     'Estimate; Asia: - South Central Asia: - Sri Lanka': 'sri_lanka', 
                     'Estimate; Africa: - Northern Africa: - Sudan': 'sudan', 
                     'Estimate; Europe: - Western Europe: - Switzerland': 'switzerland', 
                     'Estimate; Asia: - Western Asia: - Syria': 'syria', 
                     'Estimate; Asia: - South Eastern Asia: - Thailand': 'thailand', 
                     'Estimate; Americas: - Latin America: - Caribbean: - Trinidad and Tobago': 'trinidad_and_tobago', 
                     'Estimate; Asia: - Western Asia: - Turkey': 'turkey', 
                     'Estimate; Europe: - Eastern Europe: - Ukraine': 'ukraine', 
                     'Estimate; Europe: - Northern Europe: - United Kingdom (inc. Crown Dependencies):': 'united_kingdom', 
                     'Estimate; Americas: - Latin America: - South America: - Uruguay': 'uruguay', 
                     'Estimate; Asia: - South Central Asia: - Uzbekistan': 'uzbekistan', 
                     'Estimate; Americas: - Latin America: - South America: - Venezuela': 'venezuela', 
                     'Estimate; Asia: - South Eastern Asia: - Vietnam': 'vietnam', 
                     'Estimate; Asia: - Western Asia: - Yemen': 'yemen'}


    if(j>1) :
        
        cname   =   fixes.get(colnames[j],None)
        
        if(cname == None) :
            newcolname  =   colnames[j]
        else :
            if(j==2) :
                newcolname  =   cname
            else :
                newcolname  =   "population_foreign_born_" + cname + "_total"

    else :
        newcolname  =  colnames[j] 
    
    
    newcolnames.append(newcolname)

    print("newcolname",newcolname,j)

    return()


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Housing Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""


def clean_ACS_17_Housing_Occupancy(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_total"
    elif(colnames[j].find("Owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_total"
    elif(colnames[j].find("Renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_total"
    
    elif(colnames[j].find("Estimate; HOUSEHOLD SIZE ") >-1 ) :
        
        if(colnames[j].find("1-person household") >-1 ) : 
            size = "_1_person"
        elif(colnames[j].find("2-person household") >-1 ) : 
            size = "_2_person"
        elif(colnames[j].find("3-person household") >-1 ) : 
            size = "_3_person"
        elif(colnames[j].find("4-or-more-person household") >-1 ) : 
            size = "_3_or_more_person"
        else :
            size = ""
            
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""
            
        newcolname  =   "housing_units_with" + size + stype
            
    elif(colnames[j].find(" Estimate; OCCUPANTS PER ROOM") >-1 ) :
            
        if(colnames[j].find("1.00 or less occupants per room") >-1 ) : 
            size = "_1_or_less_per_room"
        elif(colnames[j].find("1.01 to 1.50 occupants per room") >-1 ) : 
            size = "_1_to_1.5_per_room"
        elif(colnames[j].find("1.51 or more occupants per room") >-1 ) : 
            size = "_1.5_or_more_per_room"
        elif(colnames[j].find("4-or-more-person household") >-1 ) : 
            size = "_3_or_more_person"
        else :
            size = ""

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_with" + size + stype

    elif(colnames[j].find("Estimate; HOUSEHOLD TYPE (INCLUDING LIVING ALONE) AND AGE OF HOUSEHOLDER") >-1 ) :
        
        if(colnames[j].find("Family households - Married-couple family") >-1 ) : 
            size = "_married_family_household"
        elif(colnames[j].find("Family households - Other family - Male householder, no wife present") >-1 ) : 
            size = "_male_no_wife_family_household"
        elif(colnames[j].find("Family households - Other family - Female householder, no husband present") >-1 ) : 
            size = "_female_no_husband_family_household"
        elif(colnames[j].find("Family households - Other family") >-1 ) : 
            size = "_other_family_household"
        elif(colnames[j].find("Family households") >-1 ) : 
            size = "_family_households"
        elif(colnames[j].find("Nonfamily households - Householder living alone") >-1 ) : 
            size = "_non_family_living_alone_households"
        elif(colnames[j].find("Nonfamily households - Householder not living alone") >-1 ) : 
            size = "_non_family_not_living_alone_households"
        elif(colnames[j].find("Nonfamily households") >-1 ) : 
            size = "_non_family_households"
        else :
            size = ""

        if(colnames[j].find("Householder 15 to 34 years") >-1 ) : 
            age = "_15_to_34"    
        elif(colnames[j].find("Householder 35 to 64 years") >-1 ) : 
            age = "_35_to_64"    
        elif(colnames[j].find("Householder 65 years and over") >-1 ) : 
            age = "_55_and_over" 
        else :
            age = ""

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_with" + size + age + stype


    elif(colnames[j].find("FAMILY TYPE AND PRESENCE OF OWN CHILDREN") >-1 ) :

        if(colnames[j].find(" With related children of householder under 18 years - No own children of householder under 18 years") >-1 ) : 
            size = "_no_own_children"
        elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years - Under 6 years and 6 to 17 years") >-1 ) : 
            size = "_own_children_6_to_17"
        elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years - Under 6 years only") >-1 ) : 
            size = "_own_children_under_6"
        elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years") >-1 ) : 
            size = "_own_children_under_18"
        elif(colnames[j].find("With related children of householder under 18 years") >-1 ) : 
            size = "_related_children_under_18"
        elif(colnames[j].find("No related children of householder under 18 years") >-1 ) : 
            size = "_no_related_children_under_18"
        else :
            size = ""
 

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_with" + size + stype
            
            
            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Housing_Demo(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_total"
    elif(colnames[j].find("Owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_total"
    elif(colnames[j].find("Renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_total"
    
    elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN OF HOUSEHOLDER") >-1 ) :

        
        if(colnames[j].find("One race -- - White") >-1 ) : 
            race = "_white"
        elif(colnames[j].find("One race -- - Black or African American") >-1 ) : 
            race = "_black"
        elif(colnames[j].find("One race -- - American Indian and Alaska Native") >-1 ) : 
            race = "_native_american"
        elif(colnames[j].find("One race -- - Asian") >-1 ) : 
            race = "_asian"
        elif(colnames[j].find("One race -- - Native Hawaiian and Other Pacific Islander") >-1 ) : 
            race = "_hawaiin_and_pacific"
        elif(colnames[j].find("One race -- - Some other race") >-1 ) : 
            race = "_other"
        elif(colnames[j].find("Two or more races") >-1 ) : 
            race = "_mixed"
    
        else :
            race = ""
            
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""
            
        newcolname  =   "housing_units" + race + stype

            
    elif(colnames[j].find("Estimate; Hispanic or Latino origin") >-1 ) :
            
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_hispanic" + stype

    elif(colnames[j].find("Estimate; White alone, not Hispanic or Latino") >-1 ) :
        
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_white_alone_not_hispanic" + stype


    elif(colnames[j].find("Estimate; AGE OF HOUSEHOLDER") >-1 ) :

        if(colnames[j].find("Under 35 years") >-1 ) : 
            age = "_under_35"
        elif(colnames[j].find("35 to 44 years") >-1 ) : 
            age = "_35_to_44"
        elif(colnames[j].find("45 to 54 years") >-1 ) : 
            age = "_45_to_54"
        elif(colnames[j].find("55 to 64 years") >-1 ) : 
            age = "_55_to_64"
        elif(colnames[j].find("65 to 74 years") >-1 ) : 
            age = "_65_to_74"
        elif(colnames[j].find("75 to 84 years") >-1 ) : 
            age = "_75_to_84"
        elif(colnames[j].find("85 years and over") >-1 ) : 
            age = "_85_and_over"
    
        else :
            age = ""
 

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_householder_age" + age + stype
 
    elif(colnames[j].find("Estimate; EDUCATIONAL ATTAINMENT OF HOUSEHOLDER ") >-1 ) :

        if(colnames[j].find("Less than high school graduate") >-1 ) : 
            edu = "_less_than_high_school"
        elif(colnames[j].find("High school graduate (includes equivalency)") >-1 ) : 
            edu = "_high_school"
        elif(colnames[j].find("Some college or associate's degree") >-1 ) : 
            edu = "_some_college+or_associate_degree"
        elif(colnames[j].find("Bachelor's degree or higher") >-1 ) : 
            edu = "_bachelor_degree_or_higher"
        else :
            edu = ""
 

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_householder_education" + edu + stype


    elif(colnames[j].find("Estimate; YEAR HOUSEHOLDER MOVED INTO UNIT") >-1 ) :

        if(colnames[j].find("Moved in 2015 or later") >-1 ) : 
            res = "_2015_or_later"
        elif(colnames[j].find("Moved in 2010 to 2014") >-1 ) : 
            res = "_2010_to_2014"
        elif(colnames[j].find("Moved in 2000 to 2009") >-1 ) : 
            res = "_2000_to_2009"
        elif(colnames[j].find("Moved in 1990 to 1999") >-1 ) : 
            res = "_1990_to_1999"
        elif(colnames[j].find("Moved in 1980 to 1989") >-1 ) : 
            res = "_1980_to_1989"
        elif(colnames[j].find("Moved in 1979 or earlier") >-1 ) : 
            res = "_1979_or_earlier"
            
        else :
            res = ""
 

        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""

        newcolname  =   "housing_units_householder_moved_in" + res + stype

           
            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Housing_Financial(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_financial_total"
    elif(colnames[j].find("Percent occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_financial_percent"
    
    elif(colnames[j].find("Owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_financial_total"
    elif(colnames[j].find("Percent owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_financial_percent"
        
        
    elif(colnames[j].find("Renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_financial_total"
    elif(colnames[j].find("Percent renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_financial_percent"
 
    
    
    elif(colnames[j].find("Estimate; HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS)") >-1 ) :

        if(colnames[j].find("Median household income (dollars)") >-1 ) :
            median  =   True
        else :
            median = False

        
        if(median) :
            
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_median"    
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_median"    
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_median"    
            else :
                stype = ""
            
            newcolname  =   "housing_units_income" + stype
            
            
        else :
            
            
            if(colnames[j].find("Less than $5,000") >-1 ) : 
                cash = "_less_than_5000"
            elif(colnames[j].find("$5,000 to $9,999") >-1 ) : 
                cash = "_5000_to_9999"
            elif(colnames[j].find("$10,000 to $14,999") >-1 ) : 
                cash = "_10000_to_14999"
            elif(colnames[j].find("$15,000 to $19,999") >-1 ) : 
                cash = "_15000_to_19999"
            elif(colnames[j].find("$20,000 to $24,999") >-1 ) : 
                cash = "_20000_to_24999"
            elif(colnames[j].find("$25,000 to $34,999") >-1 ) : 
                cash = "_25000_to_34999"
            elif(colnames[j].find("$35,000 to $49,999") >-1 ) : 
                cash = "_35000_to_49999"
            elif(colnames[j].find("$50,000 to $74,999") >-1 ) : 
                cash = "_50000_to_74999"
            elif(colnames[j].find("$75,000 to $99,999") >-1 ) : 
                cash = "_75000_to_99999"
            elif(colnames[j].find(" $100,000 to $149,999") >-1 ) : 
                cash = "_100000_to_149999"
            elif(colnames[j].find("$150,000 or more") >-1 ) : 
                cash = "_150000_or_more"
            else :
                cash = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_income" + cash + stype


    elif(colnames[j].find("MONTHLY HOUSING COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS ") >-1 ) :

        if(0) :
            
            
            newcolname  =   "housing_units_monthly_cost" + stype
            
            
        else :
            
            if(colnames[j].find("Less than 20 percent") >-1 ) : 
                pct = "_less_than_20"
            elif(colnames[j].find("20 to 29 percent") >-1 ) : 
                pct = "_20_to_29"
            elif(colnames[j].find("30 percent or more") >-1 ) : 
                pct = "_30_or_more"
            else : 
                pct = ""

            if(colnames[j].find("Less than $20,000") >-1 ) : 
                cash = "_less_than_20000"
            elif(colnames[j].find("$20,000 to $34,999") >-1 ) : 
                cash = "_25000_to_34999"
            elif(colnames[j].find("$35,000 to $49,999") >-1 ) : 
                 cash = "_35000_to_49999"
            elif(colnames[j].find(" $50,000 to $74,999") >-1 ) : 
                cash = "_50000_to_74999"
            elif(colnames[j].find("$75,000 or more") >-1 ) : 
                cash = "_75000_or_more"
            elif(colnames[j].find("Zero or negative income") >-1 ) : 
                cash = "_zero_or_less"
            elif(colnames[j].find("No cash rent") >-1 ) : 
                cash = "_no_cash_rent"
    
            else :
                cash = ""

            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_cost_as_pct_of_income" + cash + pct + stype

    elif(colnames[j].find("Estimate; MONTHLY HOUSING COSTS") >-1 ) :

        if(colnames[j].find("Median (dollars)") >-1 ) :
            median  =   True
        else :
            median = False

        if(median) :
            
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_median"    
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_median"    
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_median"    
            else :
                stype = ""
            
            newcolname  =   "housing_units_monthly_cost" + stype
            
            
        else :

            if(colnames[j].find("Less than $300") >-1 ) : 
                cash = "_less_than_300"
            elif(colnames[j].find("$300 to $499") >-1 ) : 
                cash = "_300_to_499"
            elif(colnames[j].find("$500 to $799") >-1 ) : 
                 cash = "_500_to_799"
            elif(colnames[j].find("$800 to $999") >-1 ) : 
                cash = "_800_to_999"
            elif(colnames[j].find("$1,000 to $1,499") >-1 ) : 
                cash = "_1000_to_1499"
            elif(colnames[j].find("$1,500 to $1,999") >-1 ) : 
                cash = "_1500_to_1999"
            elif(colnames[j].find(" $2,000 to $2,499") >-1 ) : 
                cash = "_2000_to_2499"
            elif(colnames[j].find("$2,500 to $2,999") >-1 ) : 
                cash = "_2500_to_2999"
            elif(colnames[j].find("$3,000 or more") >-1 ) : 
                cash = "_3000_or_more"
            elif(colnames[j].find("No cash rent") >-1 ) : 
                cash = "_no_cash_rent"
    
            else :
                cash = ""
            

            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_monthly_cost" + cash + stype


            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Housing_Chars(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if(colnames[j].find("Occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_total"
    elif(colnames[j].find("Percent occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "occupied_housing_units_percent"
    
    elif(colnames[j].find("Owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_total"
    elif(colnames[j].find("Percent owner-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "owner_occupied_housing_units_percent"
        
        
    elif(colnames[j].find("Renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_total"
    elif(colnames[j].find("Percent renter-occupied housing units; Estimate; Occupied housing units") >-1 ) :
        newcolname  =   "renter_occupied_housing_units_percent"
 
    
    
    elif(colnames[j].find("UNITS IN STRUCTURE") >-1 ) :

        
        if(0) :
            
            
            newcolname  =   "housing_units_income" 
            
            
        else :
            
            
            if(colnames[j].find(" 1, detached") >-1 ) : 
                apts = "_1_detached"
            elif(colnames[j].find("$5,000 to $9,999") >-1 ) : 
                apts = "_1_attached"
            elif(colnames[j].find(" 2 apartments") >-1 ) : 
                apts = "_2_apartments"
            elif(colnames[j].find("3 or 4 apartments") >-1 ) : 
                apts = "_3_or_4_apartments"
            elif(colnames[j].find("5 to 9 apartments") >-1 ) : 
                apts = "_5_to_9_apartments"
            elif(colnames[j].find("10 or more apartments") >-1 ) : 
                apts = "_10_or_more_apartments"
            elif(colnames[j].find("Mobile home or other type of housing") >-1 ) : 
                apts = "_mobile_home_or_other"
    
            else :
                apts = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_in_structure" + apts + stype


    elif(colnames[j].find("YEAR STRUCTURE BUILT") >-1 ) :

        
        if(0) :
            
            
            newcolname  =   "housing_units_income" 
            
            
        else :
            
            
            if(colnames[j].find("2014 or later") >-1 ) : 
                year = "_2014_or_later"
            elif(colnames[j].find("2010 to 2013") >-1 ) : 
                year = "_2010_2013"
            elif(colnames[j].find("2000 to 2009") >-1 ) : 
                year = "_2000_to_2009"
            elif(colnames[j].find("1980 to 1999") >-1 ) : 
                year = "_1980_to_1999"
            elif(colnames[j].find("1960 to 1979") >-1 ) : 
                year = "_1960_tp_1979"
            elif(colnames[j].find("1940 to 1959") >-1 ) : 
                year = "_1940_to_1959"
            elif(colnames[j].find("1939 or earlier") >-1 ) : 
                year = "_1939_or_earlier"
    
            else :
                year = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_year_built" + year + stype


    elif(colnames[j].find("Estimate; ROOMS") >-1 ) :

        
        if(0) :
            
            
            newcolname  =   "housing_units_income" 
            
            
        else :
            
            
            if(colnames[j].find("1 room") >-1 ) : 
                rooms = "_1_room"
            elif(colnames[j].find("2 or 3 rooms") >-1 ) : 
                rooms = "_2_or_3_rooms"
            elif(colnames[j].find("4 or 5 rooms") >-1 ) : 
                rooms = "_4_or_5_rooms"
            elif(colnames[j].find("6 or 7 rooms") >-1 ) : 
                rooms = "_6_or_7_rooms"
            elif(colnames[j].find("8 or more rooms") >-1 ) : 
                rooms = "_8_or_more_rooms"
    
            else :
                rooms = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_year_built" + rooms + stype


    elif(colnames[j].find("Estimate; BEDROOMS") >-1 ) :

        
        if(0) :
            
            
            newcolname  =   "housing_units_income" 
            
            
        else :
            
            
            if(colnames[j].find("No bedroom") >-1 ) : 
                rooms = "_no_bedroom"
            elif(colnames[j].find("1 bedroom") >-1 ) : 
                rooms = "_1_bedroom"
            elif(colnames[j].find("2 or 3 bedrooms") >-1 ) : 
                rooms = "_2_or_3_bedrooms"
            elif(colnames[j].find("4 or more bedrooms") >-1 ) : 
                rooms = "_4_or_more_bedrooms"
            else :
                rooms = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units" + rooms + stype


    elif(colnames[j].find("Estimate; COMPLETE FACILITIES") >-1 ) :

            if(colnames[j].find("With complete plumbing facilities") >-1 ) : 
                rooms = "_complete_plumbing"
            elif(colnames[j].find("With complete kitchen facilities") >-1 ) : 
                rooms = "_with_complete_kitchen"
            else :
                rooms = ""
            
             
            if(colnames[j].find("Occupied housing units;") >-1 ) : 
                stype = "_occupied_total"    
            elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
                stype = "_occupied_percent" 
            elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_total"    
            elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
                stype = "_owner_occupied_percent" 
            elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
                stype = "_renter_occupied_total"    
            elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
                stype = "_renter_occupied_percent"
            else :
                stype = ""
            
            newcolname  =   "housing_units_with" + rooms + stype


    elif(colnames[j].find("Estimate; VEHICLES AVAILABLE") >-1 ) :

        if(colnames[j].find("No vehicle available") >-1 ) : 
            vehs = "_none"
        elif(colnames[j].find("1 vehicle available") >-1 ) : 
            vehs = "_1"
        elif(colnames[j].find("2 vehicles available") >-1 ) : 
            vehs = "_2"
        elif(colnames[j].find("3 or more vehicles available") >-1 ) : 
            vehs = "_3_or_more"
        else :
            vehs = ""
            
             
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""
            
        newcolname  =   "housing_units_vehicles" + vehs + stype


    elif(colnames[j].find("Estimate; TELEPHONE SERVICE AVAILABLE") >-1 ) :

        if(colnames[j].find("With telephone service") >-1 ) : 
            tele = "_with_telephone_service"
        else :
            tele = ""
            
             
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""
            
        newcolname  =   "housing_units" + tele + stype


    elif(colnames[j].find("Estimate; HOUSE HEATING FUEL") >-1 ) :

        if(colnames[j].find("Utility gas") >-1 ) : 
            util = "_utility_gas"
        elif(colnames[j].find("Bottled, tank, or LP gas") >-1 ) : 
            util = "_bottled_tank_or_lp_gas"
        elif(colnames[j].find("Electricity") >-1 ) : 
            util = "_electricity"
        elif(colnames[j].find("Fuel oil, kerosene, etc.") >-1 ) : 
            util = "_fuel_oil_kerosene_etc"
        elif(colnames[j].find("Coal or coke") >-1 ) : 
            util = "_coal_or_coke"
        elif(colnames[j].find("All other fuels") >-1 ) : 
            util = "_other_fuels"
        elif(colnames[j].find("No fuel used") >-1 ) : 
            util = "_no_fuel_used"
            
        else :
            util = ""
            
             
        if(colnames[j].find("Occupied housing units;") >-1 ) : 
            stype = "_occupied_total"    
        elif(colnames[j].find("Percent occupied housing units") >-1 ) : 
            stype = "_occupied_percent" 
        elif(colnames[j].find("Owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_total"    
        elif(colnames[j].find("Percent owner-occupied housing units;") >-1 ) : 
            stype = "_owner_occupied_percent" 
        elif(colnames[j].find("Renter-occupied housing units;") >-1 ) : 
            stype = "_renter_occupied_total"    
        elif(colnames[j].find("Percent renter-occupied housing units;") >-1 ) :
            stype = "_renter_occupied_percent"
        else :
            stype = ""
            
        newcolname  =   "housing_units_heating" + util + stype

            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Economics Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def clean_ACS_17_Earnings(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    
    if(colnames[j].find("Population 16 years and over with earnings") >-1 ) :
        if(colnames[j].find("Total; Estimate") >-1 ) :
            newcolname  =   "population_earnings_total"
        elif(colnames[j].find("Percent; Estimate; ") >-1 ) :
            newcolname  =   "population_earnings_percent"
    
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            newcolname  =   "population_earnings_male_total"
        elif(colnames[j].find("Percent Male; Estimate") >-1 ) :
            newcolname  =   "population_earnings_male_percent"
        
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            newcolname  =   "population_earnings_female_total"
        elif(colnames[j].find("Percent Female; Estimate") >-1 ) :
            newcolname  =   "population_earnings_female_percent"
        
    if(colnames[j].find("Median earnings (dollars)") >-1 ) :
        if(colnames[j].find("Total; Estimate") >-1 ) :
            newcolname  =   "population_earnings_median"
    
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            newcolname  =   "population_earnings_male_median"
        
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            newcolname  =   "population_earnings_female_median"
        
    if(colnames[j].find("FULL-TIME, YEAR-ROUND WORKERS WITH EARNINGS") >-1 ) :

        if(colnames[j].find("$1 to $9,999 or loss") >-1 ) : 
            earn = "_1_to_9999_or_loss"
        elif(colnames[j].find("$10,000 to $14,999") >-1 ) : 
            earn = "_10000_to_14999"
        elif(colnames[j].find("$15,000 to $24,999") >-1 ) : 
            earn = "_15000_to_24999"
        elif(colnames[j].find("$25,000 to $34,999") >-1 ) : 
            earn = "_25000_to_34999"
        elif(colnames[j].find("$35,000 to $49,999") >-1 ) : 
            earn = "_35000_to_49999"
        elif(colnames[j].find("$50,000 to $64,999") >-1 ) : 
            earn = "_50000_to_64999"
        elif(colnames[j].find("$65,000 to $74,999") >-1 ) : 
            earn = "_65000_to_74999"
        elif(colnames[j].find("$75,000 to $99,999") >-1 ) : 
            earn = "_75000_to_99999"
        elif(colnames[j].find("$100,000 or more") >-1 ) : 
            earn = "_100000_or_more"
        else :
            earn = ""

        if(colnames[j].find("Total; Estimate") >-1 ) :
            stype  =   "_total"
        elif(colnames[j].find("Percent; Estimate; ") >-1 ) :
            stype  =   "_percent"
    
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            stype  =   "_male_total"
        elif(colnames[j].find("Percent Male; Estimate") >-1 ) :
            stype  =   "_male_percent"
        
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            stype  =   "_female_total"
        elif(colnames[j].find("Percent Female; Estimate") >-1 ) :
            stype  =   "s_female_percent"


        newcolname  =   "population_full_time_earnings" + earn + stype

    if(colnames[j].find("Median earnings (dollars) for full-time, year-round workers with earnings") >-1 ) :

        if(colnames[j].find("Total; Estimate") >-1 ) :
            newcolname  =   "population_full_time_earnings_median"
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            newcolname  =   "population_full_time_earnings_male_median"
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            newcolname  =   "population_full_time_earnings_female_median"

        
    if(colnames[j].find("Mean earnings (dollars) for full-time, year-round workers with earnings") >-1 ) :

        if(colnames[j].find("Total; Estimate") >-1 ) :
            newcolname  =   "population_full_time_earnings_mean"
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            newcolname  =   "population_full_time_earnings_male_mean"
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            newcolname  =   "population_full_time_earnings_female_mean"
        
    if(colnames[j].find("MEDIAN EARNINGS BY EDUCATIONAL ATTAINMENT ") >-1 ) :
        
        if(colnames[j].find("Population 25 years and over with earnings - Less than high school graduate") >-1 ) :
            edu = "_less_than_high_school_graduate"
        elif(colnames[j].find("Population 25 years and over with earnings - High school graduate (includes equivalency)") >-1 ) :
            edu = "l_high_school_graduate"
        elif(colnames[j].find("Population 25 years and over with earnings - Some college or associate's degree") >-1 ) :
            edu = "_some_colege_or_associate_degree"
        elif(colnames[j].find("Population 25 years and over with earnings - Bachelor's degree") >-1 ) :
            edu = "_bachelor_degree"
        elif(colnames[j].find("Population 25 years and over with earnings - Graduate or professional degree") >-1 ) :
            edu = "_graduate_or_professional_degree"
        else :
            edu = ""
        

        if(colnames[j].find("Total; Estimate") >-1 ) :
            stype  =   "_median"
        elif(colnames[j].find("Male; Estimate;") >-1 ) :
            stype  =   "_male_median"
        elif(colnames[j].find("Female; Estimate;") >-1 ) :
            stype  =   "_female_median"
        
        newcolname = "population_full_time_earnings" + edu + stype        
        
            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Income_Median(j,colnames,newcolnames) :
    
    newcolname  =   ""
   
    if( (colnames[j].find("Estimate; Households") >-1 ) or 
        ("Hispanic or Latino origin (of any race)") or 
        ("White alone, not Hispanic or Latino") ) :
        
        if(colnames[j].find("One race-- - White") >-1 ) :
            race   =   "_white"
        elif(colnames[j].find("Black or African American") >-1 ) :
            race   =   "_black"
        elif(colnames[j].find("American Indian and Alaska Native") >-1 ) :
            race   =   "_native_american"
        elif(colnames[j].find("One race-- - Asian") >-1 ) :
            race   =   "_asian"
        elif(colnames[j].find("One race-- - Native Hawaiian and Other Pacific Islander") >-1 ) :
            race   =   "_hawaiin_pacific"
        elif(colnames[j].find("One race-- - Some other race") >-1 ) :
            race   =   "_other"
        elif(colnames[j].find("Two or more races") >-1 ) :
            race   =   "_mixed"
        elif(colnames[j].find("Hispanic or Latino origin (of any race)") >-1 ) :    
            race   =   "_hispanic"
        elif(colnames[j].find("White alone, not Hispanic or Latino") >-1 ) :    
            race   =   "_white_not_hispanic"
        else :
            race = ""
    
        if(colnames[j].find("Number; Estimate; ") >-1 ) :
            stype   =   "_total"
        elif(colnames[j].find("Percent Distribution") >-1 ) :
            stype   =   "_percent"
        elif(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income" + race + stype
    
    if(colnames[j].find("HOUSEHOLD INCOME BY AGE OF HOUSEHOLDER") >-1 ) :
    
        if(colnames[j].find("15 to 24 years") >-1 ) :
            age   =   "_15_to_24"
        elif(colnames[j].find("25 to 44 years") >-1 ) :
            age   =   "_25_to_44"
        elif(colnames[j].find("45 to 64 years") >-1 ) :
            age   =   "_45_to_64"
        elif(colnames[j].find("65 years and over") >-1 ) :
            age   =   "_65_and_over"

        if(colnames[j].find("Number; Estimate; ") >-1 ) :
            stype   =   "_total"
        elif(colnames[j].find("Percent Distribution") >-1 ) :
            stype   =   "_percent"
        elif(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income" + age + stype

    
    if(colnames[j].find("FAMILIES - Families") >-1 ) :
    
        if(colnames[j].find("With own children of householder under 18 years") >-1 ) :
            child   =   "_own_children_under_18"
        elif(colnames[j].find("With no own children of householder under 18 years") >-1 ) :
            child   =   "_no_own_children_under_18"


        elif(colnames[j].find("Married-couple families") >-1 ) :
            
            if(colnames[j].find(" With own children under 18 years") >-1 ) :
                child   =   "_married_own_children_under_18"
            elif(colnames[j].find("With no own children of householder under 18 years") >-1 ) :
                child   =   "_no_own_children_under_18"
            else :
                child   =   "_married_couple"
    
        elif(colnames[j].find("Female householder, no husband present") >-1 ) :
            
            if(colnames[j].find(" With own children under 18 years") >-1 ) :
                child   =   "_female_no_husband_own_children_under_18"
            else :
                child   =   "_female_no_husband"
            
        elif(colnames[j].find("Male householder, no wife present") >-1 ) :
            
            if(colnames[j].find(" With own children under 18 years") >-1 ) :
                child   =   "_male_no_wife_own_children_under_18"
            else :
                child   =   "_male_no_wife"
                
        else :
            child = ""
    
    
        if(colnames[j].find("Number; Estimate; ") >-1 ) :
            stype   =   "_total"
        elif(colnames[j].find("Percent Distribution") >-1 ) :
            stype   =   "_percent"
        elif(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income" + child + stype
    
    
    if(colnames[j].find("FAMILY INCOME BY FAMILY SIZE") >-1 ) :
    
        if(colnames[j].find("2-person families") >-1 ) :
            fsize  =   "_2_person"
        elif(colnames[j].find("3-person families") >-1 ) :
            fsize  =   "_3_person"
        elif(colnames[j].find("4-person families") >-1 ) :
            fsize  =   "_4_person"
        elif(colnames[j].find("5-person families") >-1 ) :
            fsize  =   "_5_person"
        elif(colnames[j].find("6-person families") >-1 ) :
            fsize  =   "_6_person"
        elif(colnames[j].find("7-or-more person families") >-1 ) :
            fsize  =   "_7_or_more"
   
        if(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income" + fsize + "_family" + stype
    
    if(colnames[j].find("FAMILY INCOME BY NUMBER OF EARNERS") >-1 ) :
    
        if(colnames[j].find("No earners") >-1 ) :
            fsize  =   "_no_earners"
        elif(colnames[j].find("1 earner") >-1 ) :
            fsize  =   "_1_earner"
        elif(colnames[j].find("2 earners") >-1 ) :
            fsize  =   "_2_earners"
        elif(colnames[j].find(" 3 or more earners") >-1 ) :
            fsize  =   "_3_or_more_earners"
        else :
            fsize  =   ""
   
        if(colnames[j].find("Number; Estimate; ") >-1 ) :
            stype   =   "_total"
        elif(colnames[j].find("Percent Distribution") >-1 ) :
            stype   =   "_percent"
        elif(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income" + fsize + "_in_family" + stype
    
    
    if(colnames[j].find("NONFAMILY HOUSEHOLDS") >-1 ) :
    
        
        if(colnames[j].find("Female householder - Living alone") >-1 ) :
            fam  =   "_female_alone"
        elif(colnames[j].find("Female householder - Not living alone") >-1 ) :
            fam  =   "_female_not_alone"
        elif(colnames[j].find("Female householder") >-1 ) :
            fam  =   "_female"

        elif(colnames[j].find("Male householder - Living alone") >-1 ) :
            fam  =   "_male_alone"
        elif(colnames[j].find("Male householder - Not living alone") >-1 ) :
            fam  =   "_male_not_alone"
        elif(colnames[j].find("Male householder") >-1 ) :
            fam  =   "_male"
        else :
            fam = ""

        if(colnames[j].find("Number; Estimate; ") >-1 ) :
            stype   =   "_total"
        elif(colnames[j].find("Percent Distribution") >-1 ) :
            stype   =   "_percent"
        elif(colnames[j].find("Median income (dollars);") >-1 ) :
            stype   =   "_median"
        else :
            stype = ""
 
        newcolname =    "population_income_household" + fam + stype
            
    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Income(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if(colnames[j].find("Households; Estimate; Total") >-1 ) :
        newcolname   =   "households_with_income_total"
    elif(colnames[j].find("Families; Estimate; Total") >-1 ) :
        newcolname   =   "households_with_income_family_total"
    elif(colnames[j].find("Married-couple families; Estimate; Total") >-1 ) :
        newcolname   =   "households_with_income_married_couple_total"
    elif(colnames[j].find("Nonfamily households; Estimate; Total") >-1 ) :
        newcolname   =   "households_with_income_non_family_total"


    elif( (colnames[j].find("Households; Estimate; Median") >-1)  or 
          (colnames[j].find("Nonfamily households; Estimate; Median") >-1 ) or
          (colnames[j].find("Married-couple families; Estimate; Median") >-1 ) or 
          (colnames[j].find("Families; Estimate; Median") >-1) ) :

        if(colnames[j].find("Families; Estimate; Median") >-1 ) :
            fam     =   "_families" 
        elif(colnames[j].find("Married-couple families; Estimate; Median") >-1 ) :
            fam     =   "_married_couple" 
        elif(colnames[j].find("Nonfamily households; Estimate; Median") >-1 ) :
            fam     =   "_non_family"
        else :
            fam = ""

        newcolname =    "households" + fam + "_income_median"

    elif( (colnames[j].find("Households; Estimate; Mean") >-1)  or 
          (colnames[j].find("Nonfamily households; Estimate; Mean") >-1 ) or
          (colnames[j].find("Married-couple families; Estimate; Mean") >-1 ) or 
          (colnames[j].find("Families; Estimate; Mean") >-1) ) :

        if(colnames[j].find("Families; Estimate; Mean") >-1 ) :
            fam     =   "_families" 
        elif(colnames[j].find("Married-couple families; Estimate; Mean") >-1 ) :
            fam     =   "_married_couple" 
        elif(colnames[j].find("Nonfamily households; Estimate; Mean") >-1 ) :
            fam     =   "_non_family"
        else :
            fam = ""

        newcolname =    "households" + fam + "_income_mean"


    elif( (colnames[j].find("PERCENT ALLOCATED ") >-1) ) :

        if(colnames[j].find("Families; Estimate;") >-1 ) :
            fam     =   "_families" 
        elif(colnames[j].find("Nonfamily households; Estimate;") >-1 ) :
            fam     =   "_non_family"
        else :
            fam = ""

        newcolname =    "households" + fam + "_income_allocated_percent"


    elif( (colnames[j].find("Households; Estimate;") >-1)  or 
          (colnames[j].find("Nonfamily households; Estimate;") >-1 ) or
          (colnames[j].find("Married-couple families; Estimate") >-1 ) or 
          (colnames[j].find("Families; Estimate;") >-1) ) :
        
        if(colnames[j].find("Families; Estimate;") >-1 ) :
            fam     =   "_families" 
        elif(colnames[j].find("Married-couple families; Estimate") >-1 ) :
            fam     =   "_married_couple" 
        elif(colnames[j].find("Nonfamily households; Estimate;") >-1 ) :
            fam     =   "_non_family"
        else :
            fam = ""
                
        if(colnames[j].find("Less than $10,000") >-1 ) :
            inc = "_less_than_10000"
        elif(colnames[j].find("$10,000 to $14,999") >-1 ) :
            inc = "_10000_to_14999"
        elif(colnames[j].find("$15,000 to $24,999") >-1 ) :
            inc = "_15000_to_24999"
        elif(colnames[j].find("$25,000 to $34,999") >-1 ) :
            inc = "_25000_to_34999"
        elif(colnames[j].find("$35,000 to $49,999") >-1 ) :
            inc = "_35000_to_49999"
        elif(colnames[j].find("$35,000 to $49,999") >-1 ) :
            inc = "_35000_to_49999"
        elif(colnames[j].find("$50,000 to $74,999") >-1 ) :
            inc = "_50000_to_74999"
        elif(colnames[j].find("$75,000 to $99,999") >-1 ) :
            inc = "_75000_to_99999"
        elif(colnames[j].find("$100,000 to $149,999") >-1 ) :
            inc = "_100000_to_149999"
        elif(colnames[j].find("$150,000 to $199,999") >-1 ) :
            inc = "_150000_to_199999"
        elif(colnames[j].find("$200,000 or more") >-1 ) :
            inc = "_200000_or_more"

        newcolname =    "households" + fam + inc + "_income_total"

    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Mean_Income(j,colnames,newcolnames) :
    
    newcolname  =   ""


    if( (colnames[j].find("FAMILY INCOME BY NUMBER OF WORKERS IN FAMILY") >-1)) : 

        if(colnames[j].find("Number; Estimate;") >-1 ) :
            stype = "_income_total"
        elif(colnames[j].find("Percent Distribution; Estimate;") >-1 ) :
            stype = "_income_percent"
        elif(colnames[j].find("Mean income (dollars); Estimate") >-1 ) :
            stype = "_income_mean"
        else :
            stype = ""

        if(colnames[j].find("All families - No workers") >-1 ) :
            wclass  =   "_no_workers"
        elif(colnames[j].find("All families - 1 worker") >-1 ) :
            wclass  =   "_1_worker"
        elif(colnames[j].find("All families - 2 workers, husband and wife worked") >-1 ) :
            wclass  =   "_2_workers_husband_and_wife"
        elif(colnames[j].find("All families - 2 workers, other") >-1 ) :
            wclass  =   "_2_workers_other"
        elif(colnames[j].find("All families - 3 or more workers, husband and wife worked") >-1 ) :
            wclass  =   "_3_or_more_workers_husband_and_wife"
        elif(colnames[j].find("All families - 3 or more workers, other") >-1 ) :
            wclass  =   "_3_or_more_workers_other"
        else :
            wclass = "_workers"

        newcolname = "households_with" + wclass + stype 


    elif( (colnames[j].find("PER CAPITA INCOME BY RACE AND HISPANIC OR LATINO ORIGIN") >-1)) : 

        if(colnames[j].find("Number; Estimate;") >-1 ) :
            stype = "_income_total"
        elif(colnames[j].find("Percent Distribution; Estimate;") >-1 ) :
            stype = "_income_percent"
        elif(colnames[j].find("Mean income (dollars); Estimate") >-1 ) :
            stype = "_income_mean"
        else :
            stype = ""

        if(colnames[j].find("One race-- - White") >-1 ) :
            race = "_white"
        elif(colnames[j].find("One race-- - Black or African American") >-1 ) :
            race = "_black"
        elif(colnames[j].find("One race-- - Asian") >-1 ) :
            race = "_asian"
        elif(colnames[j].find("One race-- - American Indian and Alaska Native") >-1 ) :
            race = "_native_american"
        elif(colnames[j].find("One race-- - Native Hawaiian and Other Pacific Islander") >-1 ) :
            race = "_hawaiin_pacific"
        elif(colnames[j].find("One race-- - Some other race") >-1 ) :
            race = "_other"
        elif(colnames[j].find("Two or more races") >-1 ) :
            race = "_mixed"
        else :
            race = "_all_races"

        newcolname = "households" + race + stype 


    elif( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1)) : 

        if(colnames[j].find("Number; Estimate;") >-1 ) :
            stype = "_income_total"
        elif(colnames[j].find("Percent Distribution; Estimate;") >-1 ) :
            stype = "_income_percent"
        elif(colnames[j].find("Mean income (dollars); Estimate") >-1 ) :
            stype = "_income_mean"
        else :
            stype = ""

        newcolname = "households_hispanic" + stype 


    elif( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) : 

        if(colnames[j].find("Number; Estimate;") >-1 ) :
            stype = "_income_total"
        elif(colnames[j].find("Percent Distribution; Estimate;") >-1 ) :
            stype = "_income_percent"
        elif(colnames[j].find("Mean income (dollars); Estimate") >-1 ) :
            stype = "_income_mean"
        else :
            stype = ""

        newcolname = "households_white_not_hispanic" + stype 
       
 
    
    elif( (colnames[j].find("Number; Estimate;") >-1) or 
        (colnames[j].find("Percent Distribution; Estimate;") >-1) or 
        (colnames[j].find("Mean income (dollars); Estimate") >-1) ):
    
        if(colnames[j].find("Number; Estimate;") >-1 ) :
            stype = "_total"
        elif(colnames[j].find("Percent Distribution; Estimate;") >-1 ) :
            stype = "_percent"
        elif(colnames[j].find("Mean income (dollars); Estimate") >-1 ) :
            stype = "_mean"
        else :
            stype = ""
        

        if(colnames[j].find("With earnings - With wages or salary income") >-1 ) :
            wclass  =   "_with_wages_or_salary"
        elif(colnames[j].find("With earnings - With self-employment income") >-1 ) :
            wclass  =   "_self_employment"
        elif(colnames[j].find("With earnings") >-1 ) :
            wclass  =   ""
        elif(colnames[j].find("With interest, dividends, or net rental income") >-1 ) :
            wclass  =   "_interest_dividends_rental_income"
        elif(colnames[j].find("With Social Security income") >-1 ) :
            wclass  =   "_social_security"
        elif(colnames[j].find("With Supplemental Security Income (SSI)") >-1 ) :
            wclass  =   "_social_security_ssi"
        elif(colnames[j].find("With cash public assistance income or Food Stamps/SNAP - With cash public assistance") >-1 ) :
            wclass  =   "_public_assistance_or_food_stamps_and_cash"
        elif(colnames[j].find("With cash public assistance income or Food Stamps/SNAP") >-1 ) :
            wclass  =   "_public_assistance_or_food_stamps"
        elif(colnames[j].find("With retirement income") >-1 ) :
            wclass  =   "_retirement"
        elif(colnames[j].find("With other types of income") >-1 ) :
            wclass  =   "_other_income"
        else :
            wclass = ""
            
        newcolname = "households_earnings" + wclass + stype            

    if(j>3) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Median_Earning_Occupaton(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Median earnings (dollars); Estimate;") >-1)) : 
        stype   =   "_median"
    elif( (colnames[j].find("Median earnings (dollars) for male; ") >-1)) : 
        stype   =   "_male_median"
    elif( (colnames[j].find("Median earnings (dollars) for female; ") >-1)) : 
        stype   =   "_female_median"
    elif( (colnames[j].find("Women's earnings as a percentage of men's earning; Estimate;") >-1)) : 
        stype   =   "_female_to_male_percent"
    else :
        stype = ""        

    ocu = get_occupation(j,colnames)
    
    newcolname  =   "earnings_occupation" + ocu + stype


    if(j>5) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Industry_Full_Time(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Male; Estimate;") >-1)) : 
        stype   =   "_male_total"
    elif( (colnames[j].find("Percent Male;") >-1)) : 
        stype   =   "_male_percent"
    elif( (colnames[j].find("Female; Estimate;") >-1)) : 
        stype   =   "_female_total"
    elif( (colnames[j].find("Percent Female;") >-1)) : 
        stype   =   "_female_percent"
    else :
        stype = ""
        
        
    ocu     =   get_industry(colnames,j)
        

    newcolname  =   "population_employed" + ocu + stype
        

    if(j>7) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Median_Earning_Industry(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Median earnings (dollars); Estimate;") >-1)) : 
        stype   =   "_median"
    elif( (colnames[j].find("Median earnings (dollars) for male;") >-1)) : 
        stype   =   "_male_median"
    elif( (colnames[j].find("Median earnings (dollars) for female; ") >-1)) : 
        stype   =   "_female_median"
    elif( (colnames[j].find("Women's earnings as a percentage of men's earning; Estimate") >-1)) : 
        stype   =   "_earnings_of_women_to_men_percent"
    else :
        stype = ""

        
    ocu     =   get_industry(colnames,j)

    newcolname  =   "earnings" + ocu + stype
        

    if(j>5) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Transportation Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def clean_ACS_17_Means_Of_Transportation(j,colnames,newcolnames) :
    
    newcolname  =   ""

        
    if( (colnames[j].find("Estimate; AGE") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_drove_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""
        
        if( (colnames[j].find("16 to 19 years") >-1)) : 
            age   =   "_16_to_19"
        elif( (colnames[j].find("20 to 24 years") >-1)) : 
            age   =   "_20_to_24"
        elif( (colnames[j].find("25 to 44 years") >-1)) : 
            age   =   "_25_to_44"
        elif( (colnames[j].find("45 to 54 years") >-1)) : 
            age   =   "_45_to_54"
        elif( (colnames[j].find("55 to 59 years") >-1)) : 
            age   =   "_55_to_59"
        elif( (colnames[j].find("60 years and over") >-1)) : 
            age   =   "_60_and_over"
        else :
            age = ""
            
        newcolname  =   "transportation_age" + age + stype + "_total"


    elif( (colnames[j].find("Estimate; Median age (years)") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        newcolname  =   "transportation_age" + stype + "_median"


    elif( (colnames[j].find("Estimate; SEX") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("Estimate; SEX - Male") >-1)) : 
            sex   =   "_male"
        elif( (colnames[j].find("Estimate; SEX - Female") >-1)) : 
            sex   =   "_female"
        else :
            sex = ""

        newcolname  =   "transportation_sex" + sex + stype + "_median"


    elif( (colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN ") >-1)) : 
        
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""
        
        if( (colnames[j].find("One race - White") >-1)) : 
            race   =   "_white"
        elif( (colnames[j].find("One race - Black or African American") >-1)) : 
            race   =   "_black"
        elif( (colnames[j].find("One race - American Indian and Alaska Native") >-1)) : 
            race   =   "_native_american"
        elif( (colnames[j].find("One race - Asian") >-1)) : 
            race   =   "_asian"
        elif( (colnames[j].find("One race - Native Hawaiian and Other Pacific Islander") >-1)) : 
            race   =   "_hawaiian_pacific"
        elif( (colnames[j].find("One race - Some other race") >-1)) : 
            race   =   "_other"
        elif( (colnames[j].find("Two or more races") >-1)) : 
            race   =   "_mixed"
        elif( (colnames[j].find("One race") >-1)) : 
            race   =   "_one_race"
        else :
            race = ""

        newcolname  =   "transportation_race" + race + stype + "_total"


    elif( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1)) : 
        
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        newcolname  =   "_transportation_race_hispanic" + stype + "_total"

    elif( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        newcolname  =   "transportation_race_white_not_hispanic" + stype + "_total"


    elif( (colnames[j].find("NATIVITY AND CITIZENSHIP STATUS") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("Native") >-1)) : 
            nat   =   "_native_citizen"
        elif( (colnames[j].find("Foreign born - Naturalized U.S. citizen") >-1)) : 
            nat   =   "_naturalized_citizen"
        elif( (colnames[j].find("Foreign born - Not a U.S. citizen") >-1)) : 
            nat   =   "_not_a_citizen"
        elif( (colnames[j].find("Foreign born") >-1)) : 
            nat   =   "_foreign_born"
        else :
            nat = ""

        newcolname  =   "transportation_nativity" + nat + stype + "_total"


    elif( (colnames[j].find("EARNINGS IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS) FOR WORKERS ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("$1 to $9,999 or loss") >-1)) : 
            nat   =   "_1_to_99_or_less"
        elif( (colnames[j].find("$10,000 to $14,999") >-1)) : 
            nat   =   "_10000_to_14999"
        elif( (colnames[j].find(" $15,000 to $24,999") >-1)) : 
            nat   =   "_15000_to_24999"
        elif( (colnames[j].find("$25,000 to $34,999") >-1)) : 
            nat   =   "_25000_to_34999"
        elif( (colnames[j].find("$35,000 to $49,999") >-1)) : 
            nat   =   "_35000_to_49999"
        elif( (colnames[j].find("$50,000 to $64,999") >-1)) : 
            nat   =   "_50000_to_64999"
        elif( (colnames[j].find("$65,000 to $74,999") >-1)) : 
            nat   =   "_65000_to_74999"
        elif( (colnames[j].find("$75,000 or more") >-1)) : 
            nat   =   "_75000_and_over"
        else :
            nat = ""

        newcolname  =   "transportation_earnings" + nat + stype + "_total"
 
    
    elif( (colnames[j].find("EARNINGS IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS) FOR WORKERS ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("$1 to $9,999 or loss") >-1)) : 
            nat   =   "_1_to_99_or_less"
        elif( (colnames[j].find("$10,000 to $14,999") >-1)) : 
            nat   =   "_10000_to_14999"
        elif( (colnames[j].find(" $15,000 to $24,999") >-1)) : 
            nat   =   "_15000_to_24999"
        elif( (colnames[j].find("$25,000 to $34,999") >-1)) : 
            nat   =   "_25000_to_34999"
        elif( (colnames[j].find("$35,000 to $49,999") >-1)) : 
            nat   =   "_35000_to_49999"
        elif( (colnames[j].find("$50,000 to $64,999") >-1)) : 
            nat   =   "_50000_to_64999"
        elif( (colnames[j].find("$65,000 to $74,999") >-1)) : 
            nat   =   "_65000_to_74999"
        elif( (colnames[j].find("$75,000 or more") >-1)) : 
            nat   =   "_75000_and_over"
        else :
            nat = ""

        newcolname  =   "transportation_earnings" + nat + stype + "_total"

 
    elif( (colnames[j].find("Estimate; Median earnings (dollars)") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        newcolname  =   "transportation_earnings" + stype + "_median"
    
    
    elif( (colnames[j].find("POVERTY STATUS IN THE PAST 12 MONTHS") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""


        if(colnames[j].find("Below 100 percent of the poverty level") >-1) :
            estat = "_below_100_pct_of_level_of_poverty"
        elif(colnames[j].find("100 to 149 percent of the poverty level") >-1) :
            estat = "_100_to_149_pct_of_level_of_poverty"
        elif(colnames[j].find("At or above 150 percent of the poverty level") >-1) :
            estat = "_150_pct_or_above_level_of_poverty"
        else :
            estat = ""

        newcolname  =   "transportation_poverty" + estat + stype + "_total"


    elif( (colnames[j].find("OCCUPATION ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        ocu = get_occupation(j,colnames)

        newcolname  =   "transportation_occupation" + ocu + stype + "_total"


    elif( (colnames[j].find("INDUSTRY") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        ind = get_industry(colnames,j)
        
        newcolname  =   "transportation_industry" + ind + stype + "_total"


    elif( (colnames[j].find("CLASS OF WORKER ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        wclass  =   get_class_of_worker(j,colnames) 
        
        newcolname  =   "transportation_worker" + wclass + stype + "_total"


    elif( (colnames[j].find(" PLACE OF WORK ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        plow = get_place_of_work(j,colnames) 
        
        newcolname  =   "transportation_work" + plow + stype + "_total"


    elif( (colnames[j].find("Workers 16 years and over who did not work at home") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        
        newcolname  =   "transportation_work_did_not_work_at_home" + stype + "_total"



    elif( (colnames[j].find("TRAVEL TIME TO WORK - Mean travel time to work (minutes)") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        newcolname  =   "transportation_commute_time" + stype + "_mean"

    
    elif( (colnames[j].find("TRAVEL TIME TO WORK") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("15 to 19 minutes") >-1)) : 
            ttime   =   "_15_to_19_mins"
        elif( (colnames[j].find("20 to 24 minutes") >-1)) : 
            ttime   =   "_20_to_24_mins"
        elif( (colnames[j].find("25 to 29 minutes") >-1)) : 
            ttime   =   "_25_to_29_mins"
        elif( (colnames[j].find("25 to 29 minutes") >-1)) : 
            ttime   =   "_25_to_29_mins"
        elif( (colnames[j].find("30 to 34 minutes") >-1)) : 
            ttime   =   "_30_to_34_mins"
        elif( (colnames[j].find("35 to 44 minutes") >-1)) : 
            ttime   =   "_35_to_44_mins"
        elif( (colnames[j].find("45 to 59 minutes") >-1)) : 
            ttime   =   "_45_to_59_mins"
        elif( (colnames[j].find("60 or more minutes") >-1)) : 
            ttime   =   "_60_or_more_mins"
        else :
            ttime = ""
        
        newcolname  =   "transportation_commute_time" + ttime + stype + "_total"


    elif( (colnames[j].find("HOUSING TENURE ") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("Owner-occupied housing units") >-1)) : 
            house   =   "_owner"
        elif( (colnames[j].find("Renter-occupied housing units") >-1)) : 
            house   =   "_renter"
        else :
            house = ""
        
        newcolname  =   "transportation_housing" + house + stype + "_total"


    elif( (colnames[j].find("VEHICLES AVAILABLE") >-1)) : 
        
        if( (colnames[j].find("Car, truck, or van -- drove alone;") >-1)) : 
            stype   =   "_car_truck_van_alone"
        elif( (colnames[j].find("Car, truck, or van -- carpooled") >-1)) : 
            stype   =   "_car_truck_van_carpool"
        elif( (colnames[j].find("Public transportation (excluding taxicab)") >-1)) : 
            stype   =   "_public_transport_no_taxi"
        else :
            stype = ""

        if( (colnames[j].find("No vehicle available") >-1)) : 
            veh   =   "_no_vehicle"
        elif( (colnames[j].find("1 vehicle available") >-1)) : 
            veh   =   "_1_vehicle"
        elif( (colnames[j].find("2 vehicles available") >-1)) : 
            veh   =   "_2_vehicles"
        elif( (colnames[j].find("3 or more vehicles available") >-1)) : 
            veh   =   "_3_or_more_vehicles"
        else :
            veh = ""
        
        newcolname  =   "transportation_vehicles" + veh + stype + "_total"
    
    else :
        newcolname  =  colnames[j]


    if(j>5) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)

    
"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Internet Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""


def clean_ACS_17_Internet(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    else :
        stype = ""

        
    if( (colnames[j].find(" TYPES OF COMPUTER") >-1)) :
        
        if(colnames[j].find("Has one or more types of computing devices: - Desktop or laptop - Desktop or laptop with no other type of computing device") >-1) :
            ctype     =   "_one_or_more_desktop_or_laptop_no_other"
        elif(colnames[j].find("Has one or more types of computing devices: - Desktop or laptop") >-1) :
            ctype     =   "_one_or_more_desktop_or_laptop"
        
        elif(colnames[j].find("Has one or more types of computing devices: - Smartphone - Smartphone with no other type of computing device") >-1) :
            ctype     =   "_one_or_more_smartphones_and_no_other"
        elif(colnames[j].find("Has one or more types of computing devices: - Smartphone") >-1) :
            ctype     =   "_one_or_more_smartphones"

        elif(colnames[j].find(" Has one or more types of computing devices: - Tablet or other portable wireless computer - Tablet or other portable wireless computer with no other type of computing device") >-1) :
            ctype     =   "_one_or_more_tablets_or_portables_and_no_other"
        elif(colnames[j].find("Has one or more types of computing devices: - Tablet or other portable wireless computer") >-1) :
            ctype     =   "_one_or_more_tablets_or_portables"

        elif(colnames[j].find(" Has one or more types of computing devices: - Other computer - Other computer with no other type of computing device") >-1) :
            ctype     =   "_one_or_more_other_computers_and_no_other_devices"
        elif(colnames[j].find(" Has one or more types of computing devices: - Other computer") >-1) :
            ctype     =   "_one_or_more_other_computers"

        elif(colnames[j].find("Has one or more types of computing devices") >-1) :
            ctype     =   "_one_or_more_computing_devices"

        elif(colnames[j].find("No computer") >-1) :
            ctype     =   "_no_computer"
        else :
            ctype = ""
            
        newcolname  =   "households_with_income" + ctype + stype

    elif( (colnames[j].find("TYPE OF INTERNET SUBSCRIPTIONS") >-1)) :

        if(colnames[j].find("With an Internet subscription: - Dial-up with no other type of Internet subscription") >-1) :
            ctype     =   "_dial_up_only_internet_subscription"
        
        elif(colnames[j].find(" With an Internet subscription: - Broadband of any type - Cellular data plan - Cellular data plan with no other type of Internet subscription") >-1) :
            ctype     =   "_cellular_broadband_only_internet_subscription"
        elif(colnames[j].find("With an Internet subscription: - Broadband of any type - Cellular data plan") >-1) :
            ctype     =   "_cellular_broadband_internet_subscription"
        elif(colnames[j].find("With an Internet subscription: - Broadband of any type") >-1) :
            ctype     =   "_broadband_internet_subscription"
        
        elif(colnames[j].find("With an Internet subscription: - Broadband of any type - Broadband such as cable, fiber optic or DSL") >-1) :
            ctype     =   "_broadband_cable_fiber_optic_dsl_internet_subscription"

        elif(colnames[j].find("With an Internet subscription: - Broadband of any type - Satellite Internet service") >-1) :
            ctype     =   "_satelite_internet_subscription"

        elif(colnames[j].find("With an Internet subscription") >-1) :
            ctype     =   "_internet_subscription"

        elif(colnames[j].find("Without an Internet subscription") >-1) :
            ctype     =   "_without_internet_subscription"
        else :
            ctype   =   ""

        newcolname  =   "households_with_income" + ctype + stype


    elif( (colnames[j].find("HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2017 INFLATION-ADJUSTED DOLLARS)") >-1)) :

        
        if(colnames[j].find("Less than $20,000: - With dial-up Internet subscription alone") >-1) :
            amt     =   "_less_than_20000_with_dialup"
        elif(colnames[j].find("Less than $20,000: - With a broadband Internet subscription") >-1) :
            amt     =   "_less_than_20000_with_broadband"
        elif(colnames[j].find("Less than $20,000: - Without an Internet subscription") >-1) :
            amt     =   "_less_than_20000_without_internet"
        elif(colnames[j].find("Less than $20,000") >-1) :
            amt     =   "_less_than_20000"
        
        elif(colnames[j].find("$20,000 to $74,999: - With dial-up Internet subscription alone") >-1) :
            amt     =   "_20000_t0_74999_with_dialup"
        elif(colnames[j].find("$20,000 to $74,999: - With a broadband Internet subscription") >-1) :
            amt     =   "_20000_t0_74999_with_broadband"
        elif(colnames[j].find("$20,000 to $74,999: - Without an Internet subscription") >-1) :
            amt     =   "_20000_t0_74999_without_internet"
        elif(colnames[j].find("$20,000 to $74,999") >-1) :
            amt     =   "_20000_t0_74999"

        elif(colnames[j].find("$75,000 or more: - With dial-up Internet subscription alone") >-1) :
            amt     =   "_75000_or_more_with_dialup"
        elif(colnames[j].find("$75,000 or more: - With a broadband Internet subscription") >-1) :
            amt     =   "_75000_or_more_with_broadband"
        elif(colnames[j].find("$75,000 or more: - Without an Internet subscription") >-1) :
            amt     =   "_75000_or_more_without_internet"
        elif(colnames[j].find("$75,000 or more") >-1) :
            amt     =   "_75000_or_more"
        else :
            amt     =   ""

        newcolname  =   "households_with_income" + amt + stype



    if(j>2) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Internet_Chars(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    else :
        stype = ""

    if( (colnames[j].find("AGE - Under 18 years") >-1) or 
        (colnames[j].find("AGE - 18 to 64 years") >-1) or 
        (colnames[j].find("AGE - 65 years and over") >-1)) :
        
        if(colnames[j].find("AGE - Under 18 years") >-1) :
            age = "_under_18"
        elif(colnames[j].find("AGE - 18 to 64 years") >-1) :
            age = "_18_64"
        else :
            age = "_65_and_over"
        
        if( (colnames[j].find("With a computer  - Broadband Internet Subscription") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent  Broadband Internet Subscription;") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_percent"
        elif( (colnames[j].find("With a computer  - Without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_percent"
        elif( (colnames[j].find("No computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_total"
        elif( (colnames[j].find("Percent no computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_percent"
        else :
            ctype   =   ""

        newcolname  =   "population" + age + ctype + stype


    if(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN") >-1) :
        
        if( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) :
            race   =   "_white_not_hispanic_or_latino"
        elif( (colnames[j].find("White alone") >-1)) :
            race   =   "_white"
        elif( (colnames[j].find("Black or African American alone") >-1)) :
            race   =   "_black"
        elif( (colnames[j].find("American Indian and Alaska Native alone") >-1)) :
            race   =   "_native_american"
        elif( (colnames[j].find("Asian alone") >-1)) :
            race   =   "_asian"
        elif( (colnames[j].find("Native Hawaiian and Other Pacific Islander alone") >-1)) :
            race   =   "_hawaiin_pacific"
        elif( (colnames[j].find("Some other race alone") >-1)) :
            race   =   "_other"
        elif( (colnames[j].find("Two or more races") >-1)) :
            race   =   "_mixed"
        elif( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1)) :
            race   =   "_hispanic_or_latino"
        else :
            race    =   ""
        
        if( (colnames[j].find("With a computer  - Broadband Internet Subscription") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent  Broadband Internet Subscription;") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_percent"
        elif( (colnames[j].find("With a computer  - Without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_percent"
        elif( (colnames[j].find("No computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_total"
        elif( (colnames[j].find("Percent no computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_percent"
        else :
            ctype   =   ""

        newcolname  =   "population" + race + ctype + stype


    if(colnames[j].find("EDUCATIONAL ATTAINMENT") >-1) :


        if( (colnames[j].find("Less than high school graduate or equivalency") >-1)) :
            edu   =   "_less_than_high_school"
        elif( (colnames[j].find("High school graduate (includes equivalency), some college or associate's degree") >-1)) :
            edu   =   "_high_school_graduate"
        elif( (colnames[j].find("Bachelor's degree or higher") >-1)) :
            edu   =   "_bachelor_degree_or_higher"
        else :
            edu    =   "_some_education"

        if( (colnames[j].find("With a computer  - Broadband Internet Subscription") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent  Broadband Internet Subscription;") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_percent"
        elif( (colnames[j].find("With a computer  - Without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_percent"
        elif( (colnames[j].find("No computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_total"
        elif( (colnames[j].find("Percent no computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_percent"
        else :
            ctype   =   ""

        newcolname  =   "population" + edu + ctype + stype


    if(colnames[j].find("EMPLOYMENT STATUS") >-1) :

        if( (colnames[j].find("In labor force - Employed") >-1)) :
            edu   =   "_in_labor_force_employed"
        if( (colnames[j].find("In labor force - Unemployed") >-1)) :
            edu   =   "_in_labor_force_unemployed"
        elif( (colnames[j].find("Not in labor force") >-1)) :
            edu   =   "_not_in_labor_force"
        elif( (colnames[j].find("In labor force") >-1)) :
            edu   =   "_in_labor_force"
        else :
            edu     =   "_labor_force"
            
        if( (colnames[j].find("With a computer  - Broadband Internet Subscription") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent  Broadband Internet Subscription;") >-1)) :
            ctype   =   "_with_broadband"
            stype   =   "_percent"
        elif( (colnames[j].find("With a computer  - Without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_total"
        elif( (colnames[j].find("With a computer  - Percent without an Internet Subscription") >-1)) :
            ctype   =   "_without_internet"
            stype   =   "_percent"
        elif( (colnames[j].find("No computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_total"
        elif( (colnames[j].find("Percent no computer in household") >-1)) :
            ctype   =   "_no_computer"
            stype   =   "_percent"
        else :
            ctype   =   ""

        newcolname  =   "population" + edu + ctype + stype


    if(j>8) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Insurance Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def clean_ACS_17_Health_Insurance(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; Estimate") >-1)) : 
        stype   =   "_percent"
    
    elif( (colnames[j].find("Percent Insured") >-1)) : 
        stype   =   "_insured_percent"
    elif( (colnames[j].find("Insured; Estimate") >-1)) : 
        stype   =   "_insured_total"
        
    elif( (colnames[j].find("Percent Uninsured") >-1)) : 
        stype   =   "_uninsured_percent"
    elif( (colnames[j].find("Uninsured; Estimate") >-1)) : 
        stype   =   "_uninsured_total"
    else :
        stype = ""

    if(colnames[j].find("AGE - ") >-1) :
        if(colnames[j].find("AGE - Under 6 years") >-1) :
            age     =   "_under_6"
        elif(colnames[j].find("AGE - 6 to 18 years") >-1) :
            age     =   "_6_to_18"
        elif(colnames[j].find("AGE - 19 to 25 years") >-1) :
            age     =   "_19_to_25"
        elif(colnames[j].find("AGE - 26 to 34 years") >-1) :
            age     =   "_26_to_34"
        elif(colnames[j].find("AGE - 35 to 44 years") >-1) :
            age     =   "_35_to_44"
        elif(colnames[j].find("AGE - 45 to 54 years") >-1) :
            age     =   "_45_to_54"
        elif(colnames[j].find("AGE - 55 to 64 years") >-1) :
            age     =   "_55_to_64"
        elif(colnames[j].find("AGE - 65 to 74 years") >-1) :
            age     =   "_65_to_74"
        elif(colnames[j].find("AGE - 75 years and older") >-1) :
            age     =   "_75_and_over"
        else :
            age = ""

        newcolname  =   "population_age" + age + stype


    elif( colnames[j].find("SEX") >-1) :
        
        if(colnames[j].find("Male") >-1) :
            sex = "_male"
        elif(colnames[j].find("Female") >-1) :
            sex = "_female"
        
        newcolname  =   "population_sex" + sex + stype


    elif( (colnames[j].find("Under 19 years") >-1) or 
        (colnames[j].find("19 to 64 years") >-1) or
        (colnames[j].find("65 years and older") >-1) ) :
        
        if(colnames[j].find("Under 19 years") >-1) :
            age = "_under_19"
        elif(colnames[j].find("19 to 64 years") >-1) :
            age = "_19_to_64"
        elif(colnames[j].find("65 years and older") >-1) :
            age = "_65_and_over"
        else :
            age = ""
        
        newcolname  =   "population_age" + age + stype



    elif( colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN ") >-1) :
        
        if(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - White alone") >-1) :
            race = "_white"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - Black or African American alone") >-1) :
            race = "_black"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - American Indian and Alaska Native alone") >-1) :
            race = "_native_american"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - Asian alone") >-1) :
            race = "_asian"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - Native Hawaiian and Other Pacific Islander alone") >-1) :
            race = "_hawaiin_pacific"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - Some other race alone") >-1) :
            race = "_other"
        elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN - Two or more races") >-1) :
            race = "_mixed"
        else :
            race = ""
            
        newcolname  =   "population_race" + race + stype
            
            
    elif(colnames[j].find("Hispanic or Latino (of any race)") >-1) :
        
        newcolname  =   "population_race_hispanic" + stype
    
    elif(colnames[j].find("White alone, not Hispanic or Latino") >-1) :
        
        newcolname  =   "population_race_white_alone" + stype
            
    if( colnames[j].find("LIVING ARRANGEMENTS ") >-1) :
        
        if(colnames[j].find("In married couple families") >-1) :
            mstat = "_family_married_couple"
        elif(colnames[j].find("In other families - Male householder, no wife present") >-1) :
            mstat = "_family_male_no_wife"
        elif(colnames[j].find("In other families - Female householder, no husband present") >-1) :
            mstat = "_family_female_no_husband"
        elif(colnames[j].find("In other families") >-1) :
            mstat = "_family_other"
        elif(colnames[j].find("In non-family households and other living arrangements") >-1) :
            mstat = "_female_no_husband_living_arrangements"
        else :
            mstat = "_family"
            
        newcolname  =   "population" +  mstat + stype
            
            
    if( colnames[j].find("NATIVITY AND U.S. CITIZENSHIP STATUS") >-1) :
        
        if(colnames[j].find("Native born") >-1) :
            citz = "_native_born"
        elif(colnames[j].find("Foreign born - Naturalized") >-1) :
            citz = "_foreign_born_Naturalized"
        elif(colnames[j].find("Foreign born") >-1) :
            citz = "_foreign_born"
        if(colnames[j].find("Foreign born - Not a citizen") >-1) :
            citz = "_foreign_born_non_citizen"
        else :
            citz = ""
            
        newcolname  =   "population_nativity" +  citz + stype
            
    if( colnames[j].find("DISABILITY STATUS") >-1) :
        
        if(colnames[j].find("No disability") >-1) :
            dis = "_no_disability"
        elif(colnames[j].find("With a disability") >-1) :
            dis = "_with_a_disability"
        else :
            dis = ""
            
        newcolname  =   "population" +  dis + stype
            
    if( colnames[j].find("EDUCATIONAL ATTAINMENT ") >-1) :
        
        if(colnames[j].find("Less than high school graduate") >-1) :
            edu = "_less_than_high_school_graduate"
        elif(colnames[j].find("High school graduate (includes equivalency)") >-1) :
            edu = "_high_school_graduate"
        elif(colnames[j].find("Some college or associate's degree") >-1) :
            edu = "_some_college_or_associate_degree"
        elif(colnames[j].find("Bachelor's degree or higher") >-1) :
            edu = "_bachelor_degree_or_higher"
        else :
            edu = ""
            
        newcolname  =   "population_education" +  edu + stype
             
            
    if( colnames[j].find("EMPLOYMENT STATUS") >-1) :
        
        if(colnames[j].find("In labor force - Employed") >-1) :
            estat = "_employed"
        elif(colnames[j].find("In labor force - Unemployed") >-1) :
            estat = "_unemployed"
        elif(colnames[j].find("In labor force") >-1) :
            estat = "_in_labor_force"
        elif(colnames[j].find("Not in labor force") >-1) :
            estat = "_not_in_labor_force"
        else :
            estat = ""
            
        newcolname  =   "population_employment" +  estat + stype
             
    if( colnames[j].find("WORK EXPERIENCE ") >-1) :
        
        if(colnames[j].find(" Worked full-time, year round in the past 12 months") >-1) :
            estat = "_full_time"
        elif(colnames[j].find("Worked less than full-time, year round in the past 12 months") >-1) :
            estat = "_less_than_full_time"
        elif(colnames[j].find("Did not work") >-1) :
            estat = "_did_not_work"
        else :
            estat = ""
            
        newcolname  =   "population_work" +  estat + stype
             
            
    if( colnames[j].find("HOUSEHOLD INCOME (IN 2017 INFLATION-ADJUSTED DOLLARS) ") >-1) :
        
        if(colnames[j].find("Under $25,000") >-1) :
            estat = "_under_25000"
        elif(colnames[j].find("$25,000 to $49,999") >-1) :
            estat = "_25000_to_49999"
        elif(colnames[j].find("$50,000 to $74,999") >-1) :
            estat = "_50000_to_74999"
        elif(colnames[j].find("$75,000 to $99,999") >-1) :
            estat = "_75000_to_99999"
        elif(colnames[j].find("$100,000 and over") >-1) :
            estat = "_100000_and_over"
        else :
            estat = ""
            
        newcolname  =   "population_income" +  estat + stype

    if( colnames[j].find("RATIO OF INCOME TO POVERTY LEVEL IN THE PAST 12 MONTHS") >-1) :
        
        if(colnames[j].find("Below 138 percent of the poverty threshold") >-1) :
            estat = "_below_138_pct_of_level_of_poverty"
        elif(colnames[j].find("138 to 399 percent of the poverty threshold") >-1) :
            estat = "_138_to_399_pct_of_level_of_poverty"
        elif(colnames[j].find("At or above 400 percent of the poverty threshold") >-1) :
            estat = "_400_pct_or_above_level_of_poverty"
        else :
            estat = "_poverty"
            
        if( (colnames[j].find("Total; Estimate") >-1)) : 
            stype   =   "_total"
        elif( (colnames[j].find("Percent; Estimate") >-1)) : 
            stype   =   "_percent"
        elif( (colnames[j].find("Insured; Estimate") >-1)) : 
            stype   =   "_insured_total"
        elif( (colnames[j].find("Percent Insured") >-1)) : 
            stype   =   "_insured_percent"
        elif( (colnames[j].find("Uninsured; Estimate") >-1)) : 
            stype   =   "_uninsured_total"
        elif( (colnames[j].find("Percent Uninsured") >-1)) : 
            stype   =   "_uninsured_percent"
        else :
            stype = ""
            
        newcolname  =   "population" +  estat + stype

    if( colnames[j].find("Below 100 percent of the poverty threshold") >-1) :
        
        if( (colnames[j].find("Total; Estimate") >-1)) : 
            stype   =   "_total"
        elif( (colnames[j].find("Percent; Estimate") >-1)) : 
            stype   =   "_percent"
        elif( (colnames[j].find("Percent Insured") >-1)) : 
            stype   =   "_insured_percent"
        elif( (colnames[j].find("Percent Uninsured") >-1)) : 
            stype   =   "_uninsured_percent"
        elif( (colnames[j].find("Insured; Estimate") >-1)) : 
            stype   =   "_insured_total"
        elif( (colnames[j].find("Uninsured; Estimate") >-1)) : 
            stype   =   "_uninsured_total"
        else :
            stype = ""
            
        newcolname  =   "population_below_100_pct_of_the_poverty_level" +  stype

    if(j>6) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Health_Insurance_By_Type(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Private Coverage") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Private Coverage;") >-1)) : 
        stype   =   "_total"
        

    if(colnames[j].find("COVERAGE ALONE OR IN COMBINATION") >-1) :
        if(colnames[j].find("Employer-based health insurance alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_private_employer_based" + age + stype
                
                
    elif(colnames[j].find("Direct-purchase health insurance alone or in combination") >-1) :
        if(colnames[j].find("Direct-purchase health insurance alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_private_direct_purchase" + age + stype

                
    elif(colnames[j].find("Tricare/military health insurance alone or in combination") >-1) :
        if(colnames[j].find("Tricare/military health insurance alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_private_tricare_military" + age + stype

                
    elif(colnames[j].find("PRIVATE HEALTH INSURANCE ALONE OR IN COMBINATION ") >-1) :

        if(colnames[j].find("Below 138 percent of the poverty threshold") >-1) :
            estat = "_below_138_pct_of_level_of_poverty"
        elif(colnames[j].find("138 to 399 percent of the poverty threshold") >-1) :
            estat = "_138_to_399_pct_of_level_of_poverty"
        elif(colnames[j].find("At or above 400 percent of the poverty threshold") >-1) :
            estat = "_400_pct_or_above_level_of_poverty"
        else :
            estat = "_poverty"

        newcolname  =   "population_health_insurance_private_poverty" + estat + stype


    elif(colnames[j].find("Worked full-time, year-round (19-64 years)") >-1) :

        newcolname  =   "population_health_insurance_private_worked_full_time_19_to_64" + stype


    elif(colnames[j].find("Under 6") >-1) :
        newcolname  =   "population_health_insurance_private_under_6" + stype

    elif(colnames[j].find("6 to 18 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_6_to_18" + stype
                
    elif(colnames[j].find("19 to 25 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_19_to_25" + stype

    if(colnames[j].find("26 to 34 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_26_to_34" + stype

    elif(colnames[j].find("35 to 44 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_35_to_44" + stype

    elif(colnames[j].find("45 to 54 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_45_to_54" + stype

    elif(colnames[j].find("55 to 64 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_55_to_64" + stype

    elif(colnames[j].find("65 to 74 years") >-1) :
        newcolname  =   "population_health_insurance_private_age_65_to_74" + stype

    elif(colnames[j].find("75 years and over") >-1) :
        newcolname  =   "population_health_insurance_private_75_and_over" + stype

    elif(colnames[j].find("COVERAGE ALONE - Private health insurance alone") >-1) :
        
        if(colnames[j].find("Employer-based health insurance alone") >-1) :
            itype     =   "_employer_based"
        elif(colnames[j].find("Direct-purchase health insurance alone") >-1) :
            itype     =   "_direct_purchase"
        elif(colnames[j].find("Tricare/military health coverage alone") >-1) :
            itype     =   "_tricare_military"
        else :
            itype     =   ""
        
        
        newcolname  =   "population_health_insurance_private" + itype + stype



    if(j>4) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Health_Insurance_Public_Coverage(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Public Coverage") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Public Coverage;") >-1)) : 
        stype   =   "_total"
        

    if(colnames[j].find("COVERAGE ALONE OR IN COMBINATION") >-1) :
        if(colnames[j].find("Medicare coverage alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_public_medicare_plus" + age + stype
                
                
    elif(colnames[j].find("Medicaid/means-tested public coverage alone or in combination") >-1) :
        if(colnames[j].find("Medicaid/means-tested public coverage alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_public_medicaid" + age + stype


    elif(colnames[j].find("VA health care coverage alone or in combination") >-1) :
        if(colnames[j].find("VA health care coverage alone or in combination") >-1) :
            if(colnames[j].find("Under 19") >-1) :
                age     =   "_under_19"
            elif(colnames[j].find("19 to 64 years") >-1) :
                age     =   "_19_to_64"
            elif(colnames[j].find("65 years and over") >-1) :
                age     =   "_65_and_over"
            else :
                age = ""
                
        newcolname  =   "population_health_insurance_public_va" + age + stype


    elif(colnames[j].find("PUBLIC HEALTH INSURANCE ALONE OR IN COMBINATION") >-1) :
        if(colnames[j].find("Below 138 percent of the poverty threshold") >-1) :
            estat = "_below_138_pct_of_level_of_poverty"
        elif(colnames[j].find("138 to 399 percent of the poverty threshold") >-1) :
            estat = "_138_to_399_pct_of_level_of_poverty"
        elif(colnames[j].find("At or above 400 percent of the poverty threshold") >-1) :
            estat = "_400_pct_or_above_level_of_poverty"
        else :
            estat = "_poverty"

        newcolname  =   "population_health_insurance_public_poverty" + estat + stype

    elif(colnames[j].find("Worked full-time, year-round (19-64 years)") >-1) :
        newcolname  =   "population_health_insurance_public_worked_full_time" + stype

    elif(colnames[j].find("Under 6") >-1) :
        newcolname  =   "population_health_insurance_public_under_6" + stype

    elif(colnames[j].find("6 to 18 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_6_to_18" + stype
                
    elif(colnames[j].find("19 to 25 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_19_to_25" + stype

    if(colnames[j].find("26 to 34 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_26_to_34" + stype

    elif(colnames[j].find("35 to 44 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_35_to_44" + stype

    elif(colnames[j].find("45 to 54 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_45_to_54" + stype

    elif(colnames[j].find("55 to 64 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_55_to_64" + stype

    elif(colnames[j].find("65 to 74 years") >-1) :
        newcolname  =   "population_health_insurance_public_age_65_to_74" + stype

    elif(colnames[j].find("75 years and over") >-1) :
        newcolname  =   "population_health_insurance_public_75_and_over" + stype

    elif(colnames[j].find("COVERAGE ALONE - Public health insurance alone") >-1) :
        
        if(colnames[j].find("Medicare coverage alone") >-1) :
            itype     =   "_medicare_alone"
        elif(colnames[j].find("Medicaid/means tested coverage alone") >-1) :
            itype     =   "_medicaid_alone"
        elif(colnames[j].find("VA health care coverage alone") >-1) :
            itype     =   "_va_alone"
        else :
            itype     =   "_alone"
        
        newcolname  =   "population_health_insurance_public" + itype + stype

    if(j>4) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)




def clean_ACS_17_Health_Insurance_Private_Coverage(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if( (colnames[j].find("Estimate; Total:") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Estimate; Male") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Estimate; Female") >-1)) : 
        stype   =   "_total"
    else :
        stype = ""
    
    if( (colnames[j].find("Male") >-1)) : 
        sex   =   "_male"
    elif( (colnames[j].find("Female") >-1)) : 
        sex   =   "_female"
    else : 
        sex   =   ""
    
    if( (colnames[j].find("With private health insurance") >-1)) : 
        ins   =   "_private_health_insurance"
    elif( (colnames[j].find("No private health insurance") >-1)) : 
        ins   =   "_no_health_insurance"
    else : 
        ins   =   ""
 
    if(colnames[j].find("Under 6 years") >-1) :
        age  =   "_under_6"
    elif(colnames[j].find("6 to 18 years") >-1) :
        age  =   "_age_6_to_18"
    elif(colnames[j].find("19 to 25 years") >-1) :
        age  =   "_age_19_to_25"
    elif(colnames[j].find("26 to 34 years") >-1) :
        age  =   "_age_26_to_34"
    elif(colnames[j].find("35 to 44 years") >-1) :
        age  =   "_age_35_to_44"
    elif(colnames[j].find("45 to 54 years") >-1) :
        age  =   "_age_45_to_54" 
    elif(colnames[j].find("55 to 64 years") >-1) :
        age  =   "_age_55_to_64"
    elif(colnames[j].find("65 to 74 years") >-1) :
        age  =   "_age_65_to_74"
    elif(colnames[j].find("75 years and over") >-1) :
        age  =   "_75_and_over"
    else :
        age = ""
    
    
    newcolname = "population_private_health_insurance" + age + ins + sex + stype 

    

    if(j>3) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)




def clean_ACS_17_Health_Insurance_Uninsured(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Total Uninsured; Estimate;") >-1)) : 
        stype   =   "_uninsured_total"
    elif( (colnames[j].find("Public Coverage;") >-1)) : 
        stype   =   "_total"
        

    if( (colnames[j].find("AGE - Under 19 years") >-1) or 
        (colnames[j].find("AGE - 19 to 64 years") >-1) or 
        (colnames[j].find("AGE - 65 years and older") >-1) ):
        
        if(colnames[j].find("AGE - Under 19 years") >-1) :
            if(colnames[j].find("Under 6 years") >-1) :
                age     =   "_under_6"
            elif(colnames[j].find("6 to 18 years") >-1) :
                age     =   "_6_to_18"
            else :
                age = "_under_19"
                
        elif(colnames[j].find("AGE - 19 to 64 years") >-1) :
            if(colnames[j].find("19 to 25 years") >-1) :
                age     =   "_19_to_25"
            elif(colnames[j].find("26 to 34 years") >-1) :
                age     =   "_26_to_34"
            elif(colnames[j].find("35 to 44 years") >-1) :
                age     =   "_35_to_44"
            elif(colnames[j].find("45 to 54 years") >-1) :
                age     =   "_45_to_54"
            elif(colnames[j].find("55 to 64 years") >-1) :
                age     =   "_55_to_64"
            elif(colnames[j].find("65 years and older") >-1) :
                if(colnames[j].find("65 to 74 years") >-1) :
                    age     =   "_65_to_74"
                if(colnames[j].find("75 years and older") >-1) :
                    age     =   "_75_and_over"
                else :
                    age = "_65_and_older"
            else :
                age = "_19_to_64"
        
        elif( (colnames[j].find("AGE - 65 years and older") >-1) ) :
            if(colnames[j].find("AGE - 65 years and older - 65 to 74 years") >-1) :
                 age     =   "_65_to_74"
            elif(colnames[j].find("AGE - 65 years and older - 75 years and older") >-1) :
                age     =   "_75_and_older"
            else :
                age = "_65_and_older"
                
        else :
            age = ""
               
        newcolname  =   "population_health_insurance_age" + age + stype


    elif(colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN") >-1) :
        
        if( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) :
            race   =   "_white_not_hispanic_or_latino"
        elif( (colnames[j].find("White alone") >-1)) :
            race   =   "_white"
        elif( (colnames[j].find("Black or African American alone") >-1)) :
            race   =   "_black"
        elif( (colnames[j].find("American Indian and Alaska Native alone") >-1)) :
            race   =   "_native_american"
        elif( (colnames[j].find("Asian alone") >-1)) :
            race   =   "_asian"
        elif( (colnames[j].find("Native Hawaiian and Other Pacific Islander alone") >-1)) :
            race   =   "_hawaiin_pacific"
        elif( (colnames[j].find("Some other race alone") >-1)) :
            race   =   "_other"
        elif( (colnames[j].find("Two or more races") >-1)) :
            race   =   "_mixed"
        elif( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1)) :
            race   =   "_hispanic_or_latino"
        else :
            race    =   ""

        newcolname  =   "population_health_insurance_race" + race + stype


    elif(colnames[j].find("Hispanic or Latino (of any race)") >-1) :
        newcolname  =   "population_health_insurance_race_hispanic" + stype

    elif(colnames[j].find("White alone, not Hispanic or Latino") >-1) :
        newcolname  =   "population_health_insurance_race_white_not_hispanic" + stype

    elif(colnames[j].find("NATIVITY AND U.S. CITIZENSHIP ") >-1) :
        if( (colnames[j].find("Native born") >-1)) :
            citz   =   "_citizen_native_born"
        elif( (colnames[j].find("Foreign born - Naturalized") >-1)) :
            citz   =   "_citizen_foreign_born_naturalized"
        elif( (colnames[j].find("Foreign born - Not a citizen") >-1)) :
            citz   =   "_citizen_foreign_born_not_a_citizen"

        elif( (colnames[j].find("Foreign born") >-1)) :
            citz   =   "_citizen_foreign_born"
        else :
            citz = ""
            
        newcolname  =   "population_health_insurance" + citz + stype


    elif(colnames[j].find("DISABILITY STATUS") >-1) :
        if( (colnames[j].find("No disability") >-1)) :
            disa   =   "_no_disability"
        else :
            disa = ""

        newcolname  =   "population_health_insurance_disability" + disa + stype

    
    elif( (colnames[j].find("EDUCATIONAL ATTAINMENT") >-1) or 
          (colnames[j].find("Less than high school graduate") > -1) or
          (colnames[j].find("High school graduate (includes equivalency)") > -1) or 
          (colnames[j].find("Some college or associate's degree") > -1) or 
          (colnames[j].find("Bachelor's degree or higher") > -1) ):
        
        if(colnames[j].find("Less than high school graduate") > -1) :
            edu     =   "_less_than_high_school"
        elif(colnames[j].find("High school graduate (includes equivalency)") > -1) :
            edu     =   "_high_school"
        elif(colnames[j].find("Some college or associate's degree") > -1) :
            edu     =   "_some_college_or_associates_degree"
        elif(colnames[j].find("Bachelor's degree or higher") > -1) :
            edu     =   "_bachelors_degree_or_higher"
        else :
            edu = ""

        newcolname  =   "population_health_insurance_education" + edu + stype


    elif( (colnames[j].find("EMPLOYMENT STATUS") >-1) or 
          (colnames[j].find("In labor force") > -1) or
          (colnames[j].find("Not in labor force") > -1) ):
        
        if( (colnames[j].find("In labor force - Employed") >-1)) :
            edu   =   "_labor_force_employed"
        elif( (colnames[j].find("In labor force - Unemployed") >-1)) :
            edu   =   "_labor_force_unemployed"
        elif( (colnames[j].find("Not in labor force") >-1)) :
            edu   =   "_labor_force_not_in_labor_force"
        elif( (colnames[j].find("In labor force") >-1)) :
            edu   =   "_labor_force"
        else :
            edu     =   ""

        newcolname  =   "population_health_insurance_employment" + edu + stype


    elif( (colnames[j].find("WORK EXPERIENCE") >-1) or 
          (colnames[j].find("Worked full-time, year round in the past 12 months") > -1) or
          (colnames[j].find("Worked less than full-time, year round in the past 12 months") > -1) or 
          (colnames[j].find("Did not work") > -1) or 
          (colnames[j].find("workers 16 years and over") > -1) ):
        
        if( (colnames[j].find("population 16 to 64 years") >-1)) :
            edu   =   "_16_to_64"
        if( (colnames[j].find("Worked full-time, year round in the past 12 months") >-1)) :
            edu   =   "_full_time"
        elif( (colnames[j].find("Worked less than full-time, year round in the past 12 months") >-1)) :
            edu   =   "_part_time"
        elif( (colnames[j].find("Did not work") >-1)) :
            edu   =   "_did_not_work"
        elif( (colnames[j].find("Did not work") >-1)) :
            edu   =   "_workers_16_and_over"
        else :
            edu     =   ""

        newcolname  =   "population_health_insurance_workforce" + edu + stype


    elif( (colnames[j].find("CLASS OF WORKER ") >-1) ):
        
        if( (colnames[j].find("Employee of private company workers") >-1)) :
            edu   =   "_private_for_profit_company_worker"
        elif( (colnames[j].find("Self-employed in own incorporated business workers") >-1)) :
            edu   =   "_self_employed_for_profit_incorporated_worker"
        elif( (colnames[j].find("Private for-profit wage and salary workers") >-1)) :
            edu   =   "_private_for_profit_workers"
            
        elif( (colnames[j].find("CLASS OF WORKER - Private not-for-profit wage and salary workers") >-1)) :
            edu   =   "_private_not_for_profit_workers"
        
        elif( (colnames[j].find("Local government workers") >-1)) :
            edu   =   "_local_government_workers"
        elif( (colnames[j].find("State government workers") >-1)) :
            edu   =   "_state_government_workers"
        elif( (colnames[j].find("Federal government workers") >-1)) :
            edu   =   "_federal_government_workers"
        elif( (colnames[j].find("Self-employed workers in own not incorporated business workers") >-1)) :
            edu   =   "_self_employed_not_incorporated_worker"
        elif( (colnames[j].find("Unpaid family workers") >-1)) :
            edu   =   "_unpaid_family_workers"
        else:
            edu = ""

        newcolname  =   "population_health_insurance_worker" + edu + stype


    elif( (colnames[j].find("INDUSTRY ") >-1) ):

        ind = get_industry(colnames,j)
        newcolname  =   "population_health_insurance_industry" + ind + stype


    elif( (colnames[j].find("OCCUPATION") >-1) ):

        if( (colnames[j].find("Management, business, science, and arts occupations") >-1)) :
            edu   =   "_management_business_science_and_arts"
        elif( (colnames[j].find("Service occupations") >-1)) :
            edu   =   "_service"
        elif( (colnames[j].find("Sales and office occupations") >-1)) :
            edu   =   "_sales_and_office"
        elif( (colnames[j].find("Natural resources, construction, and maintenance occupations") >-1)) :
            edu   =   "_natural_resources_construction_maintenance"
        elif( (colnames[j].find("Production, transportation, and material moving occupations") >-1)) :
            edu   =   "_production_transportation_material_moving"
        elif( (colnames[j].find("Production, transportation, and material moving occupations") >-1)) :
            edu   =   "_production_transportation_material_moving"

        newcolname  =   "population_health_insurance_occupation" + edu + stype


    elif( (colnames[j].find("EARNINGS IN THE PAST 12 MONTHS (IN 2017 INFLATION ADJUSTED DOLLARS)") >-1) or
          (colnames[j].find("$1 to $4,999 or loss") >-1) or
          (colnames[j].find("$5,000 to $14,999") >-1) or
          (colnames[j].find("$15,000 to $24,999") >-1) or 
          (colnames[j].find("$25,000 to $34,999") >-1) or 
          (colnames[j].find("$35,000 to $49,999") >-1) or 
          (colnames[j].find("$50,000 to $74,999") >-1) or 
          (colnames[j].find("$75,000 or more") >-1) ):

        if(colnames[j].find("$1 to $4,999 or loss") >-1 ) : 
            earn = "_1_to_4999_or_loss"
            
        elif(colnames[j].find("$5,000 to $14,999") >-1 ) : 
            earn = "_5000_to_14999"
        elif(colnames[j].find("$15,000 to $24,999") >-1 ) : 
            earn = "_15000_to_24999"
        elif(colnames[j].find("$25,000 to $34,999") >-1 ) : 
            earn = "_25000_to_34999"
        elif(colnames[j].find("$35,000 to $49,999") >-1 ) : 
            earn = "_35000_to_49999"
        elif(colnames[j].find("$50,000 to $74,999") >-1 ) : 
            earn = "_50000_to_74999"
        elif(colnames[j].find("$75,000 or more") >-1 ) : 
            earn = "_75000_or_more"
        else :
            earn = ""

        newcolname  =   "population_health_insurance_earnings" + earn + stype


    elif( (colnames[j].find("HOUSEHOLD INCOME (IN 2017 INFLATION ADJUSTED DOLLARS)") >-1) or
          (colnames[j].find("Under $25,000") >-1) or
          (colnames[j].find("$25,000 to $49,999") >-1) or
          (colnames[j].find("$51,000 to $74,999") >-1) or 
          (colnames[j].find("$75,000 to $99,999") >-1) or 
          (colnames[j].find("$100,000 and over") >-1) ):

        if(colnames[j].find("Under $25,000") >-1) :
            inc     =   "_under_25000"
        elif(colnames[j].find("$25,000 to $49,999") >-1) :
            inc     =   "_25000_to_49999"
        elif(colnames[j].find("$51,000 to $74,999") >-1) :
            inc     =   "_50000_to_74999"
        elif(colnames[j].find("$75,000 to $99,999") >-1) :
            inc     =   "_75000_to_99999"
        elif(colnames[j].find("$100,000 and over") >-1) :
            inc     =   "_100000_and_over"
        else :
            inc     =   ""

        newcolname  =   "population_health_insurance_income" + inc + stype


    elif( (colnames[j].find("RATIO OF INCOME TO POVERTY LEVEL IN THE PAST 12 MONTHS") >-1) or
          (colnames[j].find("Below 50 percent of the poverty level") >-1) or 
          (colnames[j].find(" 50 to 99 percent of the poverty level") >-1) or 
          (colnames[j].find("100 to 149 percent of the poverty level") >-1) or 
          (colnames[j].find("150 to 199 percent of the poverty level") >-1) or
          (colnames[j].find("200 to 299 percent of the poverty level") >-1) or
          (colnames[j].find("At or above 300 percent of the poverty level") >-1) ) :


        if(colnames[j].find("Below 50 percent of the poverty level") >-1) :
            estat = "_below_50_pct_of_level_of_poverty"
        elif(colnames[j].find(" 50 to 99 percent of the poverty level") >-1) :
            estat = "_50_to_99_pct_of_level_of_poverty"
        elif(colnames[j].find("100 to 149 percent of the poverty level") >-1) :
            estat = "_100_to_149_pct_of_level_of_poverty"
        elif(colnames[j].find("150 to 199 percent of the poverty level") >-1) :
            estat = "_150_to_199_pct_of_level_of_poverty"
        elif(colnames[j].find("200 to 299 percent of the poverty level") >-1) :
            estat = "_200_to_299_pct_of_level_of_poverty"
        elif(colnames[j].find("At or above 300 percent of the poverty level") >-1) :
            estat = "_300_or_above_pct_of_level_of_poverty"
    
        else :
            estat = "_poverty"

        newcolname  =   "population_health_insurance_income" + estat + stype
        
    else :
        newcolname     =   colnames[j]

    if(j>3) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Education Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def clean_ACS_17_School_Enrollment(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Male;") >-1)) : 
        stype   =   "_male_percent"
    elif( (colnames[j].find("Male; Estimate;") >-1)) : 
        stype   =   "_male_total"
    elif( (colnames[j].find("Percent Female;") >-1)) : 
        stype   =   "_female_percent"
    elif( (colnames[j].find("Female; Estimate;") >-1)) : 
        stype   =   "_female_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Percent") >-1)) : 
        stype   =   "_percent"
    
    else :
        stype = ""
        
    if( (colnames[j].find("Population 3 years and over enrolled in school") >-1) or 
        (colnames[j].find("Nursery school, preschool") >-1) or 
        (colnames[j].find("Kindergarten to 12th grade") >-1) or
        (colnames[j].find("Kindergarten") >-1) or
        (colnames[j].find("grade 1 to grade 4") >-1) or
        (colnames[j].find("grade 5 to grade 8") >-1) or
        (colnames[j].find("grade 9 to grade 12") >-1) or 
        (colnames[j].find("College, undergraduate") >-1) or
        (colnames[j].find("Graduate, professional school") >-1) ) :
        
        if(colnames[j].find("Population 3 years and over enrolled in school") >-1) :
            schtype = "_3_years_and_over"
        elif(colnames[j].find("Nursery school, preschool") >-1) :
            schtype = "_nursery_school_preschool"
        elif(colnames[j].find("Kindergarten to 12th grade") >-1) :
            schtype = "_kindergarten_to_12th_grade"
        elif(colnames[j].find("Kindergarten") >-1) :
            schtype = "_kindergarten"
        elif(colnames[j].find("grade 1 to grade 4") >-1) :
            schtype = "_grade_1_to_4"
        elif(colnames[j].find("grade 5 to grade 8") >-1) :
            schtype = "_grade_5_to_8"
        elif(colnames[j].find("grade 9 to grade 12") >-1) :
            schtype = "_grade_9_to_12"
        elif(colnames[j].find("College, undergraduate") >-1) :
            schtype = "_college_undergraduate"
        elif(colnames[j].find("Graduate, professional school") >-1) :
            schtype = "_graduate_professional"
        else :
            schtype = ""
        
        if( (colnames[j].find("in public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In public school;") >-1)) :
            sch = "_public"
        
        elif( (colnames[j].find("In private school;") >-1)) :
            sch = "_private"
        elif( (colnames[j].find("in private school;") >-1)) :
            sch = "_private"
        else :        
            sch = ""
    
        newcolname = "school_enrollment" + schtype + sch + stype


    elif(colnames[j].find(" Population enrolled in college or graduate school") >-1) :
        
        schtype = "_college_or_graduate"
        
        if( (colnames[j].find("in public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In private school;") >-1)) :
            sch = "_private"
        elif( (colnames[j].find("in private school;") >-1)) :
            sch = "_private"
        else :        
            sch = ""

        if( (colnames[j].find(" Males enrolled") >-1)) :
            sex = "_male"
        elif( (colnames[j].find("Females enrolled") >-1)) :
            sex = "_female"
        else :        
            sex = ""

        newcolname = "school_enrollment" + schtype + sch + sex + stype


    elif( (colnames[j].find("Population 3 to 4 years") >-1) or 
          (colnames[j].find("Population 5 to 9 years") >-1) or 
          (colnames[j].find("Population 10 to 14 years") >-1) or
          (colnames[j].find("Population 15 to 17") >-1) or
          (colnames[j].find("Population 18 to 19 years") >-1) or
          (colnames[j].find("Population 20 to 24 years") >-1) or 
          (colnames[j].find("Population 25 to 34 years") >-1) or 
          (colnames[j].find("Population 35 years and over") >-1)):
        
        
        if(colnames[j].find("3 to 4 year olds enrolled in school") >-1) :
            age = "_enrolled_3_to_4"
        elif(colnames[j].find("Population 3 to 4 years") >-1) :
            age = "_population_3_to_4"
    
        elif(colnames[j].find("5 to 9 year olds enrolled in school") >-1) :
            age = "_enrolled_5_to_9"
        elif(colnames[j].find("Population 5 to 9 years") >-1) :
            age = "_population_5_to_9"
    
        elif(colnames[j].find("10 to 14 year olds enrolled in school") >-1) :
            age = "_enrolled_10_to_14"
        elif(colnames[j].find("Population 10 to 14 years") >-1) :
            age = "_population_10_to_14"
            
            
        elif(colnames[j].find("15 to 17 year olds enrolled in school") >-1) :
            age = "_enrolled_15_to_17"
        elif(colnames[j].find("15 to 17") >-1) :
            age = "_population_15_to_17"
            
            
        elif(colnames[j].find("18 and 19 year olds enrolled in school") >-1) :
            age = "_enrolled_18_to_19"
        elif(colnames[j].find("18 to 19 years") >-1) :
            age = "_population_18_to_19"
            
        elif(colnames[j].find("20 to 24 year olds enrolled in school") >-1) :
            age = "_enrolled_20_to_24"
        elif(colnames[j].find("20 to 24 years") >-1) :
            age = "_population_20_to_24"
            
        elif(colnames[j].find("25 to 34 year olds enrolled in school") >-1) :
            age = "_enrolled_25_to_34"
        elif(colnames[j].find("25 to 34 years") >-1) :
            age = "_population_25_to_34"
            
            
        elif(colnames[j].find("35 years and over enrolled in school") >-1) :
            age = "_enrolled_35_and_over"
        elif(colnames[j].find("35 years and over") >-1) :
            age = "_population_35_and_over"
            
        else :
            age = ""


        if( (colnames[j].find("in public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In private school;") >-1)) :
            sch = "_private"
        elif( (colnames[j].find("in private school;") >-1)) :
            sch = "_private"
        else :        
            sch = ""

        newcolname = "school_age" + age + sch + stype


    elif( (colnames[j].find("Population 18 to 24 years") >-1) or 
          (colnames[j].find("Males 18 to 24 years") >-1) or
          (colnames[j].find("Females 18 to 24 years") >-1) ):
        
        
        if( (colnames[j].find("Enrolled in college or graduate school") >-1)) :
            edu = "_college_or_graduate"
        else :        
            edu = ""
            
        if( (colnames[j].find("Males 18 to 24 years") >-1)) :
            sex = "_male"
        elif( (colnames[j].find("Females 18 to 24 years") >-1)) :
            sex = "_female"
    
        else :        
            sex = ""
            
        if( (colnames[j].find("in public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In public school;") >-1)) :
            sch = "_public"
        elif( (colnames[j].find("In private school;") >-1)) :
            sch = "_private"
        elif( (colnames[j].find("in private school;") >-1)) :
            sch = "_private"
        else :        
            sch = ""

        newcolname = "school_enrollment_age_18_to_24" + edu + sch + sex + stype



    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Bachelor_Degree_Major(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Male;") >-1)) : 
        stype   =   "_male_percent"
    elif( (colnames[j].find("Male; Estimate;") >-1)) : 
        stype   =   "_male_total"
    elif( (colnames[j].find("Percent Female;") >-1)) : 
        stype   =   "_female_percent"
    elif( (colnames[j].find("Female; Estimate;") >-1)) : 
        stype   =   "_female_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Percent") >-1)) : 
        stype   =   "_percent"
    
    else :
        stype = ""


        
    if( (colnames[j].find("Science and Engineering Related Fields") >-1) ) :
        major = "_science_engineering"
    elif( (colnames[j].find("Science and Engineering") >-1) ) :
        major = "_science_engineering_related_fields"

    elif( (colnames[j].find("Business") >-1) ) :
        major = "_business"
    elif( (colnames[j].find("Education") >-1) ) :
        major = "_education"
    elif( (colnames[j].find("Arts, Humanities and Others") >-1) ) :
        major = "_arts_humanities_other"
    elif( (colnames[j].find("Arts, Humanities and Others") >-1) ) :
        major = "_science_engineering_related_fields"
    else :
        major = ""
 

    if( (colnames[j].find("DETAILED AGE") >-1) ) :

        if( (colnames[j].find("25 to 39 years") >-1) ) :
            age     =   "_age_25_to_39"
        elif( (colnames[j].find("40 to 64 years") >-1) ) :
            age     =   "_age_40_to_64"
        elif( (colnames[j].find("65 years and over") >-1) ) :
            age     =   "_age_65_and_over"
        else :
            age = ""
        
        newcolname = "education_bachelor_major" + major + age + stype
            
    else :
        
        newcolname = "education_bachelor_major" + major + stype





    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_School_Enrollment_Graduate_Level(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if( (colnames[j].find("Estimate; Male") >-1)) : 
        stype   =   "_male_total"
    elif( (colnames[j].find("Estimate; Female") >-1)) : 
        stype   =   "_female_total"
    elif( (colnames[j].find("Estimate; Total:") >-1)) : 
        stype   =   "_total"
    else :
        stype = ""

    if( (colnames[j].find("Enrolled in public college or graduate school") >-1) ) :
        sch = "_public_college_graduate_school"
    elif( (colnames[j].find("Enrolled in private college or graduate school") >-1) ) :
        sch = "_private_college_graduate_school"
    elif( (colnames[j].find("Not enrolled in college or graduate school") >-1) ) :
        sch = "_not_enrolled"
    else :
        sch = ""


    if( (colnames[j].find("15 to 17 years") >-1) ) :
        age = "_age_15_to_17"
    elif( (colnames[j].find("18 to 24 years") >-1) ) :
        age = "_age_18_to_24"
    elif( (colnames[j].find("25 to 34 years") >-1) ) :
        age = "_age_25_to_34"
    elif( (colnames[j].find("35 years and over") >-1) ) :
        age = "_age_35_and_over"
    else :
        age = ""

        
    newcolname = "education_graduate_enrollment" + sch + age + stype





    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_School_Enrollment_Detailed(j,colnames,newcolnames,race) :
    
    #print("clean",j,colnames[j])
    
    newcolname  =   ""
    
    if(colnames[j].find("Male") >-1) :
        sex = "_male"
    elif(colnames[j].find("Female") >-1) :
        sex = "_female"
    else :
        sex = ""
    
    if(colnames[j].find("Public school") >-1) :
        schtype = "_public"
    elif(colnames[j].find("Private school") >-1) :
        schtype = "_private"
    else :
        schtype = ""
    
    if(colnames[j].find("Enrolled in school") >-1) :
        
        if( (colnames[j].find("Enrolled in nursery school, preschool") >-1) ) :
            sch = "_nursery_school_preschool"
        elif( (colnames[j].find("Enrolled in kindergarten") >-1) ) :
            sch = "_kindergarten"
        elif( (colnames[j].find("Enrolled in grade 10") >-1) ) :
            sch = "_grade_10"
        elif( (colnames[j].find("Enrolled in grade 11") >-1) ) :
            sch = "_grade_11"
        elif( (colnames[j].find("Enrolled in grade 12") >-1) ) :
            sch = "_grade_12"
        
        elif( (colnames[j].find("Enrolled in grade 1 to grade 4") >-1) ) :
            sch = "_grades_1_to_4"
        elif( (colnames[j].find("Enrolled in grade 1") >-1) ) :
            sch = "_grade_1"
        elif( (colnames[j].find("Enrolled in grade 2") >-1) ) :
            sch = "_grade_2"
        elif( (colnames[j].find("Enrolled in grade 3") >-1) ) :
            sch = "_grade_3"
        elif( (colnames[j].find("Enrolled in grade 4") >-1) ) :
            sch = "_grade_4"
        elif( (colnames[j].find("Enrolled in grade 5 to grade 8") >-1) ) :
            sch = "_grades_5_to_8"
    
        elif( (colnames[j].find("Enrolled in grade 5") >-1) ) :
            sch = "_grade_5"
        elif( (colnames[j].find("Enrolled in grade 6") >-1) ) :
            sch = "_grade_6"
        elif( (colnames[j].find("Enrolled in grade 7") >-1) ) :
            sch = "_grade_7"
        elif( (colnames[j].find("Enrolled in grade 8") >-1) ) :
            sch = "_grade_8"
        elif( (colnames[j].find("Enrolled in grade 9 to grade 12") >-1) ) :
            sch = "_grades_9_to_12"
            
        elif( (colnames[j].find("Enrolled in grade 9") >-1) ) :
            sch = "_grade_9"
        elif( (colnames[j].find("Enrolled in college, undergraduate years") >-1) ) :
            sch = "_college_undergraduate"
        elif( (colnames[j].find("Enrolled in college undergraduate years") >-1) ) :
            sch = "_college_undergraduate"
        
        elif( (colnames[j].find("Enrolled in graduate or professional school") >-1) ) :
            sch = "_graduate_or_professional"
        elif( (colnames[j].find("Graduate or professional school") >-1) ) :
            sch = "_graduate_or_professional"
        else :
            sch = "_enrolled_in_school"
            
    else :
        
        if( (colnames[j].find("Not enrolled in school") >-1) ) :
            sch = "_not_enrolled"
        else :
            sch = ""

        
    newcolname = "education_enrollment_" + race + sch + schtype + sex + "_total"

    if(j>1) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Educational_Attainment(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Male;") >-1)) : 
        stype   =   "_male_percent"
    elif( (colnames[j].find("Male; Estimate;") >-1)) : 
        stype   =   "_male_total"
    elif( (colnames[j].find("Percent Female;") >-1)) : 
        stype   =   "_female_percent"
    elif( (colnames[j].find("Female; Estimate;") >-1)) : 
        stype   =   "_female_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    else :
        stype = ""
        
    if( (colnames[j].find("MEDIAN EARNINGS IN THE PAST 12 MONTHS") >-1) ) :
        
        edu = get_education(j,colnames)
        
        if( (colnames[j].find("Male; Estimate;") >-1)) :
            sex = "_male"
        elif( (colnames[j].find("Female; Estimate;") >-1)) :
            sex = "_female"
        else :        
            sex = ""
    
        newcolname = "education_earnings" + edu + sex + "_median"
        
    elif( (colnames[j].find("Estimate; Population 18 to 24 years") >-1) or 
          (colnames[j].find("Estimate; Population 25 to 34 years") >-1) or 
          (colnames[j].find("Population 25 years and over") >-1) or 
          (colnames[j].find("Estimate; Population 35 to 44 years") >-1) or 
          (colnames[j].find("Estimate; Population 45 to 64 years") >-1) or 
          (colnames[j].find("Estimate; Population 65 years and over") >-1)) : 

        if( (colnames[j].find("Population 18 to 24 years") >-1)) :
            age = "_18_to_24"
        elif( (colnames[j].find("Population 25 years and over") >-1)) :
            age = "_25_and_over"
            
        elif( (colnames[j].find("Population 25 to 34 years") >-1)) :
            age = "_25_to_34"
        elif( (colnames[j].find("Population 35 to 44 years") >-1)) :
            age = "_35_to_44"
        elif( (colnames[j].find("Population 45 to 64 years") >-1)) :
            age = "_45_to_64"
        elif( (colnames[j].find("Population 65 years and over") >-1)) :
            age = "_65_and_over"
        else :        
            age = ""


        
        if( (colnames[j].find("Male; Estimate;") >-1)) :
            sex = "_male"
        elif( (colnames[j].find("Female; Estimate;") >-1)) :
            sex = "_female"
        else :        
            sex = ""
            
        edu = get_education(j,colnames)

        
        newcolname = "education_age" + age + edu + stype


    elif( (colnames[j].find("Percent high school graduate or higher") >-1) or 
          (colnames[j].find("Percent bachelor's degree or higher") >-1) ) :
        
        if(colnames[j].find("Percent high school graduate or higher") >-1) :
            if(colnames[j].find("Percent; Estimate;") >-1) :
                edu = "_high_school_graduate_or_higher_percent"
            elif( (colnames[j].find("Percent Male; Estimate;") >-1)) :
                edu = "_high_school_graduate_or_higher_male_percent"
            else :
                edu = "_high_school_graduate_or_higher_female_percent"
                
        elif( (colnames[j].find("Percent bachelor's degree or higher") >-1)) :
            if(colnames[j].find("Percent; Estimate;") >-1) :
                edu = "_bachelor_degree_or_higher_percent"
            elif( (colnames[j].find("Percent Male; Estimate;") >-1)) :
                edu = "_bachelor_degree_or_higher_male_percent"
            else :
                edu = "_bachelor_degree_or_higher_female_percent"

        else :        
            edu = ""

        newcolname = "education" + edu 

    
    
    elif( (colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN BY EDUCATIONAL ATTAINMENT ") >-1) or 
          (colnames[j].find("White alone") >-1) or 
          (colnames[j].find("White alone, not Hispanic or Latino") >-1) or 
          (colnames[j].find("Black alone") >-1) or 
          (colnames[j].find("American Indian or Alaska Native alone") >-1) or 
          (colnames[j].find("Asian alone") >-1) or 
          (colnames[j].find("Native Hawaiian and Other Pacific Islander alone") >-1) or 
          (colnames[j].find("Some other race alone") >-1) or 
          (colnames[j].find("Two or more races") >-1) or 
          (colnames[j].find("Hispanic or Latino Origin") >-1)) : 

        if( (colnames[j].find("High school graduate or higher") >-1)) :
            edu = "_high_school_graduate_or_higher"
        elif( (colnames[j].find("Bachelor's degree or higher") >-1)) :
            edu = "_bachelor_degree_or_higher"
        else :        
            edu = ""

        if( (colnames[j].find("Male; Estimate;") >-1)) :
            sex = "_male"
        elif( (colnames[j].find("Female; Estimate;") >-1)) :
            sex = "_female"
        else :        
            sex = ""

        race = get_race(j,colnames)
        
        newcolname = "education_race" + race + edu + stype
    
    
    elif( (colnames[j].find("POVERTY RATE FOR THE POPULATION") >-1) ) :
        
        
        edu = get_education(j,colnames)
    
        newcolname = "education_poverty" + edu + stype
    
    
    if(j>4) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Employment Files
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""


def clean_ACS_17_Employment_Characteristics(j,colnames,newcolnames) :
    
    newcolname  =   ""

    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Percent Families") >-1)) : 
        stype   =   "_percent"
    
    else :
        stype = "_total"


    if( (colnames[j].find("EMPLOYMENT STATUS CHARACTERISTICS") >-1)) :
        
        mstat = get_married_status(j,colnames) 
        ftype = get_family_type(j,colnames)   
        estat = get_emp_stat(j,colnames)

        newcolname  =   "families" + mstat + ftype + estat + stype

    elif( (colnames[j].find("Other families") >-1)) :
        
        
        if(colnames[j].find("Male householder, no wife present") >-1 ) :
            ftype1  =   "_male_no_wife"
        elif(colnames[j].find(" Female householder, no husband present") >-1 ) :
            ftype1  =   "_female_no_husband"
        else :
            ftype1 = ""
        
        if(colnames[j].find("Families with own children under 18 years") >-1 ) :
            ftype  =   "_own_children_under_18"
        else :
            ftype = ""
        
        estat = get_emp_stat(j,colnames)

        newcolname  =   "families_other" + ftype1 + ftype + estat + stype

    elif( (colnames[j].find("WORK STATUS CHARACTERISTICS") >-1)) :
        
        if(colnames[j].find("Male householder, no wife present - In labor force") >-1 ) :
            ftype1  =   "_male_not_in_labor_force_no_wife"
        
        elif(colnames[j].find("Male householder, no wife present") >-1 ) :
            ftype1  =   "_male_no_wife"
        elif(colnames[j].find(" Female householder, no husband present - Not in labor force") >-1 ) :
            ftype1  =   "_female_not_in_labor_force_no_husband"
    
        elif(colnames[j].find(" Female householder, no husband present") >-1 ) :
            ftype1  =   "_female_no_husband"
        else :
            ftype1 = ""
        
        if(colnames[j].find("Families with own children under 18 years") >-1 ) :
            ftype  =   "_own_children_under_18"
        else :
            ftype = ""
        
        wstat = get_worker_status(j,colnames)

        newcolname  =   "families_workers" + ftype1 + wstat + ftype + stype

    else :
        
        ftype = get_family_type(j,colnames)   
        wtype = get_work_type(j,colnames)
        
        newcolname  =   "families_householder" + wtype + ftype  + stype
        
    if(j>3) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Employment_Status(j,colnames,newcolnames) :
    
    newcolname  =   ""
    

    if( (colnames[j].find("AGE") >-1)) :
        
        age     =   get_age_range(j,colnames)
        
        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
        
        newcolname  =   "population_employment" + age + estat


    elif( (colnames[j].find("RACE AND HISPANIC OR LATINO ORIGIN") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        race    =   get_race(j,colnames)
        
        newcolname  =   "population_employment" + race + estat
    
    elif( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        race    =   "_white_alone_not_hispanic"
        
        newcolname  =   "population_employment" + race + estat

    elif( (colnames[j].find("Hispanic or Latino origin (of any race)") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        race    =   "_hispanic"
        
        newcolname  =   "population_employment" + race + estat
        
        
    elif( (colnames[j].find("POVERTY STATUS IN THE PAST 12 MONTHS ") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        if(colnames[j].find("Below poverty level") >-1) :
            pov = "_below_poverty_level"
        elif(colnames[j].find("At or above the poverty level") >-1) :
            pov = "_at_or_above_poverty_level"
            
        newcolname  =   "population_employment" + pov + estat
        

    elif( (colnames[j].find("DISABILITY STATUS") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        newcolname  =   "population_employment_with_any_disability" + estat


    elif( (colnames[j].find("EDUCATIONAL ATTAINMENT") >-1)) :

        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"
            
        edu = get_education(j,colnames)
        
        newcolname  =   "population_employment" + edu + estat


    else :
        
        if(colnames[j].find("Labor Force Participation Rate") >-1) :
            estat   =   "_labor_force_participation_percent"
        elif(colnames[j].find("Employment/Population Ratio") >-1) :
            estat   =   "_employed_percent"
        elif(colnames[j].find("Unemployment rate;") >-1) :
            estat   =   "_unemployed_percent"
        else :
            estat   =   "_total"

        
        if(colnames[j].find("Population 20 to 64 years") >-1) :
            age     =   "_20_to_64"
        elif(colnames[j].find("Population 20 to 64 years") >-1) :
            age     =   "_20_to_64"
        else :
            age = ""
            
        if(colnames[j].find("SEX - Male") >-1) :
            sex     =   "_male"
        elif(colnames[j].find("SEX - Female") >-1) :
            sex     =   "_female"
        else :
            sex = ""

        if(colnames[j].find("With own children under 18 years - With own children under 6 to 17 years only") >-1) :
            cage     =   "_own_children_6_to_17_only"

        elif(colnames[j].find("With own children under 18 years - With own children under 6 years and 6 to 17 years") >-1) :
            cage     =   "_own_children_6_to_17"
            
        elif(colnames[j].find("With own children under 6 years only") >-1) :
            cage     =   "_own_children_under_6_only"
        elif(colnames[j].find("With own children under 18 years") >-1) :
            cage     =   "_own_children_under_18"
            
        else :
            cage = ""
       
        newcolname  =   "population_employment" + age + sex + cage + estat



        
    if(j>5) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Occupation_Full_Time(j,colnames,newcolnames) :
    
    newcolname  =   ""
    

    if(colnames[j].find("Percent") >-1) :
        estat   =   "_percent"
    else :
        estat   =   "_total"
        
    ocu     =   get_occupation(j,colnames)
    
    if(colnames[j].find("Male") >-1) :
        sex     =   "_male"
    elif(colnames[j].find("Female") >-1) :
        sex     =   "_female"
    else :
        sex = ""
    
        
    newcolname  =   "population_employment_full_time" + sex + ocu + estat



    if(j>6) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)





def clean_ACS_17_Work_Status(j,colnames,newcolnames) :
    
    newcolname  =   ""
    

    if(colnames[j].find("Percent") >-1) :
        estat   =   "_percent"
    else :
        estat   =   "_total"
        
    if(colnames[j].find("WEEKS WORKED") >-1) : 
        
        wkwork  =   get_weeks_worked(j,colnames)
    
        if(colnames[j].find("Male") >-1) :
            sex     =   "_male"
        elif(colnames[j].find("Female") >-1) :
            sex     =   "_female"
        else :
            sex = ""
            
        newcolname  =   "population_employment_weeks_worked" + sex + wkwork + estat

    elif(colnames[j].find("USUAL HOURS WORKED") >-1) : 
        
        wkwork  =   get_weeks_worked(j,colnames)

        if(colnames[j].find("Usually worked 35 or more hours per week") >-1) :
            wkspan  =   "_35_or_more_hours_per_week" + wkwork
        elif(colnames[j].find("Usually worked 15 to 34 hours per week") >-1) :
            wkspan  =   "_15_to_34_hours_per_week" + wkwork
        elif(colnames[j].find("Usually worked 1 to 14 hours per week") >-1) :
            wkspan  =   "_1_to_14_hours_per_week" + wkwork
        elif(colnames[j].find("Did not work") >-1) :
            wkspan  =   "_did_not_work"
    
        else :
            wkspan = ""
       
        if(colnames[j].find("Male") >-1) :
            sex     =   "_male"
        elif(colnames[j].find("Female") >-1) :
            sex     =   "_female"
        else :
            sex = ""
            
        newcolname  =   "population_employment_usual_hours" + sex + wkspan + estat
            
        
    elif(colnames[j].find("Mean usual hours worked") >-1) : 
        
        if(colnames[j].find("Male") >-1) :
            sex     =   "_male"
        elif(colnames[j].find("Female") >-1) :
            sex     =   "_female"
        else :
            sex = ""
        
        newcolname  =   "population_employment_workers_age" + sex + "_mean"
        
    elif(colnames[j].find("Median age of workers") >-1) : 
        
        if(colnames[j].find("Male") >-1) :
            sex     =   "_male"
        elif(colnames[j].find("Female") >-1) :
            sex     =   "_female"
        else :
            sex = ""
        
        newcolname  =   "population_employment_workers_age" + sex + "_median"
        
    else :
        newcolname  =  colnames[j]    
    
 
    if(j>7) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



def clean_ACS_17_Worker_Class(j,colnames,newcolnames) :
    
    newcolname  =   ""
    

    if(colnames[j].find("Percent") >-1) :
        estat   =   "_percent"
    else :
        estat   =   "_total"

    if(colnames[j].find("Male") >-1) :
        sex     =   "_male"
    elif(colnames[j].find("Female") >-1) :
        sex     =   "_female"
    else :
        sex = ""

    wclass = get_class_of_worker(j,colnames)

    newcolname  =   "population_employed" + wclass + sex + estat


 
    if(j>6) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)



"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Demographics
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""



def clean_ACS_17_Population_Race_Sex_Age(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if( (colnames[j].find("Percent") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Sex ratio (males per 100 females)") >-1)) : 
        stype   =   "_males_per_100_females_ratio"
    elif( (colnames[j].find("Median age") >-1)) : 
        stype   =   "_median"
    elif( (colnames[j].find("Estimate; RACE - Total population") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; RACE - Total population") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Total population - Hispanic or Latino (of any race)") >-1)) : 
        if(colnames[j].find("Percent") >-1) :
            stype   = "_percent"
        else :
            stype   =   "_total"
    
    else :
        stype = "_total"

    if( (colnames[j].find("Male") >-1)) : 
        sex   =   "_male"
    elif( (colnames[j].find("Female") >-1)) : 
        sex   =   "_female"
    else : 
        sex   =   ""
    
    if(colnames[j].find("SEX AND AGE") >-1) :
        
        if(colnames[j].find("Under 5 years") >-1) :
            age  =   "_under_5"
        elif(colnames[j].find("5 to 9 years") >-1) :
            age  =   "_age_5_to_9"
        elif(colnames[j].find("10 to 14 years") >-1) :
            age  =   "_age_10_to_14"
        elif(colnames[j].find("15 to 19 years") >-1) :
            age  =   "_age_15_to_19"
        elif(colnames[j].find("20 to 24 years") >-1) :
            age  =   "_age_20_to_24"
        elif(colnames[j].find("25 to 34 years") >-1) :
            age  =   "_age_25_to_34" 
        elif(colnames[j].find("35 to 44 years") >-1) :
            age  =   "_age_35_to_44"
        elif(colnames[j].find("45 to 54 years") >-1) :
            age  =   "_age_45_to_54"
        elif(colnames[j].find("55 to 59 years") >-1) :
            age  =   "_55_to_59"
        elif(colnames[j].find("60 to 64 years") >-1) :
            age  =   "_60_to_64"
        elif(colnames[j].find("65 to 74 years") >-1) :
            age  =   "_65_to_74"
        elif(colnames[j].find("75 to 84 years") >-1) :
            age  =   "_75_to_84"
        elif(colnames[j].find("85 years and over") >-1) :
            age  =   "_85_and_over"
        elif(colnames[j].find("Under 18 years") >-1) :
            age  =   "_under_18"
        elif(colnames[j].find("16 years and over") >-1) :
            age  =   "_16_and_over"
        elif(colnames[j].find("18 years and over") >-1) :
            age  =   "_18_and_over"
        elif(colnames[j].find("21 years and over") >-1) :
            age  =   "_21_and_over"
        elif(colnames[j].find("62 years and over") >-1) :
            age  =   "_62_and_over"
        elif(colnames[j].find("65 years and over") >-1) :
            age  =   "_65_and_over"
        else :
            age = ""
    
        newcolname = "population" + age + sex + stype 

        
    if(colnames[j].find("HISPANIC OR LATINO AND RACE ") >-1) :
        
        race    =   get_race(j,colnames) 
        
        if(race == "") :
            race = "_hispanic"
        
        newcolname = "population" + race + sex + stype 
        
    elif(colnames[j].find("RACE") >-1) :
        
        race    =   get_race(j,colnames)        
        
        newcolname = "population_non_hispanic" + race + stype 
        
    elif(colnames[j].find("CITIZEN, VOTING AGE POPULATION") >-1) :
        
       newcolname =  "population_citizen" +sex + stype        
        
    

    if(j>3) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)


def clean_ACS_17_Population_Sex_Age(j,colnames,newcolnames) :
    
    newcolname  =   ""
    
    
    if( (colnames[j].find("Total; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent; Estimate;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Percent Male;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Male; Estimate;") >-1)) : 
        stype   =   "_total"
    elif( (colnames[j].find("Percent Female;") >-1)) : 
        stype   =   "_percent"
    elif( (colnames[j].find("Female; Estimate;") >-1)) : 
        stype   =   "_total"
    else :
        stype = "_total"

    if( (colnames[j].find("Male") >-1)) : 
        sex   =   "_male"
    elif( (colnames[j].find("Female") >-1)) : 
        sex   =   "_female"
    else : 
        sex   =   ""

    if( (colnames[j].find("SUMMARY INDICATORS") >-1)) : 
        
        if( (colnames[j].find("Median age (years)") >-1)) : 
            summ = "_age" + sex + "_median"
        elif( (colnames[j].find("Sex ratio (males per 100 females)") >-1)) : 
            summ = "_males_per_100_females_ratio"
        elif( (colnames[j].find("Age dependency ratio") >-1)) : 
            summ = "_age_dependency_ratio"
        elif( (colnames[j].find("Old-age dependency ratio") >-1)) : 
            summ = "_old_age_dependency_ratio"
        elif( (colnames[j].find("Child dependency ratio") >-1)) : 
            summ = "_child_dependency_ratio"
        else :
            summ = ""
            
        newcolname = "population" + summ            
        
    else : 

        age = get_age(j,colnames)
        newcolname  =   "population" + age + sex + stype


    if(j>4) :
        newcolnames.append(newcolname)
    else :
        newcolname  =  colnames[j] 
        newcolnames.append(newcolname)
    
    print("newcolname",newcolname,j)




"""
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
                            Common Utilities
* ------------------------------------------------------------------------
* ------------------------------------------------------------------------
"""

def get_age(j,colnames) :
    
    if( (colnames[j].find("AGE - Under 5 years") >-1)) : 
        age = "_under_5"
    elif( (colnames[j].find("AGE - 5 to 9 years") >-1)) : 
        age = "_5_to_9"
    elif( (colnames[j].find("AGE - 10 to 14 years") >-1)) : 
        age = "_10_to_14"
    elif( (colnames[j].find("AGE - 15 to 19 years") >-1)) : 
        age = "_15_to_19"
    elif( (colnames[j].find("AGE - 20 to 24 years") >-1)) : 
        age = "_20_to_24"
    elif( (colnames[j].find("AGE - 25 to 29 years") >-1)) : 
        age = "_25_to_29"
    elif( (colnames[j].find("AGE - 30 to 34 years") >-1)) : 
        age = "_30_to_34"
    elif( (colnames[j].find("AGE - 35 to 39 years") >-1)) : 
        age = "_35_to_39"
    elif( (colnames[j].find("AGE - 40 to 44 years") >-1)) : 
        age = "_40_to_44"
    elif( (colnames[j].find("AGE - 45 to 49 years") >-1)) : 
        age = "_45_to_49"
    elif( (colnames[j].find("AGE - 50 to 54 years") >-1)) : 
        age = "_50_to_54"
    elif( (colnames[j].find("AGE - 55 to 59 years") >-1)) : 
        age = "_55_to_59"
    elif( (colnames[j].find("AGE - 60 to 64 years") >-1)) : 
        age = "_60_to_64"
    elif( (colnames[j].find("AGE - 65 to 69 years") >-1)) : 
        age = "_65_to_69"
    elif( (colnames[j].find("AGE - 70 to 74 years") >-1)) : 
        age = "_70_to_74"
    elif( (colnames[j].find("AGE - 75 to 79 years") >-1)) : 
        age = "_75_to_79"
    elif( (colnames[j].find("AGE - 80 to 84 years") >-1)) : 
        age = "_80_to_84"
    elif( (colnames[j].find("AGE - 85 years and over") >-1)) : 
        age = "_85_and_over"
    elif( (colnames[j].find("Under 18 years") >-1)) : 
        age = "_under_18"
    elif( (colnames[j].find("16 years and over") >-1)) : 
        age = "_16_and_over"
    elif( (colnames[j].find("18 years and over") >-1)) : 
        age = "_18_and_over"
    elif( (colnames[j].find("21 years and over") >-1)) : 
        age = "_21_and_over"
    elif( (colnames[j].find("65 years and over") >-1)) : 
        age = "_65_and_over"
    else :
        age = ""
        
    return(age)
        

def get_occupation(j,colnames) :

        if( (colnames[j].find("Management, business, science, and arts occupations") >-1)) :
            if( (colnames[j].find("Management, business, and financial occupations") >-1)) :
                if( (colnames[j].find("Management, business, and financial occupations: - Management occupations") >-1)) :
                    ocu = "_management"
                elif( (colnames[j].find("Management, business, and financial occupations: - Business and financial operations occupations") >-1)) :
                    ocu = "_business_financial"
                else :
                    ocu = "_management_business_financial"
                    
            elif( (colnames[j].find("Computer, engineering, and science occupations:") >-1)) :
                if( (colnames[j].find("Computer and mathematical occupations") >-1)) :
                    ocu = "_computer_mathematical"
                elif( (colnames[j].find("Architecture and engineering occupations") >-1)) :
                    ocu = "_architecture_engineering"
                elif( (colnames[j].find("Life, physical, and social science occupations") >-1)) :
                    ocu = "_life_physical_social_science"
                else :
                    ocu = "_computer_engineering_science"
                    
            elif( (colnames[j].find("Education, legal, community service, arts, and media occupations") >-1)) :
                if( (colnames[j].find("Community and social services occupations") >-1)) :
                    ocu = "_community_social_services"
                elif( (colnames[j].find("Legal occupations") >-1)) :
                    ocu = "_legal"
                elif( (colnames[j].find("Education, training, and library occupations") >-1)) :
                    ocu = "_education_training_library"
                elif( (colnames[j].find("Arts, design, entertainment, sports, and media occupations") >-1)) :
                    ocu = "_arts_design_entertainment_sports_media"
                else :
                    ocu = "_education_legal_community_service_arts_media"
                
            elif( (colnames[j].find("Healthcare practitioner and technical occupations") >-1)) :
                if( (colnames[j].find(" Health diagnosing and treating practitioners and other technical occupations") >-1)) :
                    ocu = "_health_diagnostics_treating_practitioners_other"
                elif( (colnames[j].find("Health technologists and technicians") >-1)) :
                    ocu = "_health_technologists_technician"
                else :
                    ocu = "_healthcare_practitioner_technical"
            
            else :
                ocu   =   "_management_business_science_and_arts"
                
        elif( (colnames[j].find("Service occupations") >-1)) :
            
            if( (colnames[j].find("Healthcare support occupations") >-1)) :
                ocu = "_healthcare_support"
            elif( (colnames[j].find("Protective service occupations") >-1)) :
                if( (colnames[j].find("Fire fighting and prevention, and other protective service workers including supervisors") >-1)) :
                    ocu = "_firefighters"
                elif( (colnames[j].find("Law enforcement workers including supervisors") >-1)) :
                    ocu = "_law_enforcement"
                else :
                    ocu = "_protective_services"
                    
            elif( (colnames[j].find("Food preparation and serving related occupations") >-1)) :
                ocu = "_food_services"
                
            elif( (colnames[j].find("Building and grounds cleaning and maintenance occupations") >-1)) :
                ocu = "_building_and_grounds_maintenance"
                
            elif( (colnames[j].find("Personal care and service occupations") >-1)) :
                ocu = "_personal_care"
                
            else :
                ocu = "_service"
            
        elif( (colnames[j].find("Sales and office occupations") >-1)) :
            
            if( (colnames[j].find("Sales and related occupations") >-1)) :
                ocu = "_sales_related"
            elif( (colnames[j].find("Office and administrative support occupations") >-1)) :
                ocu = "_office_administrative"
            else :
                ocu = "_sales_and_office"
            
        elif( (colnames[j].find("Natural resources, construction, and maintenance occupations") >-1)) :
            
            if( (colnames[j].find("Farming, fishing, and forestry occupations") >-1)) :
                ocu = "_farming_fishing_forestry"
            elif( (colnames[j].find("Construction and extraction occupations") >-1)) :
                ocu = "_construction_extraction"
            elif( (colnames[j].find("Installation, maintenance, and repair occupations") >-1)) :
                ocu = "_installation_maintenance_repair"
            else :
                ocu = "_natural_resources_construction_maintenance"
            
        elif( (colnames[j].find("Production, transportation, and material moving occupations") >-1)) :
            
            if( (colnames[j].find("Production occupations") >-1)) :
                ocu = "_production"
            elif( (colnames[j].find("Transportation occupations") >-1)) :
                ocu = "_transportation"
            elif( (colnames[j].find("Material moving occupations") >-1)) :
                ocu = "_material_moving"
            else :
                ocu = "_production_transportation_material_moving"
        elif( (colnames[j].find("Military specific occupations") >-1)) :
            ocu = "_military"    
                
        else :
            ocu = ""
            

        return(ocu)


def get_industry(colnames,j) :
    
    
    if( (colnames[j].find("Agriculture, forestry, fishing and hunting, and mining:") >-1)) :
        if(colnames[j].find("Agriculture, forestry, fishing and hunting, and mining: - Agriculture, forestry, fishing and hunting") >-1) :
            ocu     =   "_agriculture_forestry_fishing_hunting"
        elif(colnames[j].find("Agriculture, forestry, fishing and hunting, and mining: - Mining, quarrying, and oil and gas extraction") >-1) :
            ocu    =   "_mining_quarrying_and_oil_and_gas_extraction"
        else :
            ocu     =   "_agriculture_forestry_fishing_hunting_and_mining"
            
            
    elif( (colnames[j].find("Construction") >-1)) : 
        ocu   =   "_construction"
    elif( (colnames[j].find("Manufacturing") >-1)) : 
        ocu   =   "_manufacturing"
    elif( (colnames[j].find("Wholesale trade") >-1)) : 
        ocu   =   "_wholesale_trade"
    elif( (colnames[j].find("Retail trade") >-1)) : 
        ocu   =   "_retail_trade"
    elif( (colnames[j].find("Transportation and warehousing, and utilities") >-1)) : 
        if( (colnames[j].find("Transportation and warehousing, and utilities: - Transportation and warehousing") >-1)) :    
            ocu   =   "_transportation_and_warehousing"
        elif( (colnames[j].find("Transportation and warehousing, and utilities: - Utilities") >-1)) :    
            ocu   =   "_utilities"
        else :
            ocu   =   "_transportation_warehousing_utilities"
    elif( (colnames[j].find("Information") >-1)) : 
        ocu   =   "_information"
    elif( (colnames[j].find("Finance and insurance, and real estate and rental and leasing") >-1)) : 
        if( (colnames[j].find("Finance and insurance, and real estate and rental and leasing: - Finance and insurance") >-1)) :    
            ocu   =   "_finance_insurance"
        elif( (colnames[j].find("Finance and insurance, and real estate and rental and leasing: - Real estate and rental and leasing") >-1)) :    
            ocu   =   "_real_estate_rental_leasing"
        else :
            ocu   =   "_finance_insurance_real_estate_rental_leasing"
    
    elif( (colnames[j].find("Professional, scientific, and management, and administrative and waste management services") >-1) or 
          (colnames[j].find("Professional, scientific, management, and administrative and waste management services") >-1)) : 
        if( (colnames[j].find("Professional, scientific, and management, and administrative and waste management services: - Professional, scientific, and technical services") >-1)) :    
            ocu   =   "_professional_scientific_technical"
        elif( (colnames[j].find("Professional, scientific, and management, and administrative and waste management services: - Management of companies and enterprises") >-1)) :    
            ocu   =   "_management_of_companies_and_enterprises"
        elif( (colnames[j].find("Professional, scientific, and management, and administrative and waste management services: - Administrative and support and waste management services") >-1)) :    
            ocu   =   "_administrative_waste_management_services"
        else :
            ocu   =   "_professional_scientific_management_administrative_waste_management_services"
       
    elif( (colnames[j].find("Educational services, and health care and social assistance") >-1)) : 
        if( (colnames[j].find("Educational services, and health care and social assistance: - Educational services") >-1)) :    
            ocu   =   "_educational_services"
        elif( (colnames[j].find("Educational services, and health care and social assistance: - Health care and social assistance") >-1)) :    
            ocu   =   "_health_care_social_assistance"
        else :
            ocu   =   "_educational_services_health_care_social_assistance"
        
    elif( (colnames[j].find("Arts, entertainment, and recreation, and accommodation and food services") >-1)) :
        if( (colnames[j].find("Arts, entertainment, and recreation, and accommodation and food services: - Arts, entertainment, and recreation") >-1)) :    
            ocu   =   "_arts_entertainment_recreation"
        elif( (colnames[j].find("Arts, entertainment, and recreation, and accommodation and food services: - Accommodation and food services") >-1)) :    
            ocu   =   "_accommodation_food_services"
        else :
            ocu   =   "_arts_entertainment_recreation_accommodation_food_services"


    elif( (colnames[j].find("Other services, except public administration") >-1) or 
          (colnames[j].find("Other services, except public administration") >-1) ) : 
        ocu   =   "_other_services_except_public_administration"
    
    elif( (colnames[j].find("Public administration") >-1) ) : 
        ocu   =   "_other_services_except_public_administration"
 
    elif( (colnames[j].find("Armed forces") >-1) ) : 
        ocu   =   "_armed_forces"
    
    
    else :
        ocu = ""

    return(ocu)    
 

def get_income(j,colnames) :

    if( (colnames[j].find("$1 to $9,999 or loss") >-1)) : 
        inc   =   "_1_to_9999_or_loss"
    elif( (colnames[j].find("$10,000 to $14,999") >-1)) : 
        inc   =   "_10000_to_14999"
    elif( (colnames[j].find(" $15,000 to $24,999") >-1)) : 
        inc   =   "_15000_to_24999"
    elif( (colnames[j].find("$25,000 to $34,999") >-1)) : 
        inc   =   "_25000_to_34999"
    elif( (colnames[j].find("$35,000 to $49,999") >-1)) : 
        inc   =   "_35000_to_49999"
    elif( (colnames[j].find("$50,000 to $64,999") >-1)) : 
        inc   =   "_50000_to_64999"
    elif( (colnames[j].find("$65,000 to $74,999") >-1)) : 
        inc   =   "_65000_to_74999"
    elif( (colnames[j].find("$75,000 or more") >-1)) : 
        inc   =   "_75000_and_over"
    else :
        inc = "_with_income"

    return(inc)


def get_education(j,colnames) :
    
    if( (colnames[j].find("Graduate or professional degree") >-1)) : 
        edu   =   "_graduate_or_professional"
    elif( (colnames[j].find("Bachelor's degree or higher") >-1)) : 
        edu   =   "_bachelor_or_higher"
    elif( (colnames[j].find("Bachelor's degree") >-1)) : 
        edu   =   "_bachelor"
    elif( (colnames[j].find("High school graduate or higher") >-1)) : 
        edu   =   "_high_school_or_higher"
    
    
    elif( (colnames[j].find("Some college or associate's degree") >-1)) : 
        edu   =   "_some_college_or_associate"
    elif( (colnames[j].find("High school graduate (includes equivalency)") >-1)) : 
        edu   =   "_high_school"
    elif( (colnames[j].find("Less than high school graduate") >-1)) : 
        edu   =   "_less_than_high_school"
    elif( (colnames[j].find("Less than 9th grade") >-1)) : 
        edu   =   "_less_than_9th_grade"
    elif( (colnames[j].find("Associate's degree") >-1)) : 
        edu   =   "_associate_degree"
    elif( (colnames[j].find("Some college, no degree") >-1)) : 
        edu   =   "_some_college_no_degree"
    elif( (colnames[j].find(" 9th to 12th grade, no diploma") >-1)) : 
        edu   =   "_9th_to_12th_grade_no_diploma"
    
    else :
        edu = ""

    return(edu)


def get_education_age(j,colnames) :
    
    if( (colnames[j].find("18 to 24 years") >-1)) : 
        edu   =   "_16_to_19"
    elif( (colnames[j].find("25 years and over") >-1)) : 
        edu   =   "_20_to_24"
    elif( (colnames[j].find("High school graduate (includes equivalency)") >-1)) : 
        edu   =   "_25_to_44"
    elif( (colnames[j].find("Less than high school graduate") >-1)) : 
        edu   =   "_45_to_54"
    else :
        edu = ""

    return(edu)

def get_place_of_work(j,colnames) :

    if( (colnames[j].find("Worked in county of residence") >-1)) :
        plow   =   "_in_county"
    elif( (colnames[j].find("Worked in state of residence - Worked outside county of residence") >-1)) :
        plow   =   "_outside_county"
    elif( (colnames[j].find("Worked in state of residence") >-1)) :
        plow   =   "_in_state"
    elif( (colnames[j].find("Worked outside state of residence") >-1)) :
        plow   =   "_out_of_state"
    else:
        plow = ""
 
    return(plow)


def get_class_of_worker(j,colnames) :

    if( (colnames[j].find("Employee of private company workers") >-1)) :
        wclass   =   "_private_for_profit_company_worker"
    elif( (colnames[j].find("Self-employed in own incorporated business workers") >-1)) :
        wclass   =   "_self_employed_for_profit_incorporated_worker"
    elif( (colnames[j].find("Private for-profit wage and salary workers") >-1)) :
        wclass   =   "_private_for_profit_workers"
            
    elif( (colnames[j].find("Private not-for-profit wage and salary workers") >-1)) :
        wclass   =   "_private_not_for_profit_workers"
    elif( (colnames[j].find("Government workers") >-1)) :
        wclass   =   "_government_workers"
    
    elif( (colnames[j].find("Local government workers") >-1)) :
        wclass   =   "_local_government_workers"
    elif( (colnames[j].find("State government workers") >-1)) :
        wclass   =   "_state_government_workers"
    elif( (colnames[j].find("Federal government workers") >-1)) :
        wclass   =   "_federal_government_workers"
    elif( (colnames[j].find("Self-employed workers in own not incorporated business") >-1)) :
        wclass   =   "_self_employed_not_incorporated_worker"
    elif( (colnames[j].find("Self-employed in own not incorporated business workers and unpaid family workers") >-1)) :
        wclass   =   "_self_employed_not_incorporated_or_unpaid_worker"
    
    elif( (colnames[j].find("Unpaid family workers") >-1)) :
        wclass   =   "_unpaid_family_workers"
    else:
        wclass = ""
 
    return(wclass)


def get_race(j,colnames) :
    
    if( (colnames[j].find("White alone") >-1)) : 
        race   =   "_white"
    elif( (colnames[j].find("White alone, not Hispanic or Latino") >-1)) : 
        race   =   "_white_alone_not_hispanic"
    elif( (colnames[j].find("Black alone") >-1)) : 
        race   =   "_black"
    elif( (colnames[j].find("Black or African American alone") >-1)) : 
        race   =   "_black"
    
    elif( (colnames[j].find("American Indian or Alaska Native alone") >-1)) : 
        race   =   "_native_american"
    elif( (colnames[j].find("American Indian and Alaska Native alone") >-1)) : 
        race   =   "_native_american"

    elif( (colnames[j].find("Asian alone") >-1)) : 
        race   =   "_asian"
    elif( (colnames[j].find("Native Hawaiian and Other Pacific Islander alone") >-1)) : 
        race   =   "_hawaiian_pacific"
    elif( (colnames[j].find("Some other race alone") >-1)) : 
        race   =   "_other"
    elif( (colnames[j].find("Two or more races") >-1)) : 
        
        if(colnames[j].find("Two or more races - White and Black or African American") >-1) :
            race    =   "_white_and_black"
        elif(colnames[j].find("Two or more races - White and American Indian and Alaska Native") >-1) :
            race    =   "_white_and_native_american"
        elif(colnames[j].find("Two or more races - White and Asian") >-1) :
            race    =   "_white_and_asian"
        elif(colnames[j].find("Two or more races - Black or African American and American Indian and Alaska Native") >-1) :
            race    =   "_black_and_native_american"
        elif(colnames[j].find("Two or more races - Black or African American and American Indian and Alaska Native") >-1) :
            race    =   "_black_and_native_american"
        else :
            race   =   "_mixed"
            
    elif( (colnames[j].find("Hispanic or Latino Origin") >-1)) :
        race   =   "_hispanic"
    
    elif( (colnames[j].find("Hispanic or Latino (of any race)") >-1)) :
        
        if(colnames[j].find("Hispanic or Latino (of any race) - Mexican") >-1) :
            race    =   "_hispanic_any_mexican"
        elif(colnames[j].find("Hispanic or Latino (of any race) - Puerto Rican") >-1) :
            race    =   "_hispanic_any_puerto_rican"
        elif(colnames[j].find("Hispanic or Latino (of any race) - Cuban") >-1) :
            race    =   "_hispanic_any_cuban"
        elif(colnames[j].find("Hispanic or Latino (of any race) - Other Hispanic or Latino") >-1) :
            race    =   "_hispanic_any_other"
        else :
            race   =   "_hispanic_any"
        
    elif( (colnames[j].find("Not Hispanic or Latino") >-1)) :
            race   =   "_not_hispanic"
        
        
        
    elif( (colnames[j].find("One race - White") >-1)) : 
        race   =   "_white"
    elif( (colnames[j].find("One race - Black or African American") >-1)) : 
        race   =   "_black"
    elif( (colnames[j].find("One race - American Indian and Alaska Native") >-1)) : 
        
        if(colnames[j].find("Cherokee tribal grouping") >-1) :
            race    =   "_cherokee"
        elif(colnames[j].find("Chippewa tribal grouping") >-1) :
            race    =   "_chippewa"
        elif(colnames[j].find("Navajo tribal grouping") >-1) :
            race    =   "_navajo"
        elif(colnames[j].find(" Sioux tribal grouping") >-1) :
            race    =   "_sioux"
        else :
            race   =   "_native_american"
            
    elif( (colnames[j].find("One race - Asian") >-1)) : 
        
        if(colnames[j].find("Asian - Asian Indian") >-1) :
            race    =   "_asian_indian"
        elif(colnames[j].find("Asian - Chinese") >-1) :
            race    =   "_chinese"
        elif(colnames[j].find("Asian - Filipino") >-1) :
            race    =   "_filipino"
        elif(colnames[j].find("Asian - Japanese") >-1) :
            race    =   "_japanese"
        elif(colnames[j].find("Asian - Korean") >-1) :
            race    =   "_korean"
        elif(colnames[j].find("Asian - Vietnamese") >-1) :
            race    =   "_vietnamese"
        elif(colnames[j].find("Other Asian") >-1) :
            race    =   "_other_asian"
        else :
            race   =   "_asian"
       
    elif( (colnames[j].find("One race - Native Hawaiian and Other Pacific Islander") >-1)) : 

        if(colnames[j].find("One race - Native Hawaiian and Other Pacific Islander - Native Hawaiian") >-1) :
            race    =   "_hawaiian"
        elif(colnames[j].find("One race - Native Hawaiian and Other Pacific Islander - Guamanian or Chamorro") >-1) :
            race    =   "_guamanian_chamorro"
        elif(colnames[j].find("One race - Native Hawaiian and Other Pacific Islander - Samoan") >-1) :
            race    =   "_samoan"
        elif(colnames[j].find("One race - Native Hawaiian and Other Pacific Islander - Other Pacific Islander") >-1) :
            race    =   "_other_pacific_islander"
        else :
            race   =   "_hawaiian_pacific"

    elif( (colnames[j].find("One race - Some other race") >-1)) : 
        race   =   "_other_race"

    elif( (colnames[j].find("One race") >-1)) : 
        race   =   "_single_race"

    else :
        race = ""

    return(race)
 
    
def get_family_type(j,colnames) :

    if(colnames[j].find("With children under 18 years - Other family: - Male householder, no wife present") >-1 ) :
        ftype  =   "_other_male_no_wife_children_under_18"
    elif(colnames[j].find("With children under 18 years - Other family: - Female householder, no husband present") >-1 ) :
        ftype  =   "_other_female_no_husband_children_under_18"
    elif(colnames[j].find("No children under 18 years - Married-couple family") >-1 ) :
        ftype  =   "_married_no_children_under_18"
        
    elif(colnames[j].find("Percent Families with own children under 18 years") >-1 ) :
        ftype  =   "_own_children_under_18"
    elif(colnames[j].find("Families with own children under 18 years") >-1 ) :
        ftype  =   "_own_children_under_18"
          
         
    elif(colnames[j].find("No children under 18 years - Other family: - Male householder, no wife present") >-1 ) :
        ftype  =   "_other_male_no_wife_no_children_under_18"
    elif(colnames[j].find("No children under 18 years - Other family: - Female householder, no husband present") >-1 ) :
        ftype  =   "_other_female_no_husband_no_children_under_18"
    
    elif(colnames[j].find(" No children under 18 years - Other family:") >-1 ) :
        ftype  =   "_other_no_children_under_18"
    elif(colnames[j].find("No children under 18 years - Nonfamily households") >-1 ) :
        ftype  =   "_non_family_no_children_under_18"
            
    elif(colnames[j].find("No children under 18 years") >-1 ) :
        ftype  =   "_no_children_under_18"

    elif( (colnames[j].find("Married-couple family") >-1 ) ):
        ftype  =   "_married_couple"
    elif(colnames[j].find("With children under 18 years - Other family:") >-1 ) :
        ftype  =   "_other_with_children_under_18"
            
    elif( (colnames[j].find("Other family") >-1 )):
        ftype  =   "_other"
    elif(colnames[j].find("Male householder, no wife present") >-1 ) :
        ftype  =   "_male_no_wife"
    elif(colnames[j].find(" Female householder, no husband present") >-1 ) :
        ftype  =   "_female_no_husband"
    elif(colnames[j].find("Nonfamily households") >-1 ) :
        ftype  =   "_non_family"
    elif(colnames[j].find("With children under 18 years - Married-couple family") >-1 ) :
        ftype  =   "_married_couple_with_children_under_18"
    
    elif( (colnames[j].find("With children under 18 years") >-1)) :
        ftype  =   "_children_under_18"
    else :
        ftype = ""

    return(ftype)

def get_family_stat(j,colnames) :
    
    if( (colnames[j].find("Other families") >-1) ):
        ftype  =   "_other"
    
    else :
        ftype = ""
        
    return(ftype)
    
    
def get_married_status(j,colnames) :

    if(colnames[j].find("Married-couple families") >-1 ) : 
        size = "_married_couple"
    if(colnames[j].find("Married-couple") >-1 ) : 
        size = "_married_couple"
        
    elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years - Under 6 years and 6 to 17 years") >-1 ) : 
        size = "_own_children_6_to_17"
    elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years - Under 6 years only") >-1 ) : 
        size = "_own_children_under_6"
    elif(colnames[j].find("With related children of householder under 18 years - With own children of householder under 18 years") >-1 ) : 
        size = "_own_children_under_18"
    elif(colnames[j].find("With related children of householder under 18 years") >-1 ) : 
        size = "_related_children_under_18"
    elif(colnames[j].find("No related children of householder under 18 years") >-1 ) : 
        size = "_no_related_children_under_18"
    else :
        size = ""

    return(size)

def get_marrital_status(j,colnames) :

    if(colnames[j].find("Now married, except separated") >-1) :
        mstat     =   "_now_married_except_separated"
    elif(colnames[j].find("Widowed") >-1) :
        mstat     =   "_widowed"
    elif(colnames[j].find("Divorced") >-1) :
        mstat     =   "_divorced"
    elif(colnames[j].find("Separated") >-1) :
        mstat     =   "_separated"
    elif(colnames[j].find("Never married") >-1) :
        mstat     =   "_never_married"
    else :
        mstat = "" 
        
    return(mstat)


def get_emp_stat(j,colnames) :

    if(colnames[j].find("Husband in labor force, wife not in labor force") >-1 ) : 
        estat = "_husband_in_labor_force_wife_not_in_labor_force"
    elif(colnames[j].find("Wife in labor force, husband not in labor force") >-1 ) : 
        estat = "_wife_in_labor_force_husband_not_in_labor_force"
    elif(colnames[j].find("Both husband and wife not in labor force") >-1 ) : 
        estat = "_both_husband_and_wife_not_in_labor_force"
    elif(colnames[j].find("Both husband and wife in labor force") >-1 ) : 
        estat = "_both_husband_and_wife_in_labor_force"
    else :
        estat = ""

    return(estat)


def get_householder_stat(j,colnames) :

    if(colnames[j].find("Female householder, no husband present") >-1 ) : 
        estat = "_female_no_husband"
    elif(colnames[j].find("Male householder, no wife present") >-1 ) : 
        estat = "_male_no_wife"
    else :
        estat = ""

    return(estat)

def get_worker_status(j,colnames) :

    if(colnames[j].find("No workers in the past 12 months") >-1 ) : 
        estat = "_no_workers"
    elif(colnames[j].find("1 worker in the past 12 months") >-1 ) : 
        estat = "_1_worker"
    elif(colnames[j].find("2 or more workers in the past 12 months") >-1 ) : 
        estat = "_2_or_more_workers"
    else :
        estat = ""

    return(estat)

def get_work_type(j,colnames) :

    if(colnames[j].find("Householder worked full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_full_time"
    elif(colnames[j].find("Spouse worked full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_full_time_spouse_full_time"
    elif(colnames[j].find("Spouse worked less than full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_full_time_spouse_part_time"
    elif(colnames[j].find("Spouse did not work in the past 12 months") >-1 ) : 
        estat = "_worked_spouse_did_not_work"
    elif(colnames[j].find("Householder worked less than full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_part_time"
    elif(colnames[j].find("Householder worked less than full-time, year-round in the past 12 months: - Spouse worked full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_part_time_spouse_full_time"
    elif(colnames[j].find("Householder worked less than full-time, year-round in the past 12 months: - Spouse worked less than full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_worked_part_time_spouse_part_time"
    elif(colnames[j].find("Householder worked less than full-time, year-round in the past 12 months: - Spouse did not work in the past 12 months") >-1 ) : 
        estat = "_worked_part_time_spouse_did_not_work"
    elif(colnames[j].find("Householder did not work in the past 12 months") >-1 ) : 
        estat = "_worked_did_not_work"
    elif(colnames[j].find("Householder did not work in the past 12 months: - Spouse worked full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_did_not_work_spouse_full_time"
    elif(colnames[j].find("Householder did not work in the past 12 months: - Spouse worked less than full-time, year-round in the past 12 months") >-1 ) : 
        estat = "_did_not_work_spouse_part_time"
    elif(colnames[j].find("Householder did not work in the past 12 months: - Spouse did not work in the past 12 months") >-1 ) : 
        estat = "_did_not_work_spouse_did_not_work"
        
        
        
    else :
        estat = ""

    return(estat)


def get_age_range(j,colnames) :

    if(colnames[j].find("AGE - 16 to 19 years") >-1 ) : 
        age = "_16_to_19"
    elif(colnames[j].find("AGE - 20 to 24 years") >-1 ) : 
        age = "_20_to_24"
    elif(colnames[j].find("AGE - 25 to 29 years") >-1 ) : 
        age = "_25_to_29"
    elif(colnames[j].find("AGE - 30 to 34 years") >-1 ) : 
        age = "_30_to_34"
    elif(colnames[j].find("AGE - 35 to 44 years") >-1 ) : 
        age = "_35_to_44"
    elif(colnames[j].find("AGE - 45 to 54 years") >-1 ) : 
        age = "_45_to_54"
    elif(colnames[j].find("AGE - 55 to 59 years") >-1 ) : 
        age = "_55_to_59"
    elif(colnames[j].find("AGE - 60 to 64 years") >-1 ) : 
        age = "_60_to_64"
    elif(colnames[j].find("AGE - 65 to 74 years") >-1 ) : 
        age = "_65_to_74"
    elif(colnames[j].find("AGE - 75 years and over") >-1 ) : 
        age = "_75_and_over"
    else :
        age = ""

    return(age)


def get_weeks_worked(j,colnames) :
    
    if(colnames[j].find("50 to 52 weeks") >-1) : 
        wlen    =   "_50_to_52_weeks"
    elif(colnames[j].find("48 to 49 weeks") >-1) : 
        wlen    =   "_48_to_49_weeks"
    elif(colnames[j].find("40 to 47 weeks") >-1) : 
        wlen    =   "_40_to_47_weeks"
        
    elif(colnames[j].find("27 to 39 weeks") >-1) : 
        wlen    =   "_27_to_39_weeks"
    elif(colnames[j].find("14 to 26 weeks") >-1) : 
        wlen    =   "_14_to_26_weeks"
    elif(colnames[j].find("1 to 13 weeks") >-1) : 
        wlen    =   "_1_to_13_weeks"
    elif(colnames[j].find("Did not work") >-1) : 
        wlen    =   "_did_not_work"
    else :
        wlen = ""
    
    return(wlen)








def clean_raw() :
    
    opstat          =   opStatus()
    
    import os
    import pandas
    
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\")
    
    raw_files   =       ["ACS_17_Health_Insurance_Private_Sex_Age.csv"] 

    economic_files  =   ["ACS_17_Mean_Income.csv","ACS_17_Income.csv","ACS_17_Income_Median.csv","ACS_17_Earnings.csv"]                

    housing_files   =       ["ACS_17_Housing_Occupied_Chars.csv","ACS_17_Housing_Financial.csv","ACS_17_Housing_Demo.csv",
                             "ACS_17_Housing_Occupancy.csv"]                 

    place_of_birth_files  =       ["ACS_17_Place_Of_Birth_Foreign_Born.csv","ACS_17_Place_Of_Birth_Asian.csv","ACS_17_Place_Of_Birth_Black.csv","ACS_17_Place_Of_Birth_Hawaiin_Pacific.csv",
                             "ACS_17_Place_Of_Birth_Hispanic.csv","ACS_17_Place_Of_Birth_Mixed.csv","ACS_17_Place_Of_Birth_Native_American.csv",
                             "ACS_17_Place_Of_Birth_Other.csv","ACS_17_Place_Of_Birth_White.csv","ACS_17_Place_Of_Birth_White_Not_Hispanic.csv",
                             "ACS_17_Place_Of_Birth.csv","ACS_17_Place_Of_Birth_Marital_Status.csv"]                    

    nativity   =       ["ACS_17_Nativity_White.csv","ACS_17_Nativity_White_Not_Hispanic.csv",
                         "ACS_17_Nativity_All_Races.csv","ACS_17_Nativity_Other.csv"
                         "ACS_17_Nativity_Native_American.csv","ACS_17_Nativity_Mixed.csv"
                         "ACS_17_Nativity_White_Not_Hispanic.csv","ACS_17_Nativity_White.csv"
                         "ACS_17_Nativity_Hispanic.csv","ACS_17_Black_Nativity.csv","ACS_17_Asian_Nativity.csv"]


    processed   =       ["ACS_17_Languages.csv","ACS_17_Veteran_Status.csv","ACS_17_Poverty.csv",
                         "ACS_17_Marital_Status.csv","ACS_17_Food_Stamps.csv",
                         "ACS_17_Feritility.csv","ACS_17_Disability.csv",
                         "ACS_17_Earnings.csv","ACS_17_Economic.csv",
                         "ACS_17_Income.csv","ACS_17_Income_Median.csv","ACS_17_Industry_Full_Time.csv",
                         "ACS_17_Mean_Income.csv","ACS_17_Median_Earning_Industry.csv"]
    
    for i in range(len(raw_files)) :
        
        #try :
        raw_df     =   pandas.read_csv(dfc_census_path+"working\\" + raw_files[i])
        print(raw_files[i],len(raw_df))
        #except Exception as e:
        #    opstat.set_status(False)
        #    opstat.store_exception("error importing demographics data",e)
            
        colnames    =    raw_df.columns.tolist()
        print(raw_files[i]," cols : ",len(colnames))
        
        newcolnames     =   []
        for j in range(len(colnames)) :
            
            #print("colnames[j]",colnames[j])
            
            if(colnames[j].find("Margin of Error")>-1) :
                raw_df.drop(colnames[j],axis=1,inplace=True)
            else :
                
                if(raw_files[i] == "ACS_17_Disability.csv") :
                    clean_ACS_17_Disability(j,colnames,newcolnames) 
                elif(raw_files[i] == "ACS_17_Feritility.csv") :
                    clean_ACS_17_Fertility(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Food_Stamps.csv") :
                    clean_ACS_17_Foodstamps(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Marital_Status.csv") :
                    clean_ACS_17_MaritalStatus(j,colnames,newcolnames) 
                elif(raw_files[i] == "ACS_17_Poverty.csv") :    
                    clean_ACS_17_Poverty(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Veteran_Status.csv") :    
                    clean_ACS_17_Veteran_Status(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Languages.csv") :    
                    clean_ACS_17_Languages(j,colnames,newcolnames) 
                elif(raw_files[i] == "ACS_17_Asian_Nativity.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"asian") 
                elif(raw_files[i] == "ACS_17_Black_Nativity.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"black") 
                elif(raw_files[i] == "ACS_17_Nativity_Hispanic.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"hispanic") 
                elif(raw_files[i] == "ACS_17_Nativity_White.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"white") 
                elif(raw_files[i] == "ACS_17_Nativity_White_Not_Hispanic.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"white_not_hispanic") 
                elif(raw_files[i] == "ACS_17_Nativity_Mixed.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"mixed") 
                elif(raw_files[i] == "ACS_17_Nativity_Native_American.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"native_american") 
                elif(raw_files[i] == "ACS_17_Nativity_Other.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"other") 
                elif(raw_files[i] == "ACS_17_Nativity_All_Races.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"all_races") 
                elif(raw_files[i] == "ACS_17_Nativity_Median_Age.csv") :    
                    clean_ACS_17_Nativity(j,colnames,newcolnames,"all_races",True)
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Asian.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"asian")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Black.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"black")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Hawaiin_Pacific.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"hawaiin_pacific")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Hispanic.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"hispanic")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Mixed.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"mixed")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Native_American.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"native_american")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Other.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"other")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_White.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"white")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_White_Not_Hispanic.csv") :    
                    clean_ACS_17_Place_Of_Birth(j,colnames,newcolnames,"white_not_hispanic")
                elif(raw_files[i] == "ACS_17_Place_Of_Birth.csv") :    
                    clean_ACS_17_Place_Of_Birth_1(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Marital_Status.csv") :    
                    clean_ACS_17_Place_Of_Birth_MS(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Place_Of_Birth_Foreign_Born.csv") :    
                    get_countries(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Housing_Occupancy.csv") :    
                    clean_ACS_17_Housing_Occupancy(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Housing_Demo.csv") :    
                    clean_ACS_17_Housing_Demo(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Housing_Financial.csv") :    
                    clean_ACS_17_Housing_Financial(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Housing_Occupied_Chars.csv") :    
                    clean_ACS_17_Housing_Chars(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Earnings.csv") :    
                    clean_ACS_17_Earnings(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Income_Median.csv") :    
                    clean_ACS_17_Income_Median(j,colnames,newcolnames)
                elif(raw_files[i] == "ACS_17_Income.csv") :    
                    clean_ACS_17_Income(j,colnames,newcolnames)                    
                elif(raw_files[i] == "ACS_17_Mean_Income.csv") :    
                    clean_ACS_17_Mean_Income(j,colnames,newcolnames)                    
                elif(raw_files[i] == "ACS_17_Health_Insurance_Private_Sex_Age.csv") :    
                    clean_ACS_17_Mean_Income(j,colnames,newcolnames)                    
                    
                    
                    
                    
        print("raw_df",len(raw_df.columns),len(newcolnames))
        #print(newcolnames)
                    
        raw_df.columns  =   newcolnames
        raw_df.to_csv(dfc_census_path + "working\\" + "fixed_" + raw_files[i],index=False)
        print("fixed_"+ raw_files[i] + " : ",len(raw_df),len(raw_df.columns.tolist()))
        #print(raw_df.columns)




    
    
    
    
    
    



