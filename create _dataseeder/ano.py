from seeder.producer import PRODUCERS

# '{\n\t"name": v,\n\t"created_by": "system",\n\t"updated_by": "system"\n}'
# data = []
# list_name = []
# lala= PRODUCERS
# for da in PRODUCERS:
#     for val, v in da.items():
#             dataaa = f'[\n\t"name": "{v}",\n\t"sequence": ,\n\t"updated_by": "system"\n],\n'
#             lali = dataaa.replace('[', '{').replace(']', '}')
#             data.append(lali)
import os
entries = os.listdir('app/models/')
models_name = 'MODELS'
list_name = []
for data in entries:
    if data in ['__init__.py', '__pycache__']:
        continue
    else:
        file = data.replace('.py', '')
        dataaa = f'\t[\n\t\t"name": "{file}",\n\t\t"created_by": "system",\n\t\t"updated_by": "system"\n\t],\n'
        lali = dataaa.replace('[', '{').replace(']', '}')
with open('seeder/models.py', 'a', encoding='utf - 8') as f:
    f.write(f'{models_name} = [\n')
    for dat in list_name:
        f.write(f'{dat}')
    f.write(f']\n')

