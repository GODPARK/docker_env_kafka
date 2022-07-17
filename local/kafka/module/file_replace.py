import os
import argparse
import json

def is_file_path_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

def exit_with_msg(err_num=-1, msg='error'):
    print(msg)
    exit(err_num)

def validation_check_config(config_content):
    if not 'change' in config_content:
        exit_with_msg(msg="config check: change key check please")
    if len(config_content['change']) == 0:
        exit_with_msg(msg="config check: change key check please")
    for idx, config_valid in enumerate(config_content['change']):
        if not 'work_name' in config_valid:
            exit_with_msg(msg="work name is None: " + str(idx))
        if config_valid['work_name'] =='':
            exit_with_msg(msg="work name is blank: " + str(idx))

        if not 'file' in config_valid:
            exit_with_msg(msg="file is None: " + str(idx))
        if config_valid['file'] =='':
            exit_with_msg(msg="file is blank: " + str(idx))
        if not is_file_path_exists(config_valid['file']):
            exit_with_msg(msg="file path not valid: "+ str(idx))
            
        if not 'before' in config_valid:
            exit_with_msg(msg="before line is None: " + str(idx))
        if config_valid['before'] =='':
            exit_with_msg(msg="before is blank: " + str(idx))

        if not 'after' in config_valid:
            exit_with_msg(msg="after line is None: " + str(idx))
        if config_valid['after'] =='':
            exit_with_msg(msg="after is blank: " + str(idx))    

def replace_file_content(work_name, file_path, before, after):
    print(work_name)
    try:
        with open(file_path, "r+") as config:
            content = config.read()
            content = content.replace(
                before,
                after
            )
            config.seek(0)
            config.write(content)
            config.truncate()
        print("[success] replace ["+ file_path + "] as-is: "+ before + "--> to-be: " + after)
    except:
        exit_with_msg(msg= "[" + work_name + "]"+ file_path + "  = file replace error")


def main():
    parser = argparse.ArgumentParser(
        description="File replace APP"
    )
    parser.add_argument('--config', type=str, help="config file")
    args = parser.parse_args()
    
    config_file_path = args.config
    if not is_file_path_exists(config_file_path):
        exit_with_msg(-1, 'config file is not exsists')

    with open(config_file_path) as file:
        config_content = {}
        try:
            config_content = json.load(file)
        except:
            exit_with_msg(msg="json parse error, please check config json file")
        validation_check_config(config_content=config_content)
        for change in config_content["change"]:
            replace_file_content(
                work_name=change['work_name'],
                file_path=change['file'],
                before=change['before'],
                after=change['after']
            )


main()



