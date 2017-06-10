#!/usr/bin/env python3

import sys
import subprocess

import common

if __name__ == '__main__':
    print(sys.argv)
    if not len(sys.argv) > 2:
        print("Invalid usage: " + sys.argv[0] + " <branchname> <devicename>")
        sys.exit(1)

    # Get workspace location
    workspace = common.get_workspace_loc()

    # Clean workspace directory
    common.clean_directory(workspace)

    # Clean the out directory
    common.clean_directory(common.out_location)

    # Checkout the correct device in the local manifest
    common.checkout_device(sys.argv[1])
#    common.sync()
    common.docker_pull()
    common.run_in_docker('/scripts/build_bootimage.sh ' + sys.argv[2] + " eng")
    
    bootimg = common.check_one_file_eixsts(common.out_location + '/halium-boot-*.img')

    common.move_to_workspace(bootimg, workspace)

