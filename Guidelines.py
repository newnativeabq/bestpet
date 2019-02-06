# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:28:19 2019

Diet Application

Create a Guideline model that contains applicability vector (list of tags to apply guideline to)

Given as dictionary of paramaters and weights.
Includes Source information
Includes Notes textfield

Store applicable data across multiple classes.

Source() -> Compound().element -> Guideline()
    
TODO:
    create object set and test queries against dog types

@author: vince
"""

from slugify import slugify

##Importing Animal Model for Testing only.  Do not include in final package
#from DogModel import Dog

class Source():
    def __init__(self, title, url=None):
        self.title=title
        self.slug_title = slugify(title)
        self.url = url

    def __str__(self):
        return self.title

class Element():
    '''
    Molecular component of given ingredient or compound.
    Common Families (simple str, separate families by comma):
        -Mineral, Metal, Vitamin, Preservative
        -Fat, Carbohydrate, Protein
    '''
    def __init__(self, name=None, family=None):
        self.name = name
        self.family = family
        
    def __str__(self):
        return self.name
        

class Compound():
    '''
    Compound or ingredient used in production of food.  Contains 2 or more elements.
    Common Compounds:
        -Sweet Potato, Onion, Beef, Duck Liver
    '''
    def __init__(self, source=None, name=None, elements=None):
        self.name = name    
        self.sources = [source]
        self.elements = [elements]
        
    def add_source(self, source):
        if self.sources:
            sourceList = self.sources
            
            for record in sourceList:
                if record.title == source.title:
                    print('Record already added for this compound.')
                    return self.source
            
            self.sources.append(source)
            return self.sources
        else:
            sourceList = [self.source]
            return sourceList

    def add_element(self, inputElement): #can this be generalized with getattr?
        self.elements.append(inputElement)
        return self.elements
    
    def __str__(self):
        return self.name

        

class Guideline():
    def __init__(self, title=None, source=None, requirement=None, tags=None):
        ''' tags is a dictionary of dog attributes for now 
            Requirements given as dictionary of key value pairs of the form:
                element/compound: <qty> <units>
                for qty==None use 0 and any unit
                units should be in g/kg/day
        '''
        self.sources = [source]
        self.tags = tags
        self.title = self.make_title(title) #build unique identifier.  There's no point in typing this in.
        self.requirement = requirement #build constructor/format function so dictionary input isn't required
        
    def make_title(self, text):
        return text + self.sources[0].slug_title[0:5]
        
    def add_source(self, source):
        if self.sources:
            for record in self.sources:
                if record.title == source.title:
                    print('Record already added for this guideline.')
                    return self.source
                
            self.sources.append(source)
            return self.sources
        else:
            sourceList = [self.source]
            return sourceList
    
    def __str__(self):
        return self.title

