# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:52:53 2019

Dog Model.  Predicting Ideal Nutrition Load for Doggy Paramaters

@author: vince
"""
from datetime import datetime

##Extra Fields
allowed_fields = ['breed', 'diseases', 'medications', 'activity']

class Dog(dict):

    
    def __init__(self, name='dog',
                 birthday=None, weight=None, sex=None,
                 **kwargs):
        
        self.name = name
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')
        self.weight = self.weight_conversion(weight)
        self.sex = self.sex_slug(sex)
        self.age = self.get_age()

        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_fields)
        
        #For Django.  def save(self, *args, **kwargs): if self.valid: super(Model, self).save(*args, **kwargs) else: raise ValidationError
        self.valid = self.validate()
        
        
    def get_age(self):
        '''
        return ~age in months
        '''
        daysOld = (datetime.now() - self.birthday).days
        return int(daysOld/30)
    def sex_slug(self, sexword):
        '''
        return m or f for male or female variations
        '''
        try:
            if 'fem' in sexword.lower():
                return 'female'
            else:
                return 'male'
        except AttributeError:
            print('Please Enter a Sex!')
    def weight_conversion(self, weightword):
        '''
        Convert string with kg or lb to weight in kg.  Returns float to 
        1 decimal.
        '''
        if 'lb' in weightword.lower():
            return round(float(weightword.split('l')[0])*0.453592, 1)
        elif 'kg' in weightword.lower():
            return round(float(weightword.split('k')[0]), 1)
        else:
            print('Enter weight in "lb" or "kg"')
            raise ValueError
    
    def validate(self):
        '''
        Build out validation ruleset
        '''
        if self.age:
            return True
        else:
            print('That age makes no sense.')
            raise ValueError
    
    def __dir__(self):
        return allowed_fields + ['name', 'age', 'sex', 'weight']
    
    def __str__(self):
        return self.name
            
    




