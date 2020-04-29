import boto3
import sys


def main(keyname,value):
    restag = boto3.client('ec2',region_name='us-east-1')
    response = restag.describe_instances()
    for resource in  response['Reservations'] :
        for instance in resource['Instances']:
            if instance[keyname] == value:
                print (instance['InstanceId'])

if __name__ == '__main__':
    keyname=sys.argv[1]
    value=sys.argv[2]
    main(keyname,value)