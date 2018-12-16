"""
This is where the implementation of the plugin code goes.
The extractdata-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase
import json

# Setup a logger
logger = logging.getLogger('extractdata')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class extractdata(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node
        self.meta={}

        METANodes = self.core.get_all_meta_nodes(active_node)

        for path in METANodes:
            node = METANodes[path]
            self.meta[core.get_attribute(node, 'name')] = node

        self.name = core.get_attribute(active_node, 'name')

        logger.info('ActiveNode at "{0}" has name {1}'.format(core.get_path(active_node), self.name))

        #core.set_attribute(active_node, 'name', 'newName')

        commit_info = self.util.save(root_node, self.commit_hash, 'master', 'Python plugin updated the model')
        logger.info('committed :{0}'.format(commit_info))

        self.save_code()

    def create_tree(self, node):
        model={}
        model['name']=self.core.get_attribute(node, 'name')

        attribute_list=self.core.get_attribute_names(node)
        if self.core.get_meta_type(node) is not None:
            meta_type = self.core.get_attribute(self.core.get_meta_type(node), 'name')
            model['isMeta'] = self.core.is_meta_node(node)
            model['metaType']=meta_type
            if (self.core.is_type_of(node, self.meta['Controls']) or self.core.is_type_of(node, self.meta['Connection'])) and not self.core.is_meta_node(node):
                src = self.core.load_pointer(node, 'src')
                dst = self.core.load_pointer(node, 'dst')
                src_name = self.core.get_attribute(src, 'name')
                dst_name = self.core.get_attribute(dst, 'name')
                model['src'] = src_name
                model['dst'] = dst_name

        for attr in attribute_list:
            attr_value = self.core.get_attribute(node, attr)
            if attr!='name' and attr_value is not None:
                model[attr]=attr_value

        model['Children']={}
        children=self.core.load_children(node)

        for child in children:
            if len(children) == 0:
                continue
            path=child['nodePath']
            model['Children'][path]=self.create_tree(child)

        return model

    def get_meta(self):
        meta_data=[]
        for meta_name in self.meta.keys():
            meta_dict={}
            meta_dict['name']=meta_name
            meta_dict['path']=self.meta[meta_name]['nodePath']
            meta_dict['nbrofChildren']=len(self.core.load_children(self.meta[meta_name]))
            meta_dict['base']=self.core.get_attribute(self.core.get_base_type(self.meta[meta_name]),'name')
            meta_json=json.dumps(meta_dict)
            meta_data.append(meta_json)

        meta_data='[%s]' % ', '.join(map(str, meta_data))

        write_text='{}'.format(meta_data)

        return write_text

    def get_tree(self):

        model=self.create_tree(self.root_node)
        model=json.dumps(model)
        code_text='{}'.format(model)
        return code_text

    def save_code(self):
        self.add_file('tree.json', self.get_tree())
        self.add_file('meta.json', self.get_meta())