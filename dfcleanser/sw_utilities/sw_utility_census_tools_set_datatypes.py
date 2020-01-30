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
  
import dfcleanser.sw_utilities.sw_utility_census_tools_model as swctm
import dfcleanser.sw_utilities.sw_utility_census_model as swcm


def add_missing_zips(raw_df) :
    
    ZTCAS =  ['ZCTA5 00601', 'ZCTA5 00602', 'ZCTA5 00603', 'ZCTA5 00606', 'ZCTA5 00610', 
              'ZCTA5 00612', 'ZCTA5 00616', 'ZCTA5 00617', 'ZCTA5 00622', 'ZCTA5 00623', 'ZCTA5 00624', 
              'ZCTA5 00627', 'ZCTA5 00631', 'ZCTA5 00637', 'ZCTA5 00638', 'ZCTA5 00641', 'ZCTA5 00646', 
              'ZCTA5 00647', 'ZCTA5 00650', 'ZCTA5 00652', 'ZCTA5 00653', 'ZCTA5 00656', 'ZCTA5 00659',
              'ZCTA5 00660', 'ZCTA5 00662', 'ZCTA5 00664', 'ZCTA5 00667', 'ZCTA5 00669', 'ZCTA5 00670', 
              'ZCTA5 00674', 'ZCTA5 00676', 'ZCTA5 00677', 'ZCTA5 00678', 'ZCTA5 00680', 'ZCTA5 00682', 
              'ZCTA5 00683', 'ZCTA5 00685', 'ZCTA5 00687', 'ZCTA5 00688', 'ZCTA5 00690', 'ZCTA5 00692', 
              'ZCTA5 00693', 'ZCTA5 00694', 'ZCTA5 00698', 'ZCTA5 00703', 'ZCTA5 00704', 'ZCTA5 00705', 
              'ZCTA5 00707', 'ZCTA5 00714', 'ZCTA5 00715', 'ZCTA5 00716', 'ZCTA5 00717', 'ZCTA5 00718', 
              'ZCTA5 00719', 'ZCTA5 00720', 'ZCTA5 00723', 'ZCTA5 00725', 'ZCTA5 00727', 'ZCTA5 00728', 
              'ZCTA5 00729', 'ZCTA5 00730', 'ZCTA5 00731', 'ZCTA5 00735', 'ZCTA5 00736', 'ZCTA5 00738', 
              'ZCTA5 00739', 'ZCTA5 00740', 'ZCTA5 00741', 'ZCTA5 00745', 'ZCTA5 00751', 'ZCTA5 00754', 
              'ZCTA5 00757', 'ZCTA5 00765', 'ZCTA5 00766', 'ZCTA5 00767', 'ZCTA5 00769', 'ZCTA5 00771', 
              'ZCTA5 00772', 'ZCTA5 00773', 'ZCTA5 00775', 'ZCTA5 00777', 'ZCTA5 00778', 'ZCTA5 00780', 
              'ZCTA5 00782', 'ZCTA5 00783', 'ZCTA5 00784', 'ZCTA5 00786', 'ZCTA5 00791', 'ZCTA5 00794', 
              'ZCTA5 00795', 'ZCTA5 00901', 'ZCTA5 00906', 'ZCTA5 00907', 'ZCTA5 00909', 'ZCTA5 00911',
              'ZCTA5 00912', 'ZCTA5 00913', 'ZCTA5 00915', 'ZCTA5 00917', 'ZCTA5 00918', 'ZCTA5 00920', 
              'ZCTA5 00921', 'ZCTA5 00923', 'ZCTA5 00924', 'ZCTA5 00925', 'ZCTA5 00926', 'ZCTA5 00927', 
              'ZCTA5 00934', 'ZCTA5 00936', 'ZCTA5 00949', 'ZCTA5 00950', 'ZCTA5 00951', 'ZCTA5 00952', 
              'ZCTA5 00953', 'ZCTA5 00956', 'ZCTA5 00957', 'ZCTA5 00959', 'ZCTA5 00960', 'ZCTA5 00961', 
              'ZCTA5 00962', 'ZCTA5 00965', 'ZCTA5 00966', 'ZCTA5 00968', 'ZCTA5 00969', 'ZCTA5 00971', 
              'ZCTA5 00976', 'ZCTA5 00979', 'ZCTA5 00982', 'ZCTA5 00983', 'ZCTA5 00985', 'ZCTA5 00987'] 
    
    id2s =   [601,602,603,606,610,612,616,617,622,623,624,627, 631,637,638,641,646,647,650,652,653,656,659,
              660,662,664,667,669,670, 
              674,676,677,678,680,682, 
              683,685,687,688,690,692, 
              693,694,698,703,704,705, 
              707,714,715,716,717,718, 
              719,720,723,725,727,728, 
              729,730,731,735,736,738, 
              739,740,741,745,751,754, 
              757,765,766,767,769,771, 
              772,773,775,777,778,780, 
              782,783,784,786,791,794, 
              795,901,906,907,909,911,
              912,913,915,917,918,920, 
              921,923,924,925,926,927, 
              934,936,949,950,951,952, 
              953,956,957,959,960,961, 
              962,965,966,968,969,971, 
              976,979,982,983,985,987] 


    colnames    =    raw_df.columns.tolist()
    
    import pandas
    new_df      =   pandas.DataFrame(columns=colnames)
    
    us_row      =   raw_df.iloc[0]
    
    #print("us row",type(us_row),us_row)
    
    blank_df    =   pandas.DataFrame({"Id2":id2s, "Zip Code":ZTCAS}) 
    
    new_df      =   new_df.append(us_row, ignore_index = True)   
    new_df      =   new_df.append(blank_df, ignore_index = True) 
    
    raw_df.drop(raw_df.index[0],inplace=True)
    
    new_df      =   new_df.append(raw_df, ignore_index = True)
    
    print("new df",new_df.shape)
    #print(new_df.head())

    return(new_df)

