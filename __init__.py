from trytond.pool import Pool
from .health_agree import*

def register():
    Pool.register(
        Agree,
        module='health_agree', type_='model'
        )
