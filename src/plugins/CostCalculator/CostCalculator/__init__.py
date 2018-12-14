"""
This is where the implementation of the plugin code goes.
The CostCalculator-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('CostCalculator')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class CostCalculator(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

        self.meta = {}

        METANodes = self.core.get_all_meta_nodes(active_node)

        for path in METANodes:
            node = METANodes[path]
            self.meta[core.get_attribute(node, 'name')] = node

        self.active_node_name = core.get_attribute(active_node, 'name')
        self.active_node_metatype_name=self.core.get_attribute(self.core.get_base_type(self.active_node), 'name')
        children=core.load_children(active_node)

        self.metatoname={}
        names_list = []
        for child in children:
            if core.is_type_of(child, self.meta['Connection']) or core.is_type_of(child, self.meta['Controls']):
                a=1
            elif core.is_type_of(child, self.meta['ICE']) or core.is_type_of(child, self.meta['Electric']):
                price=self.core.get_attribute(child, 'price')
                if self.core.get_attribute(self.core.get_base_type(child), 'name') not in self.metatoname.keys():
                    self.metatoname['Engine Type'] = []
                    self.metatoname['Engine Name'] = []
                    self.metatoname['Engine Type'].append({'Name':self.core.get_attribute(self.core.get_base_type(child), 'name'),'Price':price})
                    self.metatoname['Engine Name'].append({
                        'Name' : self.core.get_attribute(child, 'name'),'Price':0})

                else:
                    self.metatoname['Engine Type'].append(
                        {'Name': self.core.get_attribute(self.core.get_base_type(child), 'name'), 'Price': price})
                    self.metatoname['Engine Name'].append({
                        'Name': self.core.get_attribute(child, 'name'), 'Price': 0})

            elif core.is_type_of(child, self.meta['Brake']):
                if self.core.get_attribute(child, 'BrakeType') == 'DiscBrake':
                    price = 45
                else:
                    price = 35
                if self.core.get_attribute(self.core.get_base_type(child), 'name') not in self.metatoname.keys():
                    self.metatoname['Brake Type'] = []
                    self.metatoname['Brake Type'].append({'Name':self.core.get_attribute(child, 'BrakeType'),'Price':price})

                else:
                    self.metatoname['Brake Type'].append(
                        {'Name': self.core.get_attribute(child, 'BrakeType'), 'Price': price})

            elif core.is_type_of(child, self.meta['Frontdrive']) or core.is_type_of(child, self.meta['AllDrive']):
                price=self.core.get_attribute(child,'price')
                if self.core.get_attribute(self.core.get_base_type(child), 'name') not in self.metatoname.keys():
                    self.metatoname['Drive Train'] = []
                    self.metatoname['Drive Train'].append({'Name':self.core.get_attribute(self.core.get_base_type(child), 'name'),'Price':price})

                else:
                    self.metatoname['Drive Train'].append(
                        {'Name': self.core.get_attribute(self.core.get_base_type(child), 'name'), 'Price': price})

            elif core.is_type_of(child, self.meta['Multi-link']) or core.is_type_of(child, self.meta['Swing axle']) or core.is_type_of(child, self.meta['Semi-trail arm']):
                price = self.core.get_attribute(child, 'price')
                if self.core.get_attribute(self.core.get_base_type(child), 'name') not in self.metatoname.keys():
                    self.metatoname['Suspension'] = []
                    self.metatoname['Suspension'].append(
                        {'Name': self.core.get_attribute(self.core.get_base_type(child), 'name'), 'Price': price})

                else:
                    self.metatoname['Suspension'].append(
                        {'Name': self.core.get_attribute(self.core.get_base_type(child), 'name'), 'Price': price})

            elif core.is_type_of(child, self.meta['Wheels']):
                if self.core.get_attribute(child, 'WheelType') == 'Alloy Wheel':
                    price = 110
                else:
                    price = 120

                if self.core.get_attribute(self.core.get_base_type(child), 'name') not in self.metatoname.keys():
                    self.metatoname['Wheels'] = []
                    self.metatoname['Wheels'].append(
                        {'Name': self.core.get_attribute(child, 'WheelType'), 'Price': price})
                else:
                    self.metatoname['Wheels'].append(
                        {'Name': self.core.get_attribute(child, 'WheelType'), 'Price': price})

        name = core.get_attribute(active_node, 'name')


        logger.info('ActiveNode at "{0}" has name {1}'.format(core.get_path(active_node), name))

        #core.set_attribute(active_node, 'name', 'newName')

        commit_info = self.util.save(root_node, self.commit_hash, 'master', 'Python plugin updated the model')
        logger.info('committed :{0}'.format(commit_info))
        self.save_code()

    def get_code(self):
        code_text = 'The car parameters are:\n'
        #code_text += '{}: {}\n'.format(self.core.get_attribute(self.core.get_base_type(self.active_node), 'name'), self.active_node_name)
        #code_text += '{}\n'.format(self.metatoname)
        for key in self.metatoname.keys():
            for item in self.metatoname[key]:
                code_text += '{}: {}\n'.format(key, item['Name'])
            #code_text += '{} {}\n'.format(key, self.metatoname[key])

        total_cost=0
        for ki in self.metatoname.keys():
            cost = 0
            for items in self.metatoname[ki]:
                #code_text += '{} {}'.format(items,type(items))
                cost+=items['Price']
            total_cost += cost

        code_text += 'Total cost of car configuration is {}$\n'.format(total_cost)
        
        return code_text

    def save_code(self):
        self.add_file('{}.py'.format(self.active_node_name), self.get_code())