def get_dif_zips(master,sample) :
    
    diffs   =   []
     
    if(len(master) > len(sample)) :
        
        for i in range(len(master)) :
            if(not(master[i] in sample)) :
                diffs.append(master[i])
                
    else :
        
        for i in range(len(sample)) :
            if(not(sample[i] in master)) :
                diffs.append(sample[i])
    
    print("diffs",len(diffs))            
    return(diffs)
        


def check_uniques() :
    
    import os
    import pandas
    
    opstat          =   opStatus()
   
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   os.path.join(dfc_census_path,"working","GoldenCleaned")
    dfc_census_path    =   dfc_census_path + "\\"
    
    master_zips  =   []
    
    for i in range(len(swctm.census_data_dirs)) :
        
        if(i==0) :
            files_list  =   swctm.work_files
            dups    =   []
        elif(i==1) :
            files_list  =   swctm.education_files
            dups        =   []
        elif(i==2) :
            files_list  =   swctm.transportation_files
            dups    =   []
           
        elif(i==3) :
            files_list  =   swctm.health_insurance_files
            dups        =   []

        elif(i==4) :
            files_list  =   swctm.internet_files
        elif(i==5) :
            files_list  =   swctm.economic_files
            dups    =   []
            
        elif(i==6) :
            files_list  =   swctm.housing_files
            dups        =   []
            

        elif(i==7) :
            files_list  =   swctm.immigration_files
            dups        =  []
            
        elif(i==8) :
            files_list  =   swctm.social_files
            dups        =   []
        
        elif(i==9) :
            files_list  =   swctm.population_files
            dups        =   []
        
        print("\n\nFixed Dir : ",swctm.census_data_dirs[i],"\n")
        
        dups_match  =   {}
        
        for j in range(len(files_list)) :
            
            raw_df  =   None
            
            opstat.set_status(True)
            
            try :
                raw_df     =   pandas.read_csv(dfc_census_path + swctm.census_data_dirs[i] + "\\fixed_" + files_list[j])
            except :
                opstat.set_status(False)
            
            if(opstat.get_status()) :
                
                import numpy as np
                colnames    =    raw_df.columns.tolist()
                npcolnames  =    np.array(colnames) 
                ucolnames   =    np.unique(npcolnames)
                
                unmatched_zips  =   []
                
                if((i==0)and(j==0)) :
                    master_zips     =   raw_df["Id2"]
                    master_ztacs    =   raw_df["Zip Code"]
                    current_zips    =   raw_df["Id2"]
                else :
                    current_zips    =   raw_df["Id2"]
                    current_ztacs   =   raw_df["Zip Code"]
                    
                    if(len(master_zips) == len(current_zips)) :
                        for k in range(len(current_zips)) :
                            if(not (current_zips[k] == master_zips[k])) :
                                if( not (k==0)) :
                                    unmatched_zips.append([k,master_zips[k],current_zips[k]])
                                    
                    else :
                        print("master len : ",len(master_zips)," current zips len : ",len(current_zips)," diff : ",(len(current_zips)-len(master_zips)))
                        #diffs   =   get_dif_zips(master_ztacs,current_ztacs)

                        #for q in range(100) :
                        #    print("q",q,master_zips[q],current_zips[q])

                        #for k in range(len(master_zips)) :
                            
                            #if(not (current_zips[k] == master_zips[k])) :
                            #    if( not (k==0)) :
                            #        print("no match",k,master_zips[k],current_zips[k])
 
                            
                if( (len(unmatched_zips) > 0) or (not (len(master_zips) == len(current_zips))) ) :
                    note = " Unmatched zips "
                else :
                    note = " all zips match"
                    
                print(files_list[j]," : ",len(raw_df)," : ",len(colnames)," : ",len(ucolnames),note)
                #if(note == " Unmatched zips ") :
                #    print(diffs)
                
                #if(note == " Unmatched zips ") :
                #    print(unmatched_zips)
                    
                if(j==0) :
                    cat_colnames    =   colnames
                else :
                    for m in range(len(colnames)) :
                        if(not ( (colnames[m] == cat_colnames[0]) or (colnames[m] == cat_colnames[1]) )) :
                            cat_colnames.append(colnames[m])
                            
                            
                for w in range(len(dups)) :
                    
                    dupselem    =  dups_match.get(dups[w],None)
                    
                    if(dups[w] in colnames) :
                    
                        if(dupselem is None) :
                            dups_match.update({dups[w]:[files_list[j]]})
                        else :
                        
                            dupselem.append(files_list[j])
                            dups_match.update({dups[w]:dupselem})
                        

            else :
                
                print("no df")
                
        npcat_colnames  =    np.array(cat_colnames) 
        ucat_colnames   =    np.unique(npcat_colnames)

        print("cat summaries : ",len(cat_colnames),len(ucat_colnames),"\n")
        
        if(not (len(cat_colnames) == len(ucat_colnames)) ) :
            for p in set(cat_colnames):
                if cat_colnames.count(p) > 1:
                    print(p, cat_colnames.index(p))
            
        if(len(dups_match) > 0) :

            print("\ndups_found")
            dupskeys    =   list(dups_match.keys())
            dupskeys.sort()
            
            dups_keys_cols   =   []
            
            for w in range(len(dupskeys)) :
                dupslist    =   dups_match.get(dupskeys[w])
                
                print("\n   ",dupskeys[w])
                
                dups_cols   =   []
                for z in range(len(dupslist)) :
                    print("      ",dupslist[z])
        
                
                    new_df      =   pandas.read_csv(dfc_census_path + swctm.census_data_dirs[i] + "\\fixed_" + dupslist[z])
                    new_col     =   new_df[dupskeys[w]]
                    
                    dups_cols.append(new_col)
            
                check_match_cols(dupskeys[w],dupslist,dups_cols)
            
            
            
            
            
