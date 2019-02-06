# -*- coding: utf-8 -*-
"""
SearchGuides
Created on Mon Feb  4 07:43:42 2019

Procedural Workflow for generating the model diet for given animal.
Goal:  All DB reads - no wrtites

(1) Function: Searches guidelines against animal model attributes and returns list of applicable guides
(2) Function: Creates model_diet from search fn and creates ModelDiet for animal 

@author: vince
"""

from DogModel import Dog
from Guidelines import Source, Element, Compound, Guideline

from collections import defaultdict


def read_animal(animal):
    '''
    Reads of all attribute data of object passed in.  
    '''
    attrDict = {}
    
    for attribute in dir(animal):
        try:
            attrDict[attribute] = getattr(animal, attribute)
        except:
            continue
        
    return attrDict


def search_guidelines(*args, **kwargs):
    '''
    Compare animal data to set of guidelines to see which apply
    use kwarg 'guides' to pass in a list of guides to check against
    '''
    app_guides = {}
    animal_data = args[0]
    
    int_std = .25 #std deviation for integer matching (STDVEV on Dog Model not available yet.  This is % difference from guideline value for now)
    range_check = False
    
    try:
        guides = kwargs['guides']    
    except:
        print('No guidelines provided')
        return False
    
    for guide in guides:
        for k,v in guide.tags.items():
            if k in animal_data:
                print('guide ', guide.title, 'v', v, ' animal data', animal_data[k])
                try:
                    guideVal = float(v)
                    animalVal = float(animal_data[k])
                    range_check = 2*abs((guideVal-animalVal))/(guideVal+animalVal) < int_std
                    print('range_check val: {}'.format(2*abs((guideVal-animalVal))/(guideVal+animalVal)))
                except ValueError:
                    range_check = False
                print('range_check ', range_check)
                
                if v == animal_data[k] or range_check:
                    app_guides[guide.title] = guide

    return app_guides

def compile_guidelines(*args):
    reqDict = defaultdict(list)
    guides = []
    
    if isinstance(args[0], dict):
        guideDict = args[0]
        for k,v in guideDict.items():
            guides.append(v)
            
        for guide in guides:
            for k,v in guide.requirement.items():
                reqDict[k].append(v)
        
    return reqDict
            


##Generate Test Data
    
dog1 = Dog(name='Trin', birthday='2016-10-01', weight='75lb', sex='Female', breed='shephard')
paper = Source(title='NewSource1 from Sexyhot vet', url="http://sexy.com")
paper2 = Source(title='great hair for dogs', url='http://bestpet.com')
iron = Element(name='iron', family='metal')
vitamina = Element(name='Vitamin A', family='vitamin')
liver = Compound(source=paper, name='liver', elements=iron)
liver.add_element(vitamina)
liver.add_source(paper2)

guide1Req = {
        'iron':'10 g/kg/day',
        'potato':'100 g/kg/day',
        }

guide2Req = {
        'protein':'25 g/kg/day',
        'fat':'10 g/kg/day',
        }

guide3Req = {
        'kale':'1 g/kg/day',
        'liver':'10 g/kg/day',
        }

guide1tags = {'name':'Bob',
              'sex': 'male',
              'age': '20'
              }

guide2tags = {'breed':'shephard',
              'age': 50
              }

guide3tags = {'breed':'heeler',
              'sex': 'female'
              }



guide1 = Guideline(title='guide1', source=paper, requirement=guide1Req, tags=guide1tags)
guide2 = Guideline(title='guide2', source=paper, requirement=guide2Req, tags=guide2tags)
guide3 = Guideline(title='guide3', source=paper, requirement=guide3Req, tags=guide3tags)

guideList = [guide1, guide2, guide3]