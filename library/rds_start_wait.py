#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.aws.core import AnsibleAWSModule

def start_rds(module, conn):
    has_changed = False
    #instance_name = module.params.get('instance_name')
    #response = conn.start_db_instance(instance_name)
    meta = {"start": "not yet implemented"}
    return (has_changed, response)

def stop_rds(module, conn):
    has_changed = False
    meta = {"stop": "not yet implemented"}
    return (has_changed, meta)

def main():

        fields = {
        "region": {"required": True, "type": "str"},
        "instance_name": {"required": True, "type": "str" },
        "description": {"required": False, "type": "str"},
        "wait_time": {"default": False, "type": "int" },
        "state": {
        	"default": "start",
        	"choices": ['start', 'stop'],
        	"type": 'str'
        },
	  }

        choice_map = {
            "start": start_rds,
            "stop": stop_rds,
        }

        module = AnsibleAWSModule(argument_spec=fields)
        conn = module.client('rds', retry_decorator=AWSRetry.jittered_backoff(retries=10))

        has_changed, result = choice_map.get(module.params['state'])(module.params)
        module.exit_json(changed=has_changed, meta=result)

if __name__ == '__main__':
    main()