def check_match_cols(colname,dupslist,dups_cols) :           
            
    for i in range(len(dups_cols)) :

        if(i==0) :
            master_list     =   dups_cols[0]
        else :
            match = True
            for j in range(len(master_list)) :
                
                if( not (dups_cols[i][j] == master_list[j])) :
                    print("\n        dup_comp column : ",colname,"\n           ",dupslist[i]," does not match master ",dupslist[0]," at ",j)
                    print("           ",dups_cols[i][j],"  ",master_list[j])
                    match = False
                    #print("dup_cols : ",j," does not match master")
                    break;
            
            if(match) :
                print("\n        dup_comp column : ",colname,"\n           ",dupslist[i]," does match master ",dupslist[0])
            

drop_dups   =   [None,
                 {"ACS_17_School_Enrollment_3_And_Over_Sex":["population_age_3_and_over_total"]},
                 None,
                 {"ACS_17_Health_Insurance_Public_Coverage":["population_health_insurance_total"]},
                 None,
                 None,
                 {"ACS_17_Housing_Occupancy":["occupied_housing_units_total","owner_occupied_housing_units_total","renter_occupied_housing_units_total"],
                  "ACS_17_Housing_Occupied_Chars":["occupied_housing_units_total","owner_occupied_housing_units_total","renter_occupied_housing_units_total"]},
                 None,
                 {"ACS_17_Population_Under_18":["population_under_18_total"]}]




            
