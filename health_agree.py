from trytond.model import ModelView, ModelSQL, fields, Unique
from datetime import datetime
from trytond.transaction import Transaction
from trytond import backend
from trytond.pyson import Eval
from trytond.pool import Pool


__all__ = ['Agree']
class Agree(ModelSQL, ModelView):
    'Agreements'
    __name__ = 'gnuhealth.agree'


    institution = fields.Char('Institution', translate=True, required=True, help="Institution name")
    date = fields.Date('Date Request', required=True)
    
    
    name = fields.Many2One(
        'party.party', 'Patient', required=True, 
        domain=[
            ('is_patient', '=', True),
            ('is_person', '=', True),
            ],
        states={'readonly': Eval('id', 0)>0},
        help= "Person associated to this patient")

 
   
    dob = fields.Function(fields.Date('DoB'), 'get_patient_dob')
    weight = fields.Char('Weight', required=True, help="Patient Weight")
    
    puid = fields.Function(
        fields.Char('Rut', help="Person Unique Identifier"),
        'get_patient_puid', searcher='search_patient_puid')
    
    age = fields.Function(fields.Char('Age'), 'get_patient_age')

    street = fields.Char('Street', required=True, help="Patient Street Residence")

    number = fields.Numeric('Number', required=True, help="Patient Number Residence")

    city = fields.Char('City', required=True, help="Patient City of Residence")
    
    phone_one = fields.Numeric('Phone (1)', required=True, help="Patien Main Phone")

    phone_two = fields.Numeric('Phone (2)', required=True, help="Patient Secondary Phone")

    diagnosis = fields.Char('Diagnosis', required=True, help="Patient diagnosis")

    doctor = fields.Many2One(
        'gnuhealth.healthprofessional', 'Doctor', required=True, 
        states={'readonly': Eval('id', 0)>0},
        help= "Doctor attends to this patient")

    def get_patient_dob(self, awef):
        return self.name.dob

    def get_patient_puid(self, name):
        return self.name.ref

    def get_patient_age(self, name):
        return self.name.age

    

    @classmethod
    def search_patient_puid(cls, name, clause):
        res = []
        value = clause[2]
        res.append(('name.ref', clause[1], value))
        return res
