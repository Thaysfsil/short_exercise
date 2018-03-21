#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:00:15 2018

@author: thayssilva
"""
import re


def Inwardcode(InwardCode):#Verify Inward Code
    
    validationInward= False
    #Letter Exceptions:
    resemble_digits=['C', 'I', 'K', 'M', 'O', 'V']
    
    #verify 9AA format 
    if InwardCode[0].isnumeric() and (not InwardCode[1].isnumeric()) and ( not InwardCode[2].isnumeric()) :
        #verify AA letters
        if  (InwardCode[1] not in resemble_digits) and (InwardCode[2] not in resemble_digits):
            validationInward = True
        else:
            return validationInward
    else: 
        return validationInward
    
    return validationInward

def OutwardCode(OutwardCode):
    validationOutward=False
    
    #Letter Exceptions:
    not_in_first = ['Q', 'V','X']
    not_in_second =['I','J','Z']
    not_in_third = ['I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'V', 'X', 'Y', 'Z']
    in_fourth=['A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y']
 
    #Verify Outward Code     
    state="First"
    for x in range(len(OutwardCode)):
        
        if state == "First": #verify first Digit
            if OutwardCode[x].isnumeric() or OutwardCode[x] in not_in_first:
                return validationOutward
            else:
                state="Second"
                
        elif state == "Second": #verify second Digit
            if OutwardCode[x].isnumeric():
                state="Third"
            elif OutwardCode[x] not in not_in_second:
                state="Fourth"
            else:
                return validationOutward
            
        elif state == "Third": #verify third digit if second digit is number
            if OutwardCode[x].isnumeric() or OutwardCode[x] not in not_in_third:
                pass
            else:
                return validationOutward   
        elif state == "Fourth": #verify third digit if second digit is letter
            if OutwardCode[x].isnumeric():
                state="Fifth"
            else:
                return validationOutward
            
        elif state == "Fifth": #verify fourth digit when exist
            if OutwardCode[x].isnumeric() or OutwardCode[x]  in in_fourth:
                pass
            else:
                return validationOutward
    validationOutward = True
    return validationOutward
    
def ValidatePostcode(postcode):
    if (" ") in postcode:
        postcode = postcode.upper().split()
    else:
        return "Postcode invalid format"
    
    if  len(postcode) !=2:
        return "Postcode invalid format"
    else:
        outward,inward = postcode[0],postcode[1]
        if (len(outward)<=4 and len(inward) ==3):
            if not(re.match("^[a-zA-Z0-9_]*$", outward) and  re.match("^[a-zA-Z0-9_]*$", inward)):
                return "Postcode does not accept special character"
        else:
            return "Postcode invalid format"
    
    if (Inwardcode(inward) and OutwardCode(outward)):
        return True
    else:
        return False
            
        

        
    
    