def concat_census_files() :           


    import os
    import pandas
    
    opstat          =   opStatus()
    
    for k in range(len(swctm.census_data_dirs)) :
        
        
        print("\n\nmerging",swctm.census_data_dirs[k])
    
        dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
        dfc_census_path     =   os.path.join(dfc_census_path,"working","GoldenCleaned")
        dfc_census_path     =   os.path.join(dfc_census_path,swctm.census_data_dirs[k])
            
        files_list          =   swctm.census_data_dir_files[k]
    
        merged_df   =   pandas.DataFrame()
    
        for i in range(len(files_list)) :
        
            if(1):#try :
                print("  importing",files_list[i])#,"\n    ",dfc_census_path + "\\fixed_" + files_list[i])
                raw_df     =   pandas.read_csv(dfc_census_path + "\\fixed_" + files_list[i])
                
            #except :
            #    opstat.set_status(False)
            
            
            if(1):#opstat.get_status()) :
            
                
                if(1):#try :
                
                    if(not (i==0)) :
                        raw_df.drop(["Id2","Zip Code"],axis=1,inplace=True)
                    
                    
                    print("    merging imported ",files_list[i],len(raw_df),len(raw_df.columns))

                    #cdrop_dups  =   drop_dups[i]
                    
                    #dupcols     =   cdrop_dups.get(files_list[i],None)
                    
                    #if(not(dupcols is None)) :
                        
                    #    raw_df.drop(dupcols,axis=1,inplace=True)
                            
                    
                
                    merged_df   =   pandas.concat([merged_df,raw_df],axis=1)
                
                #except :
                #    opstat.set_status(False)    
        
        if(1):#opstat.get_status()) :
                
            dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
            dfc_census_path    =   os.path.join(dfc_census_path,"working","GoldenMerged")
            dfc_census_path    =   dfc_census_path + "\\"
                
            merged_df.to_csv(dfc_census_path + "merged_" + swctm.census_data_dirs[k] + ".csv",index=False)
            
            import numpy as np
            colnames    =    merged_df.columns.tolist()
            npcolnames  =    np.array(colnames) 
            ucolnames   =    np.unique(npcolnames)

            
            
            print("\nmerged_"+ swctm.census_data_dirs[k] + " : ",len(merged_df),len(merged_df.columns),len(ucolnames))
        
  


