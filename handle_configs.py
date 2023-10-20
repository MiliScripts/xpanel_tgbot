import os
import yaml

def get_configs():
    cwd = os.getcwd().replace('\\','/')

    yaml_config_file= cwd+'/config/config.yml'
    with open(yaml_config_file,'r') as f:
        config = yaml.safe_load(f)

    return config    

#test
def get_msgs(p):
    cwd = os.getcwd().replace('\\','/')

    yaml_msgs_file= cwd+'/config/msg.yml'
    with open(yaml_msgs_file,'r',encoding='utf-8') as f:
        msgs = yaml.safe_load(f)

    return msgs[p]    

def get_extra(p):
    cwd = os.getcwd().replace('\\','/')

    yaml_extra_file= cwd+'/config/extra.yml'
    with open(yaml_extra_file,'r',encoding='utf-8') as f:
        extra= yaml.safe_load(f)
    
    return extra['iranian_months'][p]    

