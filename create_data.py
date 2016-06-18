from models import *
from sqlalchemy import *

db.drop_all()
db.create_all()

# create batch
keg1 = Keg('left_keg', 19684.1, "milliliters")
keg2 = Keg('right_keg', 19684.1, "milliliters")

db.session.add(keg1)
db.session.add(keg2)

# create beer
beer1 = Beer('daisy cutter')
beer2 = Beer('budweiser')
beer3 = Beer('kirin')

db.session.add(beer1)
db.session.add(beer2)
db.session.add(beer3)
db.session.commit()

# create batch
batch1 = Batch(beer1, keg1, 1)
batch2 = Batch(beer2, keg2, 1)
batch3 = Batch(beer3, keg1, 0)

db.session.add(batch1)
db.session.add(batch2)
db.session.add(batch3)
db.session.commit()
# create pour
pour1 = Pour(batch1, 100)

db.session.add(pour1)
db.session.commit()