def build_census_indexes() :           
    
    import os
    import pandas
    import numpy as np
 
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   os.path.join(dfc_census_path,"working","county_zips_template.csv")
    
    czips_df            =   pandas.read_csv(dfc_census_path)#,encoding='latin-1')

    
    states_dict         =   {} 
    cities_dict         =   {}
    counties_dict       =   {}
    
    for i in range(len(czips_df)) :
        
        current_zip         =   czips_df.iloc[i,0]
        current_city        =   czips_df.iloc[i,1]
        current_state_id    =   czips_df.iloc[i,2]
        current_state       =   czips_df.iloc[i,3]
        current_county      =   czips_df.iloc[i,4]
        
        cstate  =   states_dict.get(current_state_id,None)
        
        if(cstate is None) :
            
            county_dict        =   {current_county:[current_zip]}
            city_dict          =   {current_city:[current_zip]}
            county_city_dict   =   {current_county:[current_city]}
            
            states_dict.update({current_state_id:[county_dict,city_dict,county_city_dict]})
            
        else :
            
            county_dict         =   cstate[0]
            county_zip_list     =   county_dict.get(current_county,None)
            
            if(county_zip_list is None) :
                county_dict.update({current_county:[current_zip]})
            else :
                county_zip_list.append(current_zip)  
                county_dict.update({current_county:county_zip_list})
                
            
            city_dict           =   cstate[1]
            city_zip_list       =   city_dict.get(current_city,None)
            
            if(city_zip_list is None) :
                city_dict.update({current_city:[current_zip]})
            else :
                city_zip_list.append(current_zip)  
                city_dict.update({current_city:city_zip_list})


            county_city_dict       =   cstate[2]
            county_city_list       =   county_city_dict.get(current_county,None)
            
            if(county_city_list is None) :
                county_city_dict.update({current_county:[current_city]})
            else :
                
                if(not(current_city in county_city_list)) :
                    county_city_list.append(current_city)
                    county_city_dict.update({current_county:county_city_list})
                    
            states_dict.update({current_state_id:[county_dict,city_dict,county_city_dict]})
                
                
    states  =   list(states_dict.keys())
    states.sort() 

    for i in range(len(states)) :
        
        cstate          =   states_dict.get(states[i])
        
        ccounties_dict  =   cstate[0]
        ccities_dict    =   cstate[1]
        
        print(states[i]," counties : ",str(len(ccounties_dict))," cities : ",str(len(ccities_dict)))
        
        
        if(i<2) :
            
            ccounties       =   list(ccounties_dict.keys())
            ccounties.sort()
        
            county_count = 6
        
            county_names    =   []
            county_zips     =   []
        
            for k in range(len(ccounties)) :
            
                if(not((k == 0)) and ((k%county_count)==0)) :
                
                    out_string  =   ""
                    for l in range(len(county_names)) :
                        out_string  =   out_string + str(county_names[l]) + " " + str(county_zips[l]) + " : "
                    
                    print(states[i]," : ",out_string)
                    county_names    =   []
                    county_zips     =   []
        
                else :
                
                    county_names.append(ccounties[k])
                    zips_list   =   ccounties_dict.get(ccounties[k])
                    county_zips.append(len(zips_list))

















def clean_float_cols(merged_df,non_numerics,non_numerics_ids) :
    
    import numpy as np
    
    non_numerics_bad_vals   =   []
    bad_not_percent         =   []  
        
    tot_bad_vals            =   0
        
    for l in range(len(non_numerics)) :
            
        if( (non_numerics[l].endswith("_percent")) or
           (non_numerics[l].endswith("_mean")) or 
           (non_numerics[l].endswith("_median")) ):
            
            bad_vals    =   0
            bad_vals_dict           =   {}
                
            for m in range(len(merged_df)) :
                    
                try :
                    cdata   =   float(merged_df.iloc[m,non_numerics_ids[l]])
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_ids[l]]:cdata})
                except :
                    bad_vals = bad_vals + 1
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_ids[l]]:np.nan})
                        
            tot_bad_vals    = tot_bad_vals+bad_vals
            non_numerics_bad_vals.append(bad_vals)
                
            merged_df.replace({non_numerics[l]:bad_vals_dict},inplace=True)
            merged_df.astype({non_numerics[l]: 'float'},errors='ignore').dtypes
                        
        else :
            bad_not_percent.append(non_numerics[l])
    
    
def clean_int_cols(merged_df,non_numerics,non_numerics_ids) :
    
    import numpy as np
    
    non_numerics_bad_vals   =   []
    bad_not_percent         =   []  
        
    tot_bad_vals            =   0
        
    for l in range(len(non_numerics)) :
            
        if( (non_numerics[l].endswith("_percent")) or
           (non_numerics[l].endswith("_mean")) or 
           (non_numerics[l].endswith("_median")) ):
            
            bad_vals    =   0
            bad_vals_dict           =   {}
                
            for m in range(len(merged_df)) :
                    
                try :
                    cdata   =   int(merged_df.iloc[m,non_numerics_ids[l]])
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_ids[l]]:cdata})
                except :
                    bad_vals = bad_vals + 1
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_ids[l]]:np.nan})
                        
            tot_bad_vals    = tot_bad_vals+bad_vals
            non_numerics_bad_vals.append(bad_vals)
                
            merged_df.replace({non_numerics[l]:bad_vals_dict},inplace=True)
            merged_df.astype({non_numerics[l]: 'float'},errors='ignore').dtypes
                        
        else :
            bad_not_percent.append(non_numerics[l])
    


def print_datasets_stats(all_census_data_dirs,i,dfc_census_path,merged_df,colnames) :
    
    import json
    
    print(all_census_data_dirs[i]," : data")
    with open(dfc_census_path+"\\"+ all_census_data_dirs[i]+'colnames.txt', 'w') as outfile:
        json.dump(colnames, outfile)
    
    from dfcleanser.common.common_utils import  get_dtype_str_for_datatype 
          
    dftypes      =   merged_df.dtypes.tolist() 
    dftypes_str  =   []
            
    for p in range(len(dftypes)) :
        dtstr   =   get_dtype_str_for_datatype(dftypes[p])
        dftypes_str.append(dtstr)
                
    with open(dfc_census_path+"\\"+ all_census_data_dirs[i]+'dtypes.txt', 'w') as outfile:
        json.dump(dftypes_str, outfile)
        
        
    dfnans  =   merged_df.isnull().sum(axis = 0).tolist()
    with open(dfc_census_path+"\\"+ all_census_data_dirs[i]+'nanscount.txt', 'w') as outfile:
        json.dump(dfnans, outfile)
    
    
    


def check_dup_columns() :  


    import os
    import pandas
    
    all_census_data_dirs    =   ["economic","education","employment","health_insurance","housing","immigration","internet","population","social","transportation"]
    census_data_dirs        =   ["immigration"]
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   os.path.join(dfc_census_path,"working","GoldenMerged")
    
    
    

    #merged_df       =   pandas.read_csv(dfc_census_path+"\\"+ "merged_" + all_census_data_dirs[5] + ".csv")#,encoding='latin-1')
    #colnames        =   merged_df.columns.tolist()
    
    
    #process_dup_columns(dfc_census_path,colnames,merged_df,all_census_data_dirs,5)    
 
   
    #return()
    

    
    all_census_data_dirs    =   ["immigration"]#"economic","education","employment","health_insurance","housing","immigration","internet","population","social","transportation"]
    census_data_dirs        =   ["immigration"]
    
    for i in range(len(all_census_data_dirs)) :
        
        print("check column names",all_census_data_dirs[i])
        
        merged_df       =   pandas.read_csv(dfc_census_path+"\\"+ "typed_" + all_census_data_dirs[i] + ".csv")#,encoding='latin-1')
        colnames        =   merged_df.columns.tolist()
        
        print(len(colnames))
        
        dfccolnames     =   swcm.get_census_colnames(all_census_data_dirs[i])
        
        if(len(colnames) == len(dfccolnames)) :
            
            for j in range(len(colnames)) :
                
                if(not(colnames[j] == dfccolnames[j])) :
                    print("column name mismatch : ",colnames[j],dfccolnames[j])
        
        else :
            
            print("colnames len mismatch : ",len(colnames),len(dfccolnames))
            
            if(len(colnames) > len(dfccolnames)) :
                
                for j in range(len(colnames)) :
                    if(not(colnames[j] in dfccolnames)) :
                        print(colnames[j])
                        
            else :
                
                for j in range(len(colnames)) :
                    if( (j>250) and (j< 280) ):
                        print("[",j,"] ",dfccolnames[j]," : ",colnames[j])
                
                #for j in range(len(dfccolnames)) :
                #    if(not(dfccolnames[j] in colnames)) :
                #        print(dfccolnames[j])
            
            #print(colnames)
                
        print_datasets_stats(all_census_data_dirs,i,dfc_census_path,merged_df,colnames)
         
        return()
        
        if(not(all_census_data_dirs[i] in census_data_dirs)) :
            print("skip",all_census_data_dirs[i])
            print_datasets_stats(all_census_data_dirs,i,dfc_census_path,merged_df,colnames)
            
        else :
            process_dup_columns(dfc_census_path,colnames,merged_df,all_census_data_dirs,i)    
        
        
def process_dup_columns(dfc_census_path,colnames,merged_df,census_data_dirs,i) : 
    
    import numpy as np
    from dfcleanser.common.common_utils import is_numeric_col
    import pandas as pd
    import math
    
    print("\n",census_data_dirs[i],len(colnames))
    
    badnames        =   []
    non_numerics    =   []
    non_numerics_id =   []  
        
    for k in range(len(colnames)) :
            
        if(colnames[k].find(".")>-1) :
            if( (colnames[k].endswith(".1")) or 
               (colnames[k].endswith(".2")) or 
               (colnames[k].endswith(".3")) or 
               (colnames[k].endswith(".4")) or 
               (colnames[k].endswith("_"))) :
                badnames.append(colnames[k])
            
        if(not(is_numeric_col(merged_df,colnames[k]))) :
            non_numerics.append(colnames[k])
            non_numerics_id.append(k)
                
        if(colnames[k].find(" ")>-1) :
            badnames.append(colnames[k])

    print("\n File : ",census_data_dirs[i])
    print("bad names : ",str(len(badnames)),"\n",badnames)
    print("non numerics : ",str(len(non_numerics)))#,"\n",non_numerics)

    non_numerics_bad_vals   =   []
    bad_not_percent         =   []  
        
    tot_bad_vals            =   0
        
    for l in range(len(non_numerics)) :
            
        if( (non_numerics[l].endswith("_percent")) or
            (non_numerics[l].endswith("_mean")) or 
            (non_numerics[l].endswith("_median")) or 
            (non_numerics[l].endswith("_ratio"))):
            
            bad_vals    =   0
            bad_vals_dict           =   {}
                
            for m in range(len(merged_df)) :
                    
                try :
                    cdata   =   float(merged_df.iloc[m,non_numerics_id[l]])
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_id[l]]:cdata})
                except :
                    bad_vals = bad_vals + 1
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_id[l]]:np.nan})
                        
            tot_bad_vals    = tot_bad_vals + bad_vals
            non_numerics_bad_vals.append(bad_vals)
             
            #print(non_numerics[l],len(bad_vals_dict),tot_bad_vals)
            
            try :
                merged_df.replace({non_numerics[l]:bad_vals_dict},inplace=True)
            except :
                print("replace error : ",non_numerics[l],len(bad_vals_dict),merged_df[non_numerics[l]].nunique())
                if(non_numerics[l] == "population_age_median") :
                    uniques     =   merged_df[non_numerics[l]].unique()
                    print(type(uniques))
                        
                    print(type(uniques[0]))
                    nuniques = []
                    for t in range(len(uniques)) :
                        if(t>0):#not (np.isnan(uniques[t]))) :
                            nuniques.append(uniques[t])
                        
                    nuniques.sort()
                        
                    print("\n",len(nuniques),"\n",nuniques)
                        
                    print(bad_vals_dict.get('-'),type(bad_vals_dict.get('-')))
                    dictkeys    =   list(bad_vals_dict.keys())
                    ndictkeys = []
                    for t in range(len(dictkeys)) :
                        if(t>0):#not (np.isnan(dictkeys[t]))) :
                            ndictkeys.append(dictkeys[t])
                        
                        
                        
                    ndictkeys.sort()
                        
                    print("\n",len(ndictkeys),"\n",ndictkeys)
                        
                
            try :
                merged_df.astype({non_numerics[l]: 'float'},errors='ignore').dtypes
            except :
                print("float astype error : ",non_numerics[l])
                        
        elif( (non_numerics[l].endswith("_total")) or 
              (non_numerics[l].endswith("Code")) ) :
                    
            bad_vals    =   0
            bad_vals_dict           =   {}
                
            for m in range(len(merged_df)) :
                    
                try :
                    cdata   =   int(merged_df.iloc[m,non_numerics_id[l]])
                    if( (np.isneginf(cdata)) or (np.isneginf(cdata)) ) :
                        cdata   =  -1 
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_id[l]]:cdata})
                except :
                    bad_vals = bad_vals + 1
                    bad_vals_dict.update({merged_df.iloc[m,non_numerics_id[l]]:-1})
                        
            tot_bad_vals    = tot_bad_vals + bad_vals
            non_numerics_bad_vals.append(bad_vals)
                
            try :
                merged_df.replace({non_numerics[l]:bad_vals_dict},inplace=True)
            except :
                    
                print("replace error : ",len(bad_vals_dict),merged_df[non_numerics[l]].nunique())
                    
                uniques     =   merged_df[non_numerics[l]].unique()
                print("bad col : ",non_numerics[l])
                    
                from dfcleanser.common.common_utils import get_column_datatype
                print("bad col dt : ",get_column_datatype(merged_df,non_numerics[l]))
                    
                nuniques = []
                for t in range(len(uniques)) :
                        
                    try :
                        fg = uniques[t].isnumeric()    
                    except :
                        print("isnotnumeric",uniques[t])
                        
                       
                nuniques.sort()
                    
                print(uniques[0])
                print("\n",len(nuniques),"\n",nuniques[:400])
                        
                print(bad_vals_dict.get('-'),type(bad_vals_dict.get('-')))
                dictkeys    =   list(bad_vals_dict.keys())
                ndictkeys = []
                for t in range(len(dictkeys)) :
                    if(t>0):#not (np.isnan(dictkeys[t]))) :
                        ndictkeys.append(dictkeys[t])
                        
                        
                        
                ndictkeys.sort()
                print(dictkeys[0])    
                print("\n",len(ndictkeys),"\n",ndictkeys[:400])
                    
                    
                merged_df[non_numerics[l]].map(bad_vals_dict)
                
            try :
                if(bad_vals > 0) :
                    merged_df.astype({non_numerics[l]: 'float'},errors='ignore').dtypes
                else :
                    merged_df.astype({non_numerics[l]: 'int'},errors='ignore').dtypes
            except :
                print("int astype error : ",non_numerics[l])
                    
                    
        else :
                
            bad_not_percent.append(non_numerics[l])
                
            print("bad unknown",non_numerics[l])
                
    merged_df.to_csv(dfc_census_path + "\\" + "typed_" + census_data_dirs[i] + ".csv",index=False)
                
    typed_df        =   pd.read_csv(dfc_census_path+"\\"+ "typed_" + census_data_dirs[i] + ".csv")#,encoding='latin-1')
        
    #print("\ntyped col types",typed_df.dtypes)
               
    print(census_data_dirs[i],"total nan vals : ",tot_bad_vals,tot_bad_vals/(len(merged_df)*len(merged_df.columns)),"%\n",bad_not_percent)        
                
    print_datasets_stats(census_data_dirs,i,dfc_census_path,merged_df,colnames)
            
























          
            